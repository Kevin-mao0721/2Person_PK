import random as r
import ybc_box as box
from KJ_SHOP import KJShop
from ACK_SHOP import ACKShop


class Person:
    def __init__(self, name):
        self.name = name
        self.sk = KJShop()
        self.sa =ACKShop()
        self.p = box.buttonbox(name + ',请选择角色', ['吕布（伤害高）', '关羽（伤害抗性高）', '华佗（血量低， 治疗高）'])
        self.bcgme = False
        if self.p == '吕布（伤害高）':
            self.maxlife = 100.0
            self.life = 100.0
            self.add = [2, 5]
            self.bcgm = 0
            self.kj_attr = {'kj': 2,
                            'bkj': None,
                            'kjnj': None}
            self.ack_attr = {'ack': [5, 15],
                             'back': None,
                             'zcknj': None}
            self.dollar = 1000
            self.jn = ['进攻', '回血', '赚钱', '买卖装备', '探究本草纲目']
        elif self.p == '关羽（伤害抗性高）':
            self.maxlife = 100.0
            self.life = 100.0
            self.add = [2, 5]
            self.bcgm = 0
            self.kj_attr = {'kj': 3,
                            'bkj': None,
                            'kjnj': None}
            self.ack_attr = {'ack': [5, 10],
                             'back': None,
                             'zcknj': None}
            self.dollar = 1000
            self.jn = ['进攻', '回血', '赚钱', '买卖装备', '探究本草纲目']
        elif self.p == '华佗（血量低， 治疗高）':
            self.maxlife = 80.0
            self.life = 80.0
            self.add = [5, 8]
            self.bcgm = 0
            self.kj_attr = {'kj': 1,
                            'bkj': None,
                            'kjnj': None}
            self.ack_attr = {'ack': [5, 9],
                             'back': None,
                             'zcknj': None}
            self.dollar = 1000
            self.jn = ['进攻', '回血', '赚钱', '买卖装备', '探究本草纲目']
        else:
            self.maxlife = 50.0
            self.life = 50.0
            self.attack = [1, 2]
            self.add = [-5, 3]
            self.kj_attr = {'kj': 0,
                            'bkj': None,
                            'kjnj': None}
            self.ack_attr = {'ack': [1, 2],
                             'back': None,
                             'zcknj': None}
            self.dollar = 100
            self.jn = ['进攻', '回血', '赚钱', '买卖装备']

    def attacko(self, beattack):
        a = r.randint(self.ack_attr['ack'][0], self.ack_attr['ack'][1]) - beattack.kj_attr['kj']
        if a > 0:
            beattack.life -= a
            box.msgbox('造成伤害：{}滴血'.format(a))
        else:
            box.msgbox('没有造成伤害')
        if beattack.kj_attr['bkj'] is not None:
            beattack.kj_attr['kjnj'] -= 1
            if beattack.kj_attr['kjnj'] == 0:
                beattack.kj_attr['kj'] -= float(beattack.kj_attr['bkj'])
                beattack.kj_attr['kj'] = int(beattack.kj_attr['kj'])
                beattack.kj_attr['bkj'] = None
                beattack.kj_attr['kjnj'] = None
                box.msgbox(beattack.name + '的盔甲已破碎')

    def add_blood(self):
        a = r.randint(self.add[0], self.add[1])
        b = self.life + a - self.maxlife
        self.life += a
        if self.life > self.maxlife:
            self.life = self.maxlife
            box.msgbox('已暴血（爆{}滴血），所以倒扣{}血'.format(b, round(b / 2, 3)))
            self.life -= round(b / 2, 3)
            return
        box.msgbox('回血：{}滴血'.format(a))

    def yjbcgm(self, ee):
        if self.p == '华佗（血量低， 治疗高）':
            self.bcgm += 1
            self.life -= 1
            box.msgbox('本草纲目研究进度：+1，还需研究{}次'.format(3 - self.bcgm))
            if self.bcgm == 3:
                print(ee)
                if not ee:
                    box.msgbox('研究完毕，添加治疗上限, + 750元')
                    self.add = [5, 13]
                    self.dollar += 750
                    self.bcgme = True
                    self.jn = ['进攻', '回血', '赚钱', '买卖装备']
                else:
                    box.msgbox('研究完毕，添加治疗上限, + 100元')
                    self.add = [5, 13]
                    self.dollar += 100
                    self.jn = ['进攻', '回血', '赚钱', '买卖装备']
        else:
            a = r.randint(0, 3)
            self.bcgm += a
            self.life -= 5
            box.msgbox('本草纲目研究进度：+{}，还需研究{}次'.format(a, 10 - self.bcgm))
            if self.bcgm >= 10:
                print(ee)
                if not ee:
                    box.msgbox('研究完毕，添加治疗上限, + 500元')
                    self.add = [2, 8]
                    self.dollar += 500
                    self.bcgme = True
                    self.jn = ['进攻', '回血', '赚钱', '买卖装备']
                else:
                    box.msgbox('研究完毕，添加治疗上限, + 50元')
                    self.add = [2, 8]
                    self.dollar += 50
                    self.jn = ['进攻', '回血', '赚钱', '买卖装备']

    def buy_zb(self):
        a = box.buttonbox('你要去哪个市场？？？', ['刀剑市场', '盔甲市场'])
        if a == '刀剑市场':
            self.sa.come(self)
        else:
            self.sk.come(self)

    def earn_MN(self):
        if self.p == '华佗（血量低， 治疗高）':
            ra = r.randint(1, 120)
            self.dollar += ra
            box.msgbox('恭喜你赚到了{}元，你有{}元了！'.format(ra, self.dollar))
        else:
            ra = r.randint(1, self.life + 35)
            self.dollar += ra
            box.msgbox('恭喜你赚到了{}元，你有{}元了！'.format(ra, self.dollar))
