import ybc_box as box


class ACKShop:
    def come(self, p):
        if p.ack_attr['back'] is None:
            self.buy(p)
        else:
            self.sell(p)

    def buy(self, p):
        k = box.choicebox('请选择（你有${}）'.format(p.dollar), ['1:石剑（耐久：26，最低，最高伤害+2）￥150',
                                                              '2:铁剑（耐久：50，最低，最高伤害+3）￥300',
                                                              '3:钻石剑（耐久：88，最低，最高伤害+5）￥700',
                                                              '4:金剑（耐久：40，最高伤害+8）￥700'])
        if k is None:
            box.msgbox('你已离开市场')
        kjn = int(k[0])
        if kjn == 3:
            kjd = int(k[23:])
        elif kjn == 4:
            kjd = int(k[19:])
        else:
            kjd = int(k[22:])

        if p.dollar >= kjd:
            if kjn == 1:
                p.ack_attr['ack'][0] += 2
                p.ack_attr['ack'][1] += 2
                p.ack_attr['back'] = '2'
                p.ack_attr['zcknj'] = 26
                p.dollar -= 100
            if kjn == 2:
                p.ack_attr['ack'][0] += 3
                p.ack_attr['ack'][1] += 3
                p.ack_attr['back'] = '3'
                p.ack_attr['zcknj'] = 50
                p.dollar -= 250
            if kjn == 3:
                p.ack_attr['ack'][0] += 5
                p.ack_attr['ack'][1] += 5
                p.ack_attr['back'] = '5'
                p.ack_attr['zcknj'] = 88
                p.dollar -= 500
            if kjn == 4:
                p.ack_attr['ack'][1] += 8
                p.ack_attr['back'] = '8'
                p.ack_attr['zcknj'] = 40
                p.dollar -= 500
            box.msgbox('''购买成功!!!还剩{}元'''.format(p.dollar))
        else:
            box.msgbox('你买不起这个剑！！！')

    def sell(self, p):
        if p.ack_attr['back'] == '1':
            sell = int(150 / 26 * p.ack_attr['zcknj']) - (26 - p.ack_attr['zcknj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.ack_attr['ack'][0] -= float(p.ack_attr['back'])
                p.ack_attr['ack'][1] -= float(p.ack_attr['back'])
                p.ack_attr['ack'] = int(p.ack_attr['ack'])
                p.ack_attr['back'] = None
                p.ack_attr['zcknj'] = None
                p.dollar += sell
        elif p.ack_attr['back'] == '2':
            sell = int(300 / 50 * p.ack_attr['zcknj']) - (50 - p.ack_attr['zcknj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.ack_attr['ack'][0] -= float(p.ack_attr['back'])
                p.ack_attr['ack'][1] -= float(p.ack_attr['back'])
                p.ack_attr['ack'] = int(p.ack_attr['ack'])
                p.ack_attr['back'] = None
                p.ack_attr['zcknj'] = None
                p.dollar += sell
        elif p.ack_attr['back'] == '3.5':
            sell = int(700 / 88 * p.ack_attr['zcknj']) - (88 - p.ack_attr['zcknj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.ack_attr['ack'][0] -= float(p.ack_attr['back'])
                p.ack_attr['ack'][1] -= float(p.ack_attr['back'])
                p.ack_attr['back'] = None
                p.ack_attr['zcknj'] = None
                p.dollar += sell
        elif p.ack_attr['back'] == '5':
            sell = int(700 / 40 * p.ack_attr['zcknj']) - (40 - p.ack_attr['zcknj']) / 2 - 1
            self.check_destroy(sell)
            if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                p.ack_attr['ack'][1] -= float(p.ack_attr['back'])
                p.ack_attr['ack'] = int(p.ack_attr['ack'])
                p.ack_attr['back'] = None
                p.ack_attr['zcknj'] = None
                p.dollar += sell

    @staticmethod
    def check_destroy(sell):
        if sell <= 0:
            if box.ynbox('卖出失败，是否销毁？？？'):
                box.msgbox('销毁成功！')
            else:
                box.msgbox('你已放弃销毁。')
