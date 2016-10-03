import math

f_c = 5200
f_s = 11700
delta = 21

F_s = 3 * f_s
lambda_c = 2 * math.pi * f_c / F_s
print("Digital Frequency: ", lambda_c)  # цифровая частота

lambda_s = 2 * math.pi * f_s / F_s
print("Sampling Frequency: ", lambda_s)  # частота выборки

omega_c = math.tan(lambda_s/2) / math.tan(lambda_c/2)
print("Band Edge: ", omega_c)  # граница полосы затухания

# 20 * log10((( 2.914 ^ (2 * n)) ^ 1/2)) >= 21

c = 1 / (math.tan(lambda_c / 2))
print('C: ', c)
