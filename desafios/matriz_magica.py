def gerar_matriz_vazia(n_linhas, n_colunas):
    """Gera uma matriz de zeros com o número especificado de linhas e colunas."""
    return [[0]*n_colunas for _ in range(n_linhas)]

def exibir_matriz(matriz):
    """Exibe a matriz formatada."""
    for linha in matriz:
        for valor in linha:
            print(valor, "\t", end="")
        print()

def preencher_matriz_magica(matriz):
    """Preenche a matriz com o padrão mágico."""
    tamanho = len(matriz)
    linha = tamanho - 1
    coluna = int(linha / 2)
    tamanho_total = int((tamanho * tamanho))
    i = 1
    matriz[linha][coluna] = i
    
    while i < tamanho_total:       
        i += 1
        linha_save, coluna_save = linha, coluna
        linha, coluna = (linha + 1) % tamanho, (coluna + 1) % tamanho

        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = i
        else:
            linha, coluna = (linha_save - 1) % tamanho, coluna_save
            matriz[linha][coluna] = i

    exibir_matriz(matriz)

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da matriz: "))
    if tamanho % 2 == 0:
        print("O tamanho deve ser ímpar.")
    else:
        matriz = gerar_matriz_vazia(tamanho, tamanho)
        preencher_matriz_magica(matriz)
