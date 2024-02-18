import math

def takeInputs():
    total = int(input("Enter total attendance "))
    abs = int(input("Enter Absent "))
    pre = int(input("Enter Present "))
    return total, abs, pre

def calcAtt(total, pre):
    att = float((pre/total) * 100)
    print("Attendance % : ", att)
    return att

def calcMargin(att):
    marg = ((math.ceil(75 - att)) / 100)* total
    print("Margin = ", marg)
    return

def future(total, pre):
    extra = int(input("Enter the Extra absent "))
    total += extra
    att = calcAtt(total, pre)
    required(total, pre)

def required(total, pre):
    req = 0
    currentAtt = 0
    while True:
        currentAtt = calcAtt(total, pre)
        if currentAtt < 75:
            total += 1
            req += 1
            pre += 1
        else: break
    print("Required : ", req)
    return

total, abs, pre = takeInputs()
att = calcAtt(total, pre)
calcMargin(att)
future(total, pre)





