from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#Engine is responsible for the connection pool, which will be used by the ORM to interact with the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#SessionLocal is a class that will be used to create a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Ten kod definiuje funkcję get_db(), która jest używana do uzyskania dostępu do bazy danych
# w aplikacji FastAPI. Funkcja ta korzysta z generatora yield w celu utworzenia obiektu sesji bazy danych,
# który jest zwracany jako kontekst. Po zakończeniu korzystania z sesji, funkcja get_db() automatycznie
# zamyka połączenie do bazy danych. Jest to często stosowany wzorzec w aplikacjach FastAPI,
# aby zapewnić prawidłowe zarządzanie połączeniami do bazy danych i uniknąć wycieków zasobów.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# we don't need that below code now, use sqlalchemy instead


# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="postgres",
#             cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected to the database!!!")
#         break
#     except (Exception, psycopg2.Error) as error:
#         print("Error while connecting to PostgreSQL", error)
#         time.sleep(5)