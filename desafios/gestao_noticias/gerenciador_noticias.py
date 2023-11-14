import csv
from noticia import Noticia

def salvar_noticias(noticias):
    with open('noticias.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Título', 'Categoria', 'Texto', 'Palavras-Chave'])
        for noticia in noticias:
            writer.writerow([noticia.titulo, noticia.categoria, noticia.texto, ', '.join(noticia.palavras_chave)])

def carregar_noticias():
    noticias = []
    try:
        with open('noticias.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Pular cabeçalho
            for row in reader:
                titulo, categoria, texto, palavras_chave = row
                noticias.append(Noticia(titulo, categoria, texto, palavras_chave.split(', ')))
    except FileNotFoundError:
        pass
    return noticias
