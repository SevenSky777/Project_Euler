def factorial(x: int) -> int:
    total = 1
    for i in range(0, x):
        total = total * (i + 1)
    return total


def sfd(x: int) -> int:
    """Sum of the factorials of the digits."""
    total = 0
    while x > 0:
        total = total + factorial(x % 10)
        x = x // 10
    return total


def sumdigit(x: int) -> int:
    """Sum of the digits."""
    total = 0
    while x > 0:
        total = total + x % 10
        x = x // 10
    return total


my_list = []

for i in range(3, 9999999):
    if i == sfd(i):
        my_list = my_list + [i]

print(my_list)
