import time
start_time = time.time()


def isprime(my_int, prime_list):
    for i in prime_list:
        if i < int(my_int**(0.5)+1):
            if my_int % i == 0:
                return False
    return True


prime_list = [2]
cn = 1
i = 3
while cn != 10001:
    print(cn)
    if isprime(i, prime_list) == True:
        prime_list = prime_list + [i]
        cn += 1
    i = i+2

print(f'{cn}st : {prime_list[-1]}')
print(f'Execution time = {time.time()-start_time}')
