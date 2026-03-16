import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load the keys from your .env file
load_dotenv()

def get_db_engine():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("❌ DATABASE_URL not found in .env file!")
    
    # Create the SQLAlchemy engine
    engine = create_engine(url)
    return engine

if __name__ == "__main__":
    # Test the connection
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            print("✅ Connection to Neon Postgres Successful!")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")