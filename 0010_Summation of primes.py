import time
start_time = time.time()


def isprime(my_int, prime_list):
    for i in prime_list:
        if i < int(my_int**(0.5)+1):
            if my_int % i == 0:
                return False
    return True


prime_list = [2]
sum = 2
for i in range(3, 2_00000, 2):
    if isprime(i, prime_list) == True:
        prime_list = prime_list + [i]
        sum += i

print(sum)
# print(prime_list)

print(f'Execution time = {time.time()-start_time}')
