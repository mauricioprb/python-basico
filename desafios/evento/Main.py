# main.py
from evento import Evento
from conexao_db import ConexaoDB

if __name__ == "__main__":
    conexao_db = ConexaoDB()
    evento = Evento(conexao_db)
    while True:
        print("\nMenu:")
        print("1. Inscrição")
        print("2. Listar Inscritos")
        print("3. Entrada no Evento")
        print("4. Saída do Evento")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            evento.inscricao()
        elif opcao == '2':
            evento.listar_inscritos()
        elif opcao == '3':
            evento.entrada_evento()
        elif opcao == '4':
            evento.saida_evento()
        elif opcao == '5':
            evento.sair()
        else:
            print("Opção inválida. Tente novamente.")
