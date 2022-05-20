# task

to bring up backend server

```
WSL@usr:~/task python -m venv .env-test

WSL@usr:~/task source .env-test/bin/activate

(env-test)
WSL@usr:~/task (master) $ cd backend

(env-test) 
WSL@usr:~/task/backend (master) $ uvicorn app.main:app --reload --port 8000

```

for frontend
```
WSL@usr:~/task cd frontend

WSL@usr:~/task/frontend npm i

WSL@usr:~/task/frontend npm run serve
```

NOTE: frontend should run on port 8080. or else we need to config the port in cors middleware in `backend.app.main.py`
