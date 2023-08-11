import random


def gerar_letras(quantidade):
    return random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=quantidade)


def gerar_placa():
    # Gera as letras aleatórias
    letras = gerar_letras(3)
    # Gera o primeiro número aleatório
    numero1 = random.randint(0, 9)
    # Gera a letra aleatória
    letra = gerar_letras(1)[0]
    # Gera os dois últimos números aleatórios
    numero2 = random.randint(0, 9)
    numero3 = random.randint(0, 9)
    # Retorna a placa gerada
    return f"{letras[0]}{letras[1]}{letras[2]}{numero1}{letra}{numero2}{numero3}"


quantidade_placas = int(input("Quantas placas deseja gerar? "))

# Loop para gerar as placas
for i in range(quantidade_placas):
    # Gera a placa
    placa = gerar_placa()
    print(placa)
