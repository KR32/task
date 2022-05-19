from fastapi import FastAPI, Request, Response
from app.database import Session, engine
from app.endpoint import router as user_router
from app.database import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

# TODO: move this into a separate file if more routers are added
app.include_router(user_router, prefix="/v1")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = Session()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
