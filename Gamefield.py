from game_stack import GameStack
from card import Card

class Gamefield:
    
    def __init__(self):
        self.players_hand = {}
        self.playing_area = {}
        
    def return_card_hands(self,player,card):
        if player not in self.players_hand:
            self.players_hand[player] = []
        self.players_hand[player].append(card)
    def addition_card_gamefield (self,player,card):
        if player not in self.playing_area :
            self.playing_area[player] = GameStack()
        if card.card_type == 'Существо':
            print(f'{player.name} разыграл {card.name} ')
        else:
            self.playing_area[player].push_for_hold(card)
            print(f'{player.name} добавил в stack {card.name}')
    def play_card(self,player):
        if player in self.playing_area and len(self.playing_area[player]._stack) > 0:
            cArDDD = self.playing_area[player].pop_for_raise()
            print(f'{player.name} разыграл {cArDDD}')
            return cArDDD      
        else:
            print(f'у {player.name} нет карты в stack') 
            return None
            
        
    def end_turn(self,player):
        player.mana_pool.clear()
        print (f'{player} завершил ход и мана = 0')
        
    