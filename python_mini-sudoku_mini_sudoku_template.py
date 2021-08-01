class Sudoku:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for r in self.board:
          for c in r:
              print(c, end =" ")
          print()

    def is_allowed(self, row, col, value):
      row = row - 1
      col = col - 1
      rowAllowed = True
      colAllowed = True
      quadrantAllowed = True

      for n in (self.board[row]):
        if n == value:
          rowAllowed = False
          break
      
      
      for n in range(len(self.board)):
        if self.board[n][col] == value:
          colAllowed = False

      if value in self.check_quadrant(row, col):
        quadrantAllowed = False
        
      if quadrantAllowed and rowAllowed and colAllowed:
        return True
      else:
        return False

    def check_quadrant(self, row, col):
        board = self.board.copy()
        quadrantNums = []
        if row <= 1:
          quadrantNums.append(board[0])
          quadrantNums.append(board[1])
        else:
          quadrantNums.append(board[2])
          quadrantNums.append(board[3])
        
        if col >= 1:
          for n in quadrantNums:
            del n[2:]
        else:
          for n in quadrantNums:
            del n[:2]
        
        nums = []
        for rows in quadrantNums:
            for column in rows:
                nums.append(column)
        
        return(nums)

    # helper method - is sudoku solved?
    def is_filled(self):
        pass

    # alternative to the above method - find the first empty cell if exists
    # useful for automatic solver
    def find_first_empty_cell(self):
      allNums = []
      for row in self.board:
        for col in row:
          allNums.append(col)
      if 0 in allNums:
        return True
      else: 
        return False
            

    def get_dead_cell(self):
      return True
        # for r in self.board:
        #   for c in r:
        #     if c ==
        #     print(c, end =" ")

    def add_player_number(self):
        nums = (input("Zadej druhé radek, sloupec a cislo k zapsani, oddelene mezerou, napr. 2 4 3: "))
        numsArr = nums.split()
        row = int(numsArr[0])
        col = int(numsArr[1])
        value = int(numsArr[2])
        print(self.board[row -1 ][col -1])
        #zkontrolovat input
        if(self.is_allowed(row, col, value)):
          self.board[row - 1][col - 1] = value
        else:
          print('Tato hodnota nelze zapsat')
          

    def play(self):
        while self.find_first_empty_cell():
          self.print_board()
          self.add_player_number()


    def solve_board(self):
        pass


if __name__ == "__main__":

    # Test 1. Let the user solve an "easy" sudoku
    sudoku1 = Sudoku([[0, 2, 1, 0], [0, 4, 2, 3], [2, 3, 4, 0], [4, 0, 3, 2]])
    sudoku1.play()

    # Test 2. Let the user solve a "very hard" sudoku
    sudoku2 = Sudoku([[0, 0, 4, 0], [3, 0, 0, 0], [0, 0, 3, 1], [0, 3, 0, 4]])
    sudoku2.play()

    # Test 3. Automatically solves a "very hard" sudoku
    sudoku3 = Sudoku([[0, 0, 4, 0], [3, 0, 0, 0], [0, 0, 3, 1], [0, 3, 0, 4]])
    sudoku3.solve_board()
    sudoku3.play()
    # sudoku3.print_board()
    # sudoku3.add_player_number()
