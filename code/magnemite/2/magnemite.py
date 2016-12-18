import math
import matplotlib.pyplot as plt
import matplotlib.style as stl

max_in = 0
max_out = 0

# -----//-----
z11 = 0
z12 = 0
z13 = 0
z14 = 0

z21 = 0
z22 = 0
z23 = 0
z24 = 0

z31 = 0
z32 = 0
z33 = 0
z34 = 0

z41 = 0
z42 = 0
z43 = 0
z44 = 0

# -----//-----
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0

cascade1 = 0
cascade2 = 0
cascade3 = 0
cascade4 = 0

# -----//-----
a10 = 0.01756930
a20 = 0.01608500 
a30 = 0.01510810 
a40 = 0.01462730

a11 = 0.00000000 
a21 = 0.00000000 
a31 = 0.00000000 
a41 = 0.00000000

a12 = -0.0351387 
a22 = -0.0321700  
a32 = -0.0302162 
a42 = -0.0292546

a13 = 0.00000000 
a23 = 0.00000000 
a33 = 0.00000000 
a43 = 0.00000000

a14 = 0.01756930 
a24 = 0.01608500 
a34 = 0.01510810 
a44 = 0.01462730

# -----//-----
b10 =  1.000000 
b20 =  1.000000 
b30 =  1.000000
b40 =  1.000000

b11 = -3.76806
b21 = -3.61596 
b31 = -3.51586 
b41 = -3.46659

b12 =  5.44044
b22 =  4.9808   
b32 =  4.6783    
b42 =  4.52942

b13 = -3.57152 
b23 = -3.10354 
b33 = -2.79544  
b43 = -2.64395

b14 =  0.900116 
b24 =  0.739586 
b34 =  0.633933  
b44 =  0.581937

k_period = int(input('k_period: '))
F_in = int(input('F_in: '))
Fd = int(input('Fd: '))

w = 2 * math.pi * F_in

prec = 25
sp_t = []
sp_y_in = []
sp_y_out = []

for i in range(prec * round(k_period * Fd / F_in)):
    t = i / Fd / prec
    y_in = math.sin(w * t)

    sp_t.append(t * 1000)
    sp_y_in.append(y_in)

    if (i % prec) == 0:
        z14 = z13
        z13 = z12
        z12 = z11
        z11 = temp1
        temp1 = y_in - b11 * z11 - b12 * z12 - b13 * z13 - b14 * z14
        cascade1 = a10 * temp1 + a11 * z11 + a12 * z12 + a13 * z13 + a14 * z14

        z24 = z23
        z23 = z22
        z22 = z21
        z21 = temp2
        temp2 = cascade1 - b21 * z21 - b22 * z22 - b23 * z23 - b24 * z24
        cascade2 = a20 * temp2 + a21 * z21 + a22 * z22 + a23 * z23 + a24 * z24

        z34 = z33
        z33 = z32
        z32 = z31
        z31 = temp3
        temp3 = cascade2 - b31 * z31 - b32 * z32 - b33 * z33 - b34 * z34
        cascade3 = a30 * temp3 + a31 * z31 + a32 * z32 + a33 * z33 + a34 * z34

        z44 = z43
        z43 = z42
        z42 = z41
        z41 = temp4
        temp4 = cascade3 - b41 * z41 - b42 * z42 - b43 * z43 - b44 * z44
        cascade4 = a40 * temp4 + a41 * z41 + a42 * z42 + a43 * z43 + a44 * z44

        y_out = cascade4
        sp_y_out.append(y_out)

    else:
        sp_y_out.append(y_out)

    if (max_in <= y_in) and (i > prec * round((k_period - 1) * Fd / F_in)):
        max_in = y_in
    if (max_out <= y_out) and (i > prec * round((k_period - 1) * Fd / F_in)):
        max_out = y_out

dB = (20 * math.log10(max_out / max_in))
print('dB: ', str(dB))

stl.use('ggplot')
plt.plot(sp_t, sp_y_in, 'b')
plt.plot(sp_t, sp_y_out, 'c')
plt.show()
