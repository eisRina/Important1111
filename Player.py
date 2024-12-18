from deck import Deck

class Player:
    def __init__(self,name,deck = None):
        self.name = name
        self.deck = deck if deck is not None else Deck()
        self.health_points = 20
        #self.deck = None
        self.mana_pool = []
        
    def __str__(self):
        return f'Игрок - {self.name} , Колода {self.deck}'
    