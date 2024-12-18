from card import Card
from Player import Player

class Land(Card):
    def __init__(self, mana_produce):
        super().__init__()
        self.mana_produce = mana_produce 
    def tap(self,player):
        if not self.isTaped:
            super().tap()
            player.mana_pool.append(self.mana_produce)
    
    def check_mana(self,player,card):
        pool_mana = player.mana_pool[:]
        cost_mana = card.mana_cost()
        for a in cost_mana():
            if a.isdigit():
                for _ in range(int(a)):
                    if pool_mana:
                        pool_mana.pop(0)
                    else:
                        print("Мало маны")
                        return False
            else:
                if a in pool_mana:
                    pool_mana.remove(a)
                else:
                    print("Мало маны")
                    return False
        
        player.mana_pool = pool_mana
        print (f'{player.name} разыграл {card.name}')
        return True
    
                    
                    
                

                
                
                
        
        
        