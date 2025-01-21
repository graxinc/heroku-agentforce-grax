from sqlalchemy import create_engine
from models import Base
import os
from dotenv import load_dotenv

load_dotenv()

def init_db():
    # Get database URL from environment
    db_url = os.environ.get("DATABASE_URL")
    if db_url and db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    # Create engine
    engine = create_engine(db_url)

    # Create all tables
    Base.metadata.create_all(engine)
    print("Database tables created!")

if __name__ == "__main__":
    init_db()