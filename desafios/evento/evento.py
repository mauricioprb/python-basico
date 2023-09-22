# evento.py
from aifc import Error
import time
from conexao_db import ConexaoDB


class Evento:
    def __init__(self, conexao_db):
        self.conexao_db = conexao_db

    def inscricao(self):
        matricula = int(input("Informe a matrícula: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")

        try:
            cursor = self.conexao_db.connection.cursor()
            cursor.execute(
                "INSERT INTO inscricoes (matricula, nome, email) VALUES (%s, %s, %s)", (matricula, nome, email))
            self.conexao_db.connection.commit()
            print("Inscrição realizada com sucesso!")
        except Error as e:
            print(f"Erro ao realizar inscrição: {e}")

    def listar_inscritos(self):
        try:
            cursor = self.conexao_db.connection.cursor()
            cursor.execute("SELECT matricula, nome, email FROM inscricoes")
            inscritos = cursor.fetchall()
            print("\nLista de Inscritos:")
            for inscrito in inscritos:
                print(
                    f"Matrícula: {inscrito[0]}, Nome: {inscrito[1]}, Email: {inscrito[2]}")
        except Error as e:
            print(f"Erro ao listar inscritos: {e}")

    def entrada_evento(self):
        matricula = int(input("Informe a matrícula: "))
        nome = input("Informe o nome: ")

        try:
            cursor = self.conexao_db.connection.cursor()
            cursor.execute(
                "SELECT * FROM inscricoes WHERE matricula = %s AND nome = %s", (matricula, nome))
            inscrito = cursor.fetchone()
            if inscrito:
                cursor.execute(
                    "INSERT INTO entrada (matricula, nome) VALUES (%s, %s)", (matricula, nome))
                self.conexao_db.connection.commit()
                print("Entrada registrada com sucesso!")
            else:
                print("Inscrito não encontrado.")
        except Error as e:
            print(f"Erro ao registrar entrada: {e}")

    def saida_evento(self):
        matricula = int(input("Informe a matrícula: "))
        nome = input("Informe o nome: ")

        try:
            cursor = self.conexao_db.connection.cursor()
            cursor.execute(
                "SELECT * FROM entrada WHERE matricula = %s AND nome = %s", (matricula, nome))
            entrada = cursor.fetchone()
            if entrada:
                cursor.execute(
                    "INSERT INTO saida (matricula, nome, hora_saida) VALUES (%s, %s, NOW())", (matricula, nome))
                self.conexao_db.connection.commit()
                print("Saída registrada com sucesso!")
            else:
                print("Entrada não encontrada.")
        except Error as e:
            print(f"Erro ao registrar saída: {e}")

    def sair(self):
        self.conexao_db.connection.close()
        print("Programa encerrado.")
        exit()
