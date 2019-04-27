from datetime import datetime

TIMELINES, SUBSCRIPTIONS = {}, {}


def post(cmd):
    global TIMELINES, SUBSCRIPTIONS

    msg = "Comando inválido!"
    if cmd.count('->') != 1:
        return msg

    pre_pos_cmd = cmd.split('->')
    if len(pre_pos_cmd) != 2:
        return msg

    post_user, post_msg = pre_pos_cmd
    if not (post_user and post_msg):
        return msg

    post_user = post_user.strip()
    post_msg = post_msg.strip()

    TIMELINES.setdefault(post_user, []).append({'msg': post_msg,
                                                'dt': datetime.now().isoformat()})

    return "Postado com sucesso."


def reading(user):
    if user not in TIMELINES:
        return []

    dt_now = datetime.now()
    msgs = []
    for msg in TIMELINES[user]:
        dt_from_post = datetime.strptime(msg['dt'], "%Y-%m-%dT%H:%M:%S.%f")
        dt_res = (dt_now - dt_from_post).total_seconds() / 60.0  # days into minutes
        if dt_res < 1:
            dt_msg = 'posted now'
        else:
            dt_res = round(dt_res)
            dt_msg = f'{dt_res} minutes ago'
        msgs.append(f"{user} -> {msg['msg']} ({dt_msg})")
    return msgs


def follow(cmd):
    global SUBSCRIPTIONS

    msg = "Comando inválido!"
    if cmd.count('follows') != 1:
        return msg

    pre_pos_cmd = cmd.split('follows')
    if len(pre_pos_cmd) != 2:
        return msg

    post_user_or, post_user_dest = pre_pos_cmd
    if not (post_user_or and post_user_dest):
        return msg

    post_user_or = post_user_or.strip()
    post_user_dest = post_user_dest.strip()

    SUBSCRIPTIONS.setdefault(post_user_or, []).append(post_user_dest)

    return "Inscrição realizada com sucesso."


def wall(cmd):
    msg = "Comando inválido!"
    if cmd.count('wall') != 1:
        return msg

    res = cmd.split(' ')
    if len(res) != 2:
        return msg

    cmd_user, cmd = res
    if not cmd_user:
        return msg

    cmd_user = cmd_user.strip()

    if not SUBSCRIPTIONS.get(cmd_user):
        return []

    msgs = reading(cmd_user)

    for user in SUBSCRIPTIONS[cmd_user]:
        if user in TIMELINES:
            msgs.extend(reading(user))
        
    return msgs