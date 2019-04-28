time_line = {}

def post(cmd):
    global time_line

    var = cmd.split('->')

    if len(var) == 1:
        return 'Sem Operador'

    usuario = var[0]
    mensagem = var[1]
    if len(usuario) == 0:
        if len(mensagem) == 0:
            return 'ERRO!'
        return 'ERRO! Sem usuario'
    elif len(mensagem) == 0:
        return 'ERRO! Sem mensagem'

    if len(usuario) != 0 and len(mensagem) != 0:
        time_line[usuario] = [mensagem]
        print(time_line[usuario])
        print (time_line)
        return 'Mensagem postada'

def read(user):
    if user in time_line:
        return time_line[user]
    return []
