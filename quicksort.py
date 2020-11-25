from random import randrange


def qsort(a):
    if len(a) <= 1:
        return a
    median = a[randrange(0, len(a))]
    less = []
    equal = []
    greater = []
    for x in a:
        if x < median:
            less.append(x)
        elif x > median:
            greater.append(x)
        else:
            equal.append(x)
    return qsort(less) + equal + qsort(greater)


arr = list(map(int, input().split()))
print(*qsort(arr))
