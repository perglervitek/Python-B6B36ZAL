def gcd(u, w):
    if w != 0:
        gcd(w, u % w)
    return w

print(gcd(40902, 24140))