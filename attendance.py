import math

def takeInputs():
    total = int(input("Enter total attendance "))
    pre = int(input("Enter Present "))
    return total, pre

def calcAtt(total, pre):
    att = float((pre/total) * 100)
    return att

def calcMargin(att):
    marg = math.ceil(((att - 75) / 100)* total)
    print("Margin =", marg)
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
    print("Required :", req)
    return

total, pre = takeInputs()
abs = total - pre
att = calcAtt(total, pre)
print("Attendance % :", att)
if att >= 75:
    calcMargin(att)
else: 
    required(total, pre)
choice = input("Wanna bunk? (y/n)")
if choice == 'y':
    future(total, pre)
print(total)





