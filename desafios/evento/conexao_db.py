import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()


class ConexaoDB:
    def __init__(self):
        db_url = os.getenv("DB_URL")
        parsed_url = urlparse(db_url)
        self.host = parsed_url.hostname
        self.porta = parsed_url.port
        self.usuario = parsed_url.username
        self.senha = parsed_url.password
        self.banco = parsed_url.path.lstrip('/')
        self.connection = self.connect_to_db()
        self.create_tables()

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.porta,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inscricoes (
                    matricula INT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS entrada (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    matricula INT,
                    nome VARCHAR(255) NOT NULL,
                    hora_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (matricula) REFERENCES inscricoes (matricula)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS saida (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    matricula INT,
                    nome VARCHAR(255) NOT NULL,
                    hora_saida TIMESTAMP DEFAULT NULL,
                    FOREIGN KEY (matricula) REFERENCES inscricoes (matricula)
                )
            ''')
            self.connection.commit()
        except Error as e:
            print(f"Erro ao criar tabelas: {e}")


if __name__ == "__main__":
    conexao_db = ConexaoDB()
