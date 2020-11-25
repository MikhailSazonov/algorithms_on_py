def binpoisk(a, l, r, m):
    if r - l == 1:
        if a[l] == m:
            return l
        else:
            return -1
    if m < a[(l + r) // 2]:
        ans = binpoisk(a, l, (l + r) // 2, m)
    else:
        ans = binpoisk(a, (l + r) // 2, r, m)
    return ans


print("Enter sorted list")
arr = list(map(int, input().split()))
print("What number to search?")
num = int(input())
print("The position is", binpoisk(arr, 0, len(arr), num))
