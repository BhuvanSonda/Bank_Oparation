import random
def ac_no(num):
    random.shuffle(num)
    list = ""
    for i in num:
        i = str(i)
        list += i
    list=int(list)

    return (list)

def accounts():
    d = {}
    for i in range(1, 2):
        name = input("enter your name :")
        d['Name'] = name
        ac_n = ac_no([1, 4, 2, 5, 3, 0, 7, 8, 9, 6])
        d['AC.NO'] = ac_n
        ifsc = (1362)
        d['IFSC'] = ifsc
        bl = ac_no([1, 4, 2, 5, 3, 0, ])
        d['Balance'] = bl
    return d

