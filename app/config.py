from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv(usecwd=True))

#ORIGINAL
#load_dotenv(dotenv_path=".env")  # Carrega as variáveis de ambiente do arquivo .env

#db_user = os.getenv("POSTGRES_USER")
#db_password = os.getenv("POSTGRES_PASSWORD")
#db_name = os.getenv("POSTGRES_DB")
#db_host = os.getenv("DB_HOST")
#db_port = os.getenv("DB_PORT")
#FIM_ORIGINAL


db_user = "meu_usuario"
db_password = "minha_senha"
db_name = "meu_banco"
db_host = "localhost"
db_port = "5432"

# Configurando a conexão com o banco de dados

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#print("troubleshooting2")
#print(DATABASE_URL)

# Criando a engine de conexão

engine = create_engine(DATABASE_URL)

# Criando a sessão

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()