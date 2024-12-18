from deck import Deck


class Account:
    def __init__(self, username : str, password: str, decks : list[Deck]= None):
        self.username = username
        self.password = password
        self.decks = decks if decks is not None else []
        
        