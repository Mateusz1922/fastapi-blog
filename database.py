## database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db" # tells the sqlalchemy where to connect, blog.db generated automatically

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # facotry that creats db session, transaction with db, control the changes


class Base(DeclarativeBase):
    pass


def get_db(): # dependency func that provides session to our routes, calls this func for each request
    with SessionLocal() as db:
        yield db