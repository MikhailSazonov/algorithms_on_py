s = input().split()
a = []
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
                print("Unknown request")
        a.append(t)
print("%.6f" % a[0])
