from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Password@0987@localhost/WorkAppDatabase"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Sessionloacal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()