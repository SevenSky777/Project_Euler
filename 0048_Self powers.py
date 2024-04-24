import time

start_time = time.time()


def SelfPower(n: int) -> int:
    np = 1
    i = 1
    while i <= n:
        np = np * n
        i += 1
        if np > 10_000_000_000:
            np %= 10_000_000_000
    return np


sum = 0
for i in range(1, 1001):
    sum += SelfPower(i)
    if sum > 10_000_000_000:
        sum %= 10_000_000_000
print(sum)

print(f'Execution time = {time.time()-start_time}')
