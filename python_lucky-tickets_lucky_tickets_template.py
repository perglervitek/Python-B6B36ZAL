# Calculates the probability of 'lucky' public ticket number occurence
# Tickets with a 6 digit serial number are considered 'lucky'
# when the sum of first and last 3 digits of the serial number are equal  

class LuckyNumberCounter:

  def __init__(self, digitCount):
    if digitCount % 2 == 0:
      self.digitCount = digitCount
    else:
      self.digitCount = digitCount - 1
      print("Počet čísel musí být sudý.")
    self.numberCount = 10 ** digitCount

  # další funkce podle vlastního uvážení

  def isLuckyNumber(self, number):
    if number >= 0 and number <= 999999:
      numArr = [int (x) for x in str(number)]
      if len(numArr) % 2 == 0:
        firstHalf = 0
        for i in range(len(numArr) // 2):
          firstHalf += numArr[i]
        secondHalf = 0
        for i in range(len(numArr) // 2, len(numArr)):
          secondHalf += numArr[i]
        if secondHalf == firstHalf:
          return True
        else: 
          return
      else:
        return False
    else:
      raise ValueError("Špatně zadaná hodnota")
    pass

  def getLuckyNumberCount(self):
    luckyCount = 0
    for number in range(0, self.numberCount):
      if self.isLuckyNumber(number):
        luckyCount += 1
    return luckyCount


# digits = 5
# lnc = LuckyNumberCounter(digits)
# print(lnc.isLuckyNumber(55139))

# luckyNumbersTotal = lnc.getLuckyNumberCount()
# luckyNumbersProbab = luckyNumbersTotal / lnc.numberCount

# print(lnc.digitCount, "digit lucky numbers count:", luckyNumbersTotal)
# print("Probability of getting a lucky number is:", luckyNumbersProbab, end=" ")
# print("so chance is 1 in", 1 / luckyNumbersProbab)


#55252

# def x(a,b):
#     n=0
#     for i in range(a,b+1):
#         if sum(map(int,str(i//1000)))==sum(map(int,str(i%1000))):n+=1
#     print(n)

# print(x(0,999999))