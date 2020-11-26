def f(x):
    return x  # some function here


def ternary(L, R, f):
    if R - L < 1e-12:
        if f(L) > f(R):
            return L
        return R
    p1 = f(L + (R - L) / 3)
    p2 = f(L + 2 * (R - L) / 3)
    if p1 > p2:
        return ternary(L, L + 2 * (R - L) / 3, f)
    else:
        return ternary(L + (R - L) / 3, R, f)
