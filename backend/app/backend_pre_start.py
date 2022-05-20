import time
from app.database import db_session

max_retry = 5
retry_count = 0
print("Waiting for Postgres to start...")

while retry_count <= max_retry:
    try:
        db_session.execute("SELECT 1")
        print("Postgres is up!")
        break
    except Exception as e:
        print("Sleep for 3 seconds to let db and running...")
        time.sleep(3)
