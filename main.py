# def Get_small(list0):
#     if len(list0) == 1:
#         return list0[0]
#     list0.remove(max(list0))
#     return Get_small(list0)
#
#
# print(Get_small([1,2,2]))
from game_function import *
from people import Person

p1 = Person('P1')
p2 = Person('P2')

while True:
    if check_dead(p1, p2):
        break

    p1c = box.buttonbox('P1(blood:{}), 请选择：'.format(p1.life), p1.jn)
    if p1c == '进攻':
        p1.attacko(p2)
    elif p1c == '回血':
        p1.add_blood()
    elif p1c == '探究本草纲目':
        p1.yjbcgm()
    elif p1c == '买装备':
        p1.buy_zb()
    elif p1c is None:
        pass

    if check_dead(p1, p2):
        break

    p2c = box.buttonbox('P2(blood:{}), 请选择：'.format(p2.life), p2.jn)
    if p2c == '进攻':
        p2.attacko(p1)
    elif p2c == '回血':
        p2.add_blood()
    elif p2c == '探究本草纲目':
        p2.yjbcgm()
    elif p2c == '买装备':
        p2.buy_zb()
    elif p2c is None:
        pass
