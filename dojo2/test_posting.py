from twiter import post

def test_post_sem_usuario_sem_mensagem():
    assert post('->') == 'ERRO!'

def test_post_sem_usuario_com_mensagem():
    assert post('-> mensagem') == 'ERRO! Sem usuario'

def test_post_com_usuario_sem_mensagem():
    assert post('artur ->') == 'ERRO! Sem mensagem'

def test_post_com_usuario_com_mensagem():
    assert post('artur -> mensagem') == 'Mensagem postada'

def test_post_sem_operador():
    assert post('artur mensagem') == 'Sem Operador'

    