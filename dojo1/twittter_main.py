
def post(nome = None):
    if nome is None:
        return "Post sem parametro"
    if nome == "->":
        return "Comando invalido!"
    postagem = nome.split("->")
    print(postagem)
    if postagem[1] == "":
        return "Post sem mensagem!"
    elif postagem[0] == "":
        return "Post sem usuario!"
    elif postagem[0][-1] != " ":
        return "Falta carcter fantasma!"

    
   