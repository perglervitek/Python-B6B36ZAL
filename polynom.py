def polyEval(poly, x):
    res = 0.0
    for i in range(len(poly)):
        if poly[i] != 0:
            res += float(poly[i] * x**i)
    return res

def polySum(poly1, poly2):
    resPoly = []
    if len(poly1) >= len(poly2):
        for i in range(len(poly2)):
            resPoly.append(float(poly1[i] + poly2[i]))
        resPoly.extend(poly1[len(poly2):])
        for num in reversed(resPoly):
            if num == 0.0:
                resPoly = resPoly[:-1]
            else:
                break
    else: 
        for i in range(len(poly1)):
            resPoly.append(float(poly1[i] + poly2[i]))
        resPoly.extend(poly2[len(poly1):])
    return resPoly


def polyMultiply(poly1, poly2):
    resPoly = [0.0]
    resPoly = resPoly * (len(poly1) + len(poly2) - 1)
    for i in range((len(poly1))):
        for j in range((len(poly2))):
            resPoly[i+j] += float(poly1[i] * poly2[j])
    return resPoly