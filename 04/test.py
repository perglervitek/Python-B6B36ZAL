# psy = ['husky', 'pudl', 'buldok']
# cats = psy
# cats[0] = 'kocour'
# print(psy)

# def mojeFunkce(mujString, mujSeznam):
#   mujString = 'okurka'
#   mujSeznam[1] = 'krtek'
# ovoce = 'jablko'
# psy = ['husky', 'pudl', 'buldok']
# mojeFunkce(ovoce, psy)
# print(ovoce)
# print(psy)

# for i in range(1, min(a,b) +1):
#     if(a%i==0) and (b%i==0):
#         cislo = i
#     print(cislo)

def sum(min,max):
    tempSum = 0
    for i in range(min, max+1):
        tempSum += i
    return tempSum

def sum1(min, max):
    tempSum = 0
    while(min <= max):
        tempSum += min
        min += 1
    return tempSum

print(sum1(1,10))