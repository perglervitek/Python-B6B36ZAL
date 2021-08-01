import string

#    Slovník, pořadí nemusí být garantované u starších verzí
def createBoard():
    board = {}
    for i in range(8):
        board[i] = {}
        for j in range(8):
            board[i][j] = getColor(i,j)
    return board

def getColor(n, m):
    if (n + m) % 2 == 0:
        return 'B'
    else:
        return 'W'

def getTile(tile):
    chars = string.ascii_uppercase[:8]
    n = tile[:1]
    m = int(tile[1:2])
    indexOfLetter = chars.find(n)
    board = createBoard()
    print(board[indexOfLetter][m-1])
    return tile

tile = input("Zadejte pole ve tvaru: A1,A5,B8: ")
getTile(tile)



# def euclid(num1, num2):
#     help = 0
#     while num2 != 0:
#         help = num2
#         num2 = num1 % num2
#         num1 = help
#     return num1

# num1 = int(input("Zadej první číslo: "))
# num2 = int(input("Zadej druhé číslo: "))


# print(euclid(num1, num2))

