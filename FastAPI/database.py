from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Change the host to localhost for outside container, postgres for insdie the containner
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@postgres:5432/fastapi"
# Scheme: "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

Base = declarative_base()