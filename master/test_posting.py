def test_posting_sem_usuario_e_sem_mensagem(ctx):
    assert ctx.post("->") == "Comando inválido!"


def test_posting_sem_usuario(ctx):
    assert ctx.post("-> OLAR") == "Comando inválido!"


def test_posting_sem_mensagem(ctx):
    assert ctx.post("Day ->") == "Comando inválido!"


def test_posting_dois_operados(ctx):
    assert ctx.post("Day -> -> Msg") == "Comando inválido!"


def test_posting_operador_lugar_errado(ctx):
    assert ctx.post("-> Day Msg") == "Comando inválido!"


def test_posting_correto(ctx):
    assert ctx.post("Day -> OLAR") == "Postado com sucesso."


def test_posting_correto_nome_sobrenome(ctx):
    assert ctx.post("Day Day -> Msg") == "Postado com sucesso."