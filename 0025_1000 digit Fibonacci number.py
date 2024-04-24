import math

a, b = 1, 1
cn = 2
digits = 1

while digits != 1000:
    cn += 1
    b = a+b
    a = b-a
    digits = int(math.log10(b))+1

print(cn)
