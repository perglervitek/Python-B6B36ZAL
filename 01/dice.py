import random

numbers = {
    1:'''
     *
     ''',
    2:'''
    *
     
      *
     ''',
    3:'''
    *
     *
      *
     ''',
    4:'''
    * *
     
    * *
     ''',
    5:'''
    * *
     *
    * *
     ''',
    6:'''
    * *
    * *
    * *
     '''
}

class Dice:
    def roll(self):
        rolled_num = random.randint(1, 6)
        print(numbers.get(rolled_num, "Error"))
        return rolled_num


dice = Dice()
number_rolled = dice.roll()
