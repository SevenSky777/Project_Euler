with open('./13_Large_sum.txt', 'r') as f:
    f_read = f.readlines()
    sum = 0
    for i in f_read:
        sum = sum + int(i)/1e51

print(int(sum*1e9))
