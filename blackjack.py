#BlackJack
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        suits = ["Heart", "Diamonds", "Clover", "Spade"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
        
    def dealCard(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.cantAces = 0
        
    def addCard(self, card):
        self.cards.append(card)
        
        if card.rank == 'Ace':
            self.cantAces += 1
        self.calculateValue()
            
    def calculateValue(self):
        self.value = sum([self.getValue(card) for card in self.cards])
        
        if self.value > 21 and self.cantAces:
            self.value -= 10
            self.cantAces -= 1
        
    def getValue(self, card):
        if card.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif card.rank == 'Ace':
            return 11
        else:
            return int(card.rank)

class Game:
    def__init__
