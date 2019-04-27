import pytest


def test_reading_sem_post(ctx):
    assert ctx.reading('Day') == []


def test_reading_com_um_post(ctx):
    msg = 'Day -> OLAR'
    ctx.post(msg)
    assert ctx.reading('Day') == [msg + ' (posted now)']


def test_reading_com_dois_posts(ctx):
    msg1, msg2 = 'Day -> OLAR', 'Day -> Hi'
    ctx.post(msg1), ctx.post(msg2)
    assert ctx.reading('Day') == [msg1+' (posted now)', msg2+' (posted now)']


def test_reading_com_dois_posts_usuarios_diferentes(ctx):
    msg1, msg2 = 'Day -> OLAR', 'BoB -> Hi'
    ctx.post(msg1), ctx.post(msg2)
    assert ctx.reading('Day') == [msg1+' (posted now)'] and ctx.reading('BoB') == [msg2+' (posted now)']


@pytest.mark.long
def test_reading_com_dois_posts_ordenados_por_tempo(ctx):
    import time
    msg1, msg2 = 'Day -> OLAR', 'Day -> OLAR after 1 min'
    ctx.post(msg1)
    assert ctx.reading('Day') == [msg1+' (posted now)']
    time.sleep(62), ctx.post(msg2)
    assert ctx.reading('Day') == [msg1+' (1 minutes ago)', msg2+' (posted now)']