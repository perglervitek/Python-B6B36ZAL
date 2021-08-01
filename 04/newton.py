def newton(num):
    a = num
    while (num != 3.0):
        num = 0.5*(num + (a/num))
        print(num)
    return num

# print(newton(9.0))

def primeNumber(num):
    if num <= 1:
        return False

    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

print(primeNumber(32326729))