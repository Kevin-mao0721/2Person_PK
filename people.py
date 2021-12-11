import random as r
import ybc_box as box


class Person:
    def __init__(self, name):
        self.p = box.buttonbox(name + ',请选择角色', ['吕布（伤害高）', '关羽（伤害抗性高）', '华佗（血量低， 治疗高）'])
        if self.p == '吕布（伤害高）':
            self.life = 100
            self.attack = [5, 15]
            self.kj = 2
            self.add = [2, 5]
            self.bcgm = 0
            self.jn = ['进攻', '回血', '探究本草纲目']
        elif self.p == '关羽（伤害抗性高）':
            self.life = 100
            self.attack = [5, 10]
            self.kj = 3
            self.add = [2, 5]
            self.bcgm = 0
            self.jn = ['进攻', '回血', '探究本草纲目']
        elif self.p == '华佗（血量低， 治疗高）':
            self.life = 80
            self.attack = [5, 10]
            self.kj = 1
            self.add = [5, 8]
            self.bcgm = 0
            self.jn = ['进攻', '回血', '探究本草纲目']
        else:
            self.life = 50
            self.attack = [1, 2]
            self.kj = 0
            self.add = [-5, 3]
            self.jn = ['进攻', '回血']

    def attacko(self, beattack):
        a = r.randint(self.attack[0], self.attack[1]) - beattack.kj
        if a > 0:
            beattack.life -= a
            box.msgbox('造成伤害：{}滴血'.format(a))
        else:
            box.msgbox('没有造成伤害')

    def add_blood(self):
        a = r.randint(self.add[0], self.add[1])
        self.life += a
        box.msgbox('回血：{}滴血'.format(a))

    def yjbcgm(self):
        if self.p == '华佗（血量低， 治疗高）':
            self.bcgm += 1
            self.life -= 1
            box.msgbox('本草纲目研究进度：+1，还需研究{}次'.format(3-self.bcgm))
            if self.bcgm == 3:
                box.msgbox('研究完毕，添加治疗上限')
                self.add = [5, 13]
                self.jn = ['进攻', '回血']
        else:
            a = r.randint(0, 3)
            self.bcgm += a
            self.life -= 5
            box.msgbox('本草纲目研究进度：+{}，还需研究{}次'.format(a, 10 - self.bcgm))
            if self.bcgm >= 10:
                self.add = [2, 8]
                self.jn = ['进攻', '回血']
