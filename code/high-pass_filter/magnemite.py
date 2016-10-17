from math import *

fc = float(input('>>> fc (4.5 - 18):   '))
fs = float(input('>>> fs (0 - 2.2):    '))

fc_max = 18
print('fc_max:             ', fc_max)

print('=' * 77)

Fs = 2 * fc_max
print('Fs:                 ', Fs)

lambda_c = 2 * pi * fc / Fs
print('lambda_c:           ', lambda_c)

lambda_s = 2 * pi * fs / Fs
print('lambda_s:           ', lambda_s)

c = tan(lambda_c / 2)
print('c:                  ', c)

omega = tan(lambda_c / 2) / tan(lambda_s / 2)
print('omega:              ', omega)
