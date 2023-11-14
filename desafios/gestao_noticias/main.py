from noticia import Noticia
from gerenciador_noticias import salvar_noticias, carregar_noticias

def cadastrar_noticia(noticias):
    titulo = input("Título da notícia: ")
    categoria = input("Categoria da notícia: ")
    texto = input("Texto da notícia (máximo 400 letras): ")[:400]
    palavras_chave = input("Palavras-chave (separadas por vírgula): ").split(', ')
    
    noticia = Noticia(titulo, categoria, texto, palavras_chave)
    noticias.append(noticia)
    salvar_noticias(noticias)
    print("Notícia cadastrada com sucesso!")

def pesquisar_noticia(noticias):
    termo_pesquisa = input("Digite o termo de pesquisa: ").lower()
    for noticia in noticias:
        if (termo_pesquisa in noticia.titulo.lower() or
            termo_pesquisa in noticia.categoria.lower() or
            termo_pesquisa in noticia.texto.lower() or
            termo_pesquisa in [palavra.lower() for palavra in noticia.palavras_chave]):
            print("Título:", noticia.titulo)
            print("Categoria:", noticia.categoria)
            print("Texto:", noticia.texto)
            print("Palavras-Chave:", ', '.join(noticia.palavras_chave))
            print("-" * 30)

def alterar_noticia(noticias):
    titulo_alterar = input("Digite o título da notícia a ser alterada: ")
    for i, noticia in enumerate(noticias):
        if titulo_alterar.lower() == noticia.titulo.lower():
            print("Encontrada a notícia para alteração:")
            print("Título:", noticia.titulo)
            print("Categoria:", noticia.categoria)
            print("Texto:", noticia.texto)
            print("Palavras-Chave:", ', '.join(noticia.palavras_chave))
            print("-" * 30)
            
            novo_titulo = input("Novo título (ou Enter para manter o mesmo): ")
            noticia.titulo = novo_titulo if novo_titulo else noticia.titulo
            
            nova_categoria = input("Nova categoria (ou Enter para manter a mesma): ")
            noticia.categoria = nova_categoria if nova_categoria else noticia.categoria
            
            novo_texto = input("Novo texto (ou Enter para manter o mesmo): ")
            noticia.texto = novo_texto if novo_texto else noticia.texto
            
            novas_palavras_chave = input("Novas palavras-chave (ou Enter para manter as mesmas): ")
            noticia.palavras_chave = novas_palavras_chave.split(', ') if novas_palavras_chave else noticia.palavras_chave
            
            noticias[i] = noticia
            salvar_noticias(noticias)
            print("Notícia alterada com sucesso!")
            return
    print("Notícia não encontrada.")

def remover_noticia(noticias):
    titulo_remover = input("Digite o título da notícia a ser removida: ")
    for i, noticia in enumerate(noticias):
        if titulo_remover.lower() == noticia.titulo.lower():
            print("Encontrada a notícia para remoção:")
            print("Título:", noticia.titulo)
            print("Categoria:", noticia.categoria)
            print("Texto:", noticia.texto)
            print("Palavras-Chave:", ', '.join(noticia.palavras_chave))
            print("-" * 30)
            
            confirmacao = input("Deseja realmente remover esta notícia? (S para confirmar): ")
            if confirmacao.lower() == 's':
                del noticias[i]
                salvar_noticias(noticias)
                print("Notícia removida com sucesso!")
            return
    print("Notícia não encontrada.")

# Carregar notícias do arquivo CSV
noticias = carregar_noticias()

# Menu principal
while True:
    print("\nSistema de Gestão de Notícias")
    print("1. Cadastrar Notícia")
    print("2. Pesquisar Notícia")
    print("3. Alterar Notícia")
    print("4. Remover Notícia")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        cadastrar_noticia(noticias)
    elif opcao == '2':
        pesquisar_noticia(noticias)
    elif opcao == '3':
        alterar_noticia(noticias)
    elif opcao == '4':
        remover_noticia(noticias)
    elif opcao == '5':
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
