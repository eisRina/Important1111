
from card import Card
from Player import Player
from deck import Deck
from Gamefield import Gamefield
import random
from game_stack import GameStack

def uploading_file_card(filename : str) -> Deck:
    listC = []
    with open(filename , 'r' , encoding= 'utf-8') as file:
        #next(file)
        for i in file:
            if i.startswith("#") or not i.strip():
                continue
            name, cost, card_type, card_subtype, power, health = [x.strip("'") for x in i.strip().split(';')]
            card = Card()
            card.name = name
            card.cost = cost
            card.card_type = card_type
            card.card_subtype = card_subtype
            card.power = int(power)
            card.health = int(health)
            listC.append(card)
    return Deck(listC)


#Шаг 1: Игрок вводит своё имя
#Шаг 2: Игроку даётся колода карт (загружается из файла)
#Шаг 3: Колода карт перемешивается
   
def start_the_game():
    name = input('Введите имя:' )
    card_deck = uploading_file_card('my_cards.txt')  
    playerr = Player(name,card_deck)
    print (f'{name} получил {len(playerr.deck.card_list)}')
    
    size_deck = random.randint(10,60)
    playerr.deck.card_list = random.sample(playerr.deck.card_list, min(size_deck, len(playerr.deck.card_list)))
    print (f'Ваша колода состоит из данного кол карт: {len(playerr.deck.card_list)}')
    
    random.shuffle(playerr.deck.card_list)
    print('Карты перемешаны')
    
    gamee_stackk = Gamefield()
    players_hand_size = min(7,len(playerr.deck.card_list))
    
    for i in range(players_hand_size):
        a = playerr.deck.card_list.pop()
        gamee_stackk.return_card_hands(playerr,a)
        
start_the_game()
    
    
    

    
            
                
    


