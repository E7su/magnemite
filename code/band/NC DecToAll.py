
def DecToBin(num):
    IntPart = int(num)
    FloatPart = num - int(num)

    print(IntPart,FloatPart) #отладка
    
    BinIntPart = 0
    BinFloatPart = 0
    temp1 = 0
    i = 1
    j = 0.1
    
    while IntPart > 0:
        BinIntPart = BinIntPart + IntPart % 2 * i
        i = i * 10
        IntPart = int(IntPart / 2)

    while j > 0.000000000000000000001:
        temp1 = FloatPart * 2
        BinFloatPart = BinFloatPart + (int(temp1)) * j
        FloatPart = temp1 - int(temp1)
        j = j / 10

    BinFull = BinIntPart + BinFloatPart #возможно не нужно
    print('{:.20f}'.format(BinFull)) #отладка
    
    return BinIntPart, BinFloatPart


def BinToHex(HexInt, HexFloat):
    dic = {'0000':'0','1000':'8',
           '0001':'1','1001':'9',
           '0010':'2','1010':'A',
           '0011':'3','1011':'B',
           '0100':'4','1100':'C',
           '0101':'5','1101':'D',
           '0110':'6','1110':'E',
           '0111':'7','1111':'F'}
    
    print (str(HexInt), str(HexFloat)) #отладка
    HexInt = str(HexInt)
    if (len(HexInt)%4 != 0):
        HexInt = HexInt.rjust(8, '0') #корректировка, сделать динамически

    HexFull = ''    
    cut1=0
    cut2=4
    while(cut2<=len(HexInt)):
        temp1 = HexInt[cut1:cut2]
        for key in dic.keys():
            temp1 = temp1.replace(key, dic[key])
        cut1 += 4
        cut2 += 4
        HexFull += temp1

    HexFloat = str(HexFloat)[2:]
    if (len(HexFloat)%4 != 0):
        HexFloat = HexFloat.ljust(8, '0') #корректировка, сделать динамически

    HexFull += '.'
    
    cut1=0
    cut2=4
    while(cut2<=len(HexFloat)):
        temp1 = HexFloat[cut1:cut2]
        for key in dic.keys():
            temp1 = temp1.replace(key, dic[key])
        cut1 += 4
        cut2 += 4
        HexFull += temp1

    print(HexFull) #отладка   
    
    return HexFull

def BinToOct(OctInt, OctFloat):
    dic = {'000':'0','100':'4',
           '001':'1','101':'5',
           '010':'2','110':'6',
           '011':'3','111':'7'}
    
    OctInt = str(OctInt)
    if (len(OctInt)%3 != 0):
        OctInt = OctInt.rjust(9, '0') #корректировка, сделать динамически

    OctFull = ''    
    cut1=0
    cut2=3
    while(cut2<=len(OctInt)):
        temp1 = OctInt[cut1:cut2]
        for key in dic.keys():
            temp1 = temp1.replace(key, dic[key])
        cut1 += 3
        cut2 += 3
        OctFull += temp1

    OctFloat = str(OctFloat)[2:]
    if (len(OctFloat)%3 != 0):
        OctFloat = OctFloat.ljust(9, '0') #корректировка, сделать динамически

    OctFull += '.'
    
    cut1=0
    cut2=3
    while(cut2<=len(OctFloat)):
        temp1 = OctFloat[cut1:cut2]
        for key in dic.keys():
            temp1 = temp1.replace(key, dic[key])
        cut1 += 3
        cut2 += 3
        OctFull += temp1

    print(OctFull) #отладка   
    
    return OctFull


HexInt, HexFloat = DecToBin(255.6541)
BinToHex(HexInt, HexFloat)
BinToOct(HexInt, HexFloat)
print()
HexInt, HexFloat = DecToBin(30)
BinToHex(HexInt, HexFloat)
BinToOct(HexInt, HexFloat)
print()
print()
print()
print('============================')
HexInt, HexFloat = DecToBin(1.73858)
print()
HexInt, HexFloat = DecToBin(0.788336)
print()
print()
HexInt, HexFloat = DecToBin(0.105832)
print()
HexInt, HexFloat = DecToBin(0.105832)
print()
print()
print()
HexInt, HexFloat = DecToBin(3.63738)
print()
HexInt, HexFloat = DecToBin(5.08009)
print()
HexInt, HexFloat = DecToBin(3.23092)
print()
HexInt, HexFloat = DecToBin(0.790955)
print()
print()
HexInt, HexFloat = DecToBin(0.012371)
print()
HexInt, HexFloat = DecToBin(0.0247421)
print()
HexInt, HexFloat = DecToBin(0.012371)
print()
