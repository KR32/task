from fastapi import FastAPI, Request, Response
from app.database import Session, engine
from app.endpoint import router as user_router
from app.database import Base
from app import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="UserReg", openapi_url="/api/v1/openapi.json")

Base.metadata.create_all(bind=engine)

# TODO: move this into a separate file if more routers are added
app.include_router(user_router, prefix="/api/v1")

# CORS
origins = []

# Set all CORS enabled origins
if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(",")
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = Session()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
