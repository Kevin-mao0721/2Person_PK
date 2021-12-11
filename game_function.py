import ybc_box as box


def check_dead(p1, p2):
    if p1.life <= 0:
        box.msgbox('P2 Win!!!')
        return True
    elif p2.life <= 0:
        box.msgbox('P1 Win!!!')
        return True
