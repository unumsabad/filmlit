from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambiar la contraseña dependiendo del dispositivo
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:0000@localhost:3306/FilmLit'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()