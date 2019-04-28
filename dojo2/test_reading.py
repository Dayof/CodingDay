from twiter import *

def test_read_usuario_inexistente():
    assert read('wesley') == []

def test_post_and_read():
    post('Joao -> Funcionou!')
    assert read('Joao ') == [' Funcionou!']

    