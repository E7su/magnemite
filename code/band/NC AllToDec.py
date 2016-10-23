 
def ToDec(num,base):
  
    print(num)
  
    DecIntPart = 0
    DecFloatPart = 0
    i = 0
    temp1 = 0
    cut1 = 0 
    cut2 = 1
    
    temp1 = str(num).upper()

    while temp1[cut1:cut2] != '.':
        cut1 += 1
        cut2 += 1
        i += 1
    
    cut1 = 0 
    cut2 = 1
    i -= 1
    
    while cut2 <= len(str(num)):
        if temp1[cut1:cut2] == '.':
            cut1 += 1
            cut2 += 1
        elif temp1[cut1:cut2] == 'A':
            DecIntPart += 10 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp1[cut1:cut2] == 'B':
            DecIntPart += 11 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp1[cut1:cut2] == 'C':
            DecIntPart += 12 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp1[cut1:cut2] == 'D':
            DecIntPart += 13 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp1[cut1:cut2] == 'E':
            DecIntPart += 14 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        elif temp1[cut1:cut2] == 'F':
            DecIntPart += 15 * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        
        else:
            DecIntPart += int(temp1[cut1:cut2]) * base ** i
            cut1 += 1
            cut2 += 1
            i -= 1
        
    print(DecIntPart)
        

ToDec(101.01,2)
print()
ToDec(10.0,8)
print()
ToDec('FF.A7',16)
print()
ToDec(202.01,2)
print()

print('----------------')
ToDec(1.10111101000100101000,2)
print()
ToDec(0.11001001110100000000,2)
print()
print()

ToDec(0.00011011000101111101,2)
print()
ToDec(0.00011011000101111101,2)
print()
print()

ToDec(11.10100011001010100000,2)
print()
ToDec(101.00010100100000000000,2)
print()
ToDec(11.00111011000111000000,2)
print()
ToDec(0.11001010011111001000,2)
print()
print()

ToDec(1.00000011001010101011,2)
print()
ToDec(1.00000110010101010111,2)
print()
ToDec(1.00000011001010101011,2)
print()
print()
