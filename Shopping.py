import ybc_box as box


class Shop:
    def __init__(self):
        pass

    def buy_kj(self, p):
        if p.bkj is None:
            k = box.choicebox('请选择（你有${}）'.format(p.dollar), ['1:石盔甲（耐久：24，盔甲+1）￥100',
                                                              '2:铁盔甲（耐久：47，盔甲+2）￥250',
                                                              '3:钻石甲（耐久：85，盔甲+3.5）￥500',
                                                              '4:金盔甲（耐久：37，盔甲+5）￥500'])
            kjn = int(k[0])
            if kjn == 3:
                kjd = int(k[20:])
            else:
                kjd = int(k[18:])

            if p.dollar >= kjd:
                if kjn == 1:
                    p.kj += 1
                    p.bkj = '1'
                    p.bkjnj = 24
                    p.dollar -= 100
                if kjn == 2:
                    p.kj += 2
                    p.bkj = '2'
                    p.bkjnj = 47
                    p.dollar -= 250
                if kjn == 3:
                    p.kj += 3.5
                    p.bkj = '3.5'
                    p.bkjnj = 85
                    p.dollar -= 500
                if kjn == 4:
                    p.kj += 5
                    p.bkj = '5'
                    p.bkjnj = 37
                    p.dollar -= 500
                box.msgbox('''购买成功!!!还剩{}元'''.format(p.dollar))
            else:
                box.msgbox('你买不起这套盔甲！！！')
        else:
            if p.bkj == '1':
                sell = int(100 / 24*p.bkjnj)
                if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                    p.kj -= float(p.bkj)
                    p.kj = int(p.kj)
                    p.bkj = None
                    p.bkjnj = None
                    p.dollar += sell
            elif p.bkj == '2':
                sell = int(250 / 47 * p.bkjnj)
                if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                    p.kj -= float(p.bkj)
                    p.kj = int(p.kj)
                    p.bkj = None
                    p.bkjnj = None
                    p.dollar += sell
            elif p.bkj == '3.5':
                sell = int(500 / 85 * p.bkjnj)
                if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                    p.kj -= float(p.bkj)
                    p.kj = int(p.kj)
                    p.bkj = None
                    p.bkjnj = None
                    p.dollar += sell
            elif p.bkj == '5':
                sell = int(500 / 37 * p.bkjnj)
                if box.ynbox('是否要卖出它？？？你可获得{}元'.format(sell)):
                    p.kj -= float(p.bkj)
                    p.kj = int(p.kj)
                    p.bkj = None
                    p.bkjnj = None
                    p.dollar += sell
