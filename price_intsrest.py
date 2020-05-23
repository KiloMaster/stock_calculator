


def cal1_seg_money_count(all, deta, lmt, price, jian = True):
    seg_money = all/lmt
    count = 0 
    price_now = price
    for i in range(0, int(lmt)):
        count = count + int(seg_money/ price_now)
        if jian == True:
            price_now = price_now - deta
        else:
            price_now = price_now + deta

    return count

def cal1_dijia_count(all, deta, lmt, price):
    count = cal1_seg_money_count(all, deta, lmt, price, jian = False)
    return count

def cal1_dijian_count(all, deta, lmt, price):
    count = cal1_seg_money_count(all, deta, lmt, price, jian = True)
    return count    

def cal1_dijia_interest(all, deta, lmt, price, mubiaojia):
    ct = cal1_dijia_count(all, deta, lmt, price)
    interest = ct * mubiaojia - all 
    return interest

def cal1_dijian_interest(all, deta, lmt, price, mubiaojia):
    ct = cal1_dijian_count(all, deta, lmt, price)
    interest = ct * mubiaojia - all 
    return interest


if __name__ == '__main__':
    import sys
    cmd =  sys.argv[1] 
    p1 = float(sys.argv[2])
    p2 = float(sys.argv[3])
    p3 = float(sys.argv[4])
    p4 = float(sys.argv[5])

    if cmd == 'jia':
        print('dijia: %d' % cal1_dijia(p1, p2, p3, p4))
    elif cmd == 'jian' :
        print('dijian: %d' % cal1_dijian(p1, p2, p3, p4))
    elif cmd == 'jiaInterest':
        p5 = float(sys.argv[6])
        boCount = 1
        if len(sys.argv) == 8:
            boCount = int(sys.argv[7])
        p1_bak = p1 
        for i in range(0, boCount):    
            inte = cal1_dijia_interest(p1, p2, p3, p4, p5)
            print('jiaInterest, %d: %d: %f ' % (i, inte, inte/ p1))
            p1 = p1 + inte
        print('all money: %d' % p1)
        print('all interest: %d' % (p1 - p1_bak))
    elif cmd == 'jianInterest':
        p5 = float(sys.argv[6])
        boCount = 1
        if len(sys.argv) == 8:
            boCount = int(sys.argv[7])
        p1_bak = p1 
        for i in range(0, boCount):    
            inte = cal1_dijian_interest(p1, p2, p3, p4, p5)
            print('jianInterest, %d: %d: %f ' % (i, inte, inte/ p1))
            p1 = p1 + inte
        print('all money: %d' % p1)
        print('all interest: %d' % (p1 - p1_bak))
