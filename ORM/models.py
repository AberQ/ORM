from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import os

host = os.getenv("DB_HOST", "host.docker.internal")
port = os.getenv("DB_PORT", "5432")
username = os.getenv("DB_USERNAME", "postgres")
password = os.getenv("DB_PASSWORD", "123")
database = os.getenv("DB_NAME", "orm")

DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database}'






try:
    engine = create_engine(
    DATABASE_URL, 
    echo=True
)

except Exception as e:
    print(f"Ошибка подключения к базе данных: {e}")
    exit()

Base = declarative_base()


class Defect(Base):
    __tablename__ = 'defects'
    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False)
    defect = Column(String(100), nullable=False)
    work_name = Column(String(100), nullable=False)
    unit = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<Defect(code='{self.code}', defect='{self.defect}', work_name='{self.work_name}', "
                f"unit='{self.unit}', count={self.count})>")

class Employer(Base):
    __tablename__ = 'employers'
    id = Column(Integer,  primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=False)
    sheets_sent = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<Employer(telegram_id={self.telegram_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', middle_name='{self.middle_name}', sheets_sent={self.sheets_sent})>")


try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Ошибка при создании таблиц: {e}")
    exit()


Session = sessionmaker(bind=engine)
session = Session()



