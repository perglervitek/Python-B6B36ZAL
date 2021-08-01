import random

class Dealer:
  def __init__(self):
    self.deck = [
      '♥A', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
      '♦A', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
      '♣A', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
      '♠A', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K'
    ]
    self.players = []
    self.game = False

  def shuffle(self):
    for i in range(len(self.deck)):
      randomNumber = random.uniform(0, len(self.deck))
      self.deck[i], self.deck[int(randomNumber)] = self.deck[int(randomNumber)], self.deck[i]

  def deal(self, n):
    cardStack = []
    if len(self.deck) < n and n != 0:
      n = len(self.deck)
    if n != 0:
      for i in range(n):
        cardStack.append(self.deck.pop(0))
    return cardStack

  def addPlayer(self, player):
    self.players.append(player)

  def removePlayer(self, player):
    playerNum = int()
    for picked, index in enumerate(self.players):
      if picked == player:
        playerNum = index
    self.players.pop(playerNum)

  def startRound(self):
    self.game = True
    playingPlayers = []
    for player in self.players:
      playingPlayers.append(player)

    for player in playingPlayers:
      player.hand.append(self.deck.pop(0))

    while self.game == True:
      self.game = False
      for index, player in enumerate(playingPlayers):
        if player is not None:
          numberOf = 0
          for cardNum in player.hand:
            print(cardNum)
            if cardNum != []:
              number = 0
              if cardNum[1:] == "A":
                number = 11
              elif cardNum[1:] == "J" or cardNum[1:] == "Q" or cardNum[1:] == "K":
                number == 1
              else:
                number = int(cardNum[1:])
              numberOf += number
          if numberOf > 21:
            playingPlayers[index] = None
          else:
            card = input(f"{ player.name } Chcete líznout další kartu? A/N:     ")
            if card == "A":
              self.players[index].hand.append(self.deck.pop(0))
            else:
              playingPlayers[index] = None

      for player in playingPlayers:
        if self.game is True:
          break
        if player is not None:
          self.game = True

      self.announceWinner()

  def announceWinner(self):
    winners = {}
    for player in self.players:
      numberOf = 0
      for cardNum in player.hand:
        print(cardNum)
        if cardNum != []:
          number = 0
          if cardNum[1:] == "A":
            number = 11
          elif cardNum[1:] == "J" or cardNum[1:] == "Q" or cardNum[1:] == "K":
            number == 1
          else:
           number = int(cardNum[1:])
          numberOf += number
      winners[player.name] = [numberOf, 21-numberOf]
    
    sortedWinners = []
    for winner in winners:
      if len(sortedWinners) == 0:
        
      print(winners[winner][1])

        

class Player:
  def __init__(self, name, strategy):
    self.name = name
    self.strategy = strategy
    self.hand = []

  def getHandValue(self):
    pass

  def acceptCard(self, cards):
    pass

  def needsCard(self):
    pass

# TEST DEAL

dealer = Dealer()
dealer.shuffle()
myHand = dealer.deal(5)
print(myHand)
dealer.shuffle()

myHand = dealer.deal(3)
print(myHand)

# # TEST GAME

newDealer = Dealer()
player1 = Player('Čeněk Člověčí', 'Human')
player2 = Player('Vilda Vopatrný', 'Cautious')
player3 = Player('Olda Odvážný','Bold')
newDealer.addPlayer(player1)
newDealer.addPlayer(player2)
newDealer.addPlayer(player3)

newDealer.startRound()
newDealer.shuffle()
