def test_following_sem_usuario_origem_destino(ctx):
    assert ctx.follow("follows") == "Comando inválido!"


def test_following_sem_usuario_origem(ctx):
    assert ctx.follow("follows BoB") == "Comando inválido!"


def test_following_sem_usuario_destino(ctx):
    assert ctx.follow("Day follows") == "Comando inválido!"


def test_following_dois_operados(ctx):
    assert ctx.follow("Day follows follows BoB") == "Comando inválido!"


def test_following_operador_lugar_errado(ctx):
    assert ctx.follow("follows Day BoB") == "Comando inválido!"


def test_following_correto(ctx):
    assert ctx.follow("Day follows BoB") == "Inscrição realizada com sucesso."


def test_following_correto_nome_sobrenome_origem(ctx):
    assert ctx.follow("Day Day follows BoB") == "Inscrição realizada com sucesso."


def test_following_correto_nome_sobrenome_destino(ctx):
    assert ctx.follow("Day follows BoB Lob") == "Inscrição realizada com sucesso."


def test_wall_sem_usuario_origem(ctx):
    assert ctx.wall("wall") == "Comando inválido!"


def test_wall_com_usuario_a_mais(ctx):
    assert ctx.wall("Day wall BoB") == "Comando inválido!"


def test_wall_correto_nenhum_follows(ctx):
    assert ctx.wall("Day wall") == []


def test_wall_correto_um_follow_sem_post(ctx):
    ctx.follow('Day follows BoB')
    assert ctx.wall("Day wall") == []


def test_wall_correto_um_follow_um_post_origem(ctx):
    p1 = 'Day -> Awesome Dojo'
    ctx.post(p1)
    ctx.follow('Day follows BoB')
    assert ctx.wall('Day wall') == [p1 + ' (posted now)']


def test_wall_correto_um_follow_um_post_destino(ctx):
    p1 = 'BoB -> Awesome Dojo'
    ctx.post(p1)
    ctx.follow('Day follows BoB')
    assert ctx.wall('Day wall') == [p1 + ' (posted now)']


def test_wall_correto_um_follow_um_post_origem_e_destino(ctx):
    p1 = 'Day -> YAS Awesome Dojo'
    ctx.post(p1)
    ctx.follow('Day follows BoB')
    p2 = 'BoB -> Awesome Dojo'
    ctx.post(p2)
    assert ctx.wall('Day wall') == [p1 + ' (posted now)',
                                    p2 + ' (posted now)']


def test_wall_correto_dois_follows_um_post_origem_e_destino(ctx):
    p1 = 'Day -> YAS Awesome Dojo'
    ctx.post(p1)
    ctx.follow('Day follows BoB')
    p2 = 'BoB -> Awesome Dojo'
    ctx.post(p2)
    ctx.follow('Day follows Charlie')
    p3 = 'Charlie -> Yes indeed'
    ctx.post(p3)
    assert ctx.wall('Day wall') == [p1 + ' (posted now)', 
                                    p2 + ' (posted now)',
                                    p3 + ' (posted now)']
