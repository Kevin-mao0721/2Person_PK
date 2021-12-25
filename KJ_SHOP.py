import ybc_box as box


class Shop:
    def come(self, p):
        if p.kj_attr['bkj'] is None:
            self.buy(p)
        else:
            self.sell(p)

    @staticmethod
    def buy(p):
        k = box.choicebox('请选择（你有${}）'.format(p.dollar), ['1:石盔甲（耐久：24，盔甲+1）￥100',
                                                          '2:铁盔甲（耐久：47，盔甲+2）￥250',
                                                          '3:钻石甲（耐久：85，盔甲+3.5）￥500',
                                                          '4:金盔甲（耐久：37，盔甲+5）￥500'])
        if k is None:
            box.msgbox('你已离开市场')
        kjn = int(k[0])
        if kjn == 3:
            kjd = int(k[20:])
        else:
            kjd = int(k[18:])

        if p.dollar >= kjd:
            if kjn == 1:
                p.kj_attr['kj'] += 1
                p.kj_attr['bkj'] = '1'
                p.kj_attr['kjnj'] = 24
                p.dollar -= 100
            if kjn == 2:
                p.kj_attr['kj'] += 2
                p.kj_attr['bkj'] = '2'
                p.kj_attr['kjnj'] = 47
                p.dollar -= 250
            if kjn == 3:
                p.kj_attr['kj'] += 3.5
                p.kj_attr['bkj'] = '3.5'
                p.kj_attr['kjnj'] = 85
                p.dollar -= 500
            if kjn == 4:
                p.kj_attr['kj'] += 5
                p.kj_attr['bkj'] = '5'
                p.kj_attr['kjnj'] = 37
                p.dollar -= 500
            box.msgbox('''购买成功!!!还剩{}元'''.format(p.dollar))
        else:
            box.msgbox('你买不起这套盔甲！！！')

    def sell(self, p):
        if p.kj_attr['bkj'] == '1':
            sell = int(100 / 24 * p.kj_attr['kjnj']) - (24 - p.kj_attr['kjnj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.kj_attr['kj'] -= float(p.kj_attr['bkj'])
                p.kj_attr['kj'] = int(p.kj_attr['kj'])
                p.kj_attr['bkj'] = None
                p.kj_attr['kjnj'] = None
                p.dollar += sell
        elif p.kj_attr['bkj'] == '2':
            sell = int(250 / 47 * p.kj_attr['kjnj']) - (47 - p.kj_attr['kjnj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.kj_attr['kj'] -= float(p.kj_attr['bkj'])
                p.kj_attr['kj'] = int(p.kj_attr['kj'])
                p.kj_attr['bkj'] = None
                p.kj_attr['kjnj'] = None
                p.dollar += sell
        elif p.kj_attr['bkj'] == '3.5':
            sell = int(500 / 85 * p.kj_attr['kjnj']) - (85 - p.kj_attr['kjnj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.kj_attr['kj'] -= float(p.kj_attr['bkj'])
                p.kj_attr['kj'] = int(p.kj_attr['kj'])
                p.kj_attr['bkj'] = None
                p.kj_attr['kjnj'] = None
                p.dollar += sell
        elif p.kj_attr['bkj'] == '5':
            sell = int(500 / 37 * p.kj_attr['kjnj']) - (37 - p.kj_attr['kjnj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.kj_attr['kj'] -= float(p.kj_attr['bkj'])
                p.kj_attr['kj'] = int(p.kj_attr['kj'])
                p.kj_attr['bkj'] = None
                p.kj_attr['kjnj'] = None
                p.dollar += sell

    @staticmethod
    def check_destroy(sell):
        if sell <= 0:
            if box.ynbox('卖出失败，是否销毁？？？'):
                box.msgbox('销毁成功！')
            else:
                box.msgbox('你已放弃销毁。')
