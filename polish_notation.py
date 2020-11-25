s = input().split()
a = []
flag = 0
for i in range(len(s)):
    if s[i] not in "+-*/":
        a.append(float(s[i]))
    else:
        b = a.pop()
        c = a.pop()
        if s[i] == "+":
            t = c + b
        elif s[i] == "-":
            t = c - b
        elif s[i] == "*":
            t = c * b
        else:
            if b != 0:
                t = c / b
            else:
                if c >= 0:
                    t = 10 ** 6
                else:
                    t = -(10 ** 6)
        if t > 10 ** 6:
            t = 10 ** 6
        elif t < -(10 ** 6):
            t = -(10 ** 6)
        elif abs(t) < 10 ** -6:
            t = 0
        a.append(t)
if a[0] > 10 ** 6:
    a[0] = 10 ** 6
elif a[0] < -(10 ** 6):
    a[0] = -(10 ** 6)
elif abs(a[0]) < 10 ** -6:
    a[0] = 0
print("%.6f" % a[0])
