import math


def is_prime(N):
    for i in range(2, math.ceil(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True


Num = int(input())
ans = is_prime(Num)
if ans:
    print(Num, "is prime")
else:
    print(Num, "is not prime")
