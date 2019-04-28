import twittter_main

def test_post_sem_usuario_sem_msg():
    assert twittter_main.post('->') == 'Comando invalido!'

def test_post_sem_msg():
    assert twittter_main.post("Alice ->") == "Post sem mensagem!"

def test_post_sem_usuario():
    assert twittter_main.post("-> Estamos no coding day") == "Post sem usuario!"

def test_post_sem_parametro():
    assert twittter_main.post() == "Post sem parametro"

def test_post_usuario_caracter_fantasma():
    assert twittter_main.post("alice->mensagem") == "Falta carcter fantasma!"