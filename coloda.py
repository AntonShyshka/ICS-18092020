import random 
 
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank
        
    def info_rank(self):
         return self.rank
 
    def __str__(self):
        return f'{self.rank} {self.suit}'
 
 
class Deck:
    
    def __init__(self, cards):
        self.cards = cards
 
    def deck_info(self):
        for card in self.cards:
            print(card)
 
    def mix_card(self):
        random.shuffle(self.cards)
 
    def one_card(self):
        if not self.cards:
            return 'no card'
        return random.choice(self.cards)
    
    def six_card(self):
        return [self.one_card() for _ in range(6)]
 
 
rank = ['Туз', 'Король','Дама','Валет','10','9','8','7','6',]
suit = ["червей","бубей","крестей","пик" ]
cards = [Card(s,r) for s in suit for r in rank] # возможно это в классе Deck нужно выполнить
 
 
deck = Deck(cards)
print('колода')
deck.deck_info()
deck.mix_card()
print()
print('перемешанная колода')
deck.deck_info()
print()
print('выдача одной карты')
print(deck.one_card())
print()
print('выдача 6 карт')
for card in deck.six_card():
    print(card)