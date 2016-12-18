import math
import matplotlib.pyplot as plt
import matplotlib.style as stl

max_in = 0
max_out = 0

# -----//-----
z01 = 0
z02 = 0
z03 = 0
z04 = 0

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

# -----//-----
temp0 = 0
temp1 = 0
temp2 = 0
temp3 = 0

cascade0 = 0
cascade1 = 0
cascade2 = 0
cascade3 = 0

# -----//-----
a00 =  0.0175693
a01 =  0
a02 = -0.0351387
a03 =  0
a04 =  0.0175693

a10 =  0.016085
a11 =  0
a12 = -0.03217
a13 =  0
a14 =  0.016085

a20 =  0.0151081
a21 =  0
a22 = -0.0302162
a23 =  0
a24 =  0.0151081

a30 =  0.0146273
a31 =  0
a32 =  -0.0292546
a33 =  0
a34 =  0.0146273

# -----//-----
b00 =  1
b01 = -3.76806
b02 =  5.44044
b03 = -3.57152
b04 =  0.900116

b10 =  1
b11 = -3.61596
b12 =  4.9808
b13 = -3.10354
b14 =  0.739586

b20 =  1
b21 = -3.51586
b22 =  4.6783
b23 = -2.79544
b24 =  0.633933

b30 =  1
b31 = -3.46659
b32 =  4.52942
b33 = -2.64395
b34 =  0.581937

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
        z04 = z03
        z03 = z02
        z02 = z01 
        z01 = temp0
        temp0 = y_in - b01 * z01 - b02 * z02 - b03 * z03 - b04 * z04
        cascade0 = a00 * temp0 + a01 * z01 + a02 * z02 + a03 * z03 + a04 * z04

        z14 = z13
        z13 = z12
        z12 = z11
        z11 = temp2
        temp1 = cascade0 - b11 * z11 - b12 * z12 - b13 * z13 - b14 * z14
        cascade2 = a10 * temp1 + a11 * z11 + a12 * z12 + a13 * z13 + a14 * z14

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

        y_out = cascade3
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
