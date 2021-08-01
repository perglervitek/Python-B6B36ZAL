def getNumberOfStones(min, max):
    n = int(input("Enter number of stones in range ["
                  + str(min)+ "," + str(max) + "]: "))
    if n < min: return min
    if n > max: return max
    return n


def humanTurn(n):
    r = ""
    while (r != "1" and r != "2" and r!= "3"):
        r = input("Number of stones is "
            + str(n) +
            ". How many stones you will take: ")
    return int(r)



def machineTurn(n):
    r = (n-1) % 4
    if r == 0: r = 1
    print("Number of stones is "
          + str(n) + ". I take: " + str(r))
    return r


MIN_S = 15
MAX_S = 35
machine = False

whoWillStart = input("Who will start?: ")
if(whoWillStart == "PC"):
    machine = True

numberOfStones = getNumberOfStones(MIN_S, MAX_S)
while (numberOfStones > 0):
    if machine:
        numberOfStones -= machineTurn(numberOfStones)
    else:
        numberOfStones -= humanTurn(numberOfStones)
    machine = not machine
if machine: print("Machine wins!")
else: print("Human wins!")
