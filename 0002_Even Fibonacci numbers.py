sum = 0
a, b = 1, 1

while b < 4000000:
    if b % 2 == 0:
        sum = sum+b
    b = a+b
    a = b-a

print(sum)
