import os
SERVER_TYPE = os.getenv("SERVER_TYPE", "DEV")
STARTUP_COMMAND = os.getenv("STARTUP_COMMAND", "/start-reload.sh")

BACKEND_CORS_ORIGINS = os.getenv(
    "BACKEND_CORS_ORIGINS"
)

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", 'localhost')
POSTGRES_USER = os.getenv("POSTGRES_USER", 'postgres')
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", 'postgres')
POSTGRES_DB = os.getenv("POSTGRES_DB", 'app')
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)