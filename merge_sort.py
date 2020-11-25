def merge(a):
    if len(a) == 1:
        return a
    t = merge_sort(merge(a[:(len(a) + 1) // 2]), merge(a[(len(a) + 1) // 2:]))
    return t


def merge_sort(b, c):
    d = []
    b_head = 0
    c_head = 0
    while b_head < len(b) and c_head < len(c):
        while b_head < len(b) and b[b_head] < c[c_head]:
            d.append(b[b_head])
            b_head += 1
        d.append(c[c_head])
        c_head += 1
    if b_head < len(b):
        d.extend(b[b_head:])
    if c_head < len(c):
        d.extend(c[c_head:])
    return d


q = list(map(int, input().split()))
print(*merge(q))
