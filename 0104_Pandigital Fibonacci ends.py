import time
start_time = time.time()

PAND = set('123456789')
TAIL = 1_000_000_000
HEAD = 1_000_000_000


def pandigital(x):
    return set(x) == PAND


c = 2
a = b = 1
aa = bb = 1
while True:
    a = a+b
    b = a-b
    a %= TAIL
    b %= TAIL

    aa = aa+bb
    bb = aa-bb
    if (aa > HEAD and bb > HEAD):
        aa /= 10
        bb /= 10

    c += 1
    if (pandigital(str(a)) and pandigital(str(aa)[0:9])):
        print(c)
        break

assert (c == 329468)
print(f'Execution time = {time.time()-start_time}')
