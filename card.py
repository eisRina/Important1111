'''class Card:
    __cost_dict = {
        'W': 'Белая',
        'U': 'Синяя',
        'B': 'Чёрная',
        'R': 'Красная',
        'G': 'Зелёная'
    }

    def __init__(self, name='Фея-Наставница', cost='W', card_type='Существо', card_subtype='', hp='1', strght='1'):
        self.name = name
        self.cost = cost
        self.card_type = card_type
        self.card_subtype = card_subtype
        self.health = hp
        self.strenght = strght

    def __define_cost(self, cost):
        # Белая - W, Синяя - U, Чёрная - B, Красная - R, Зелёная - G
        # вывести вместо букв цены её полное название
        # WU -> Белая, Синяя
        # 2W -> 2 любых, Белая

        result = ''
        for c in cost:
            if c in self.__cost_dict:
                result += self.__cost_dict[c] + ' , '
                continue
            result += f'{c} любая, '

        return result.strip()

    def __str__(self) -> str:
        return f'Я - {self.name}, стою {self.__define_cost(self.cost)} {self.card_type} – {self.card_subtype}, сила: {self.strenght}, выносливость: {self.health}'
    '''
    
def converted_mana_cost (f):
    def pack(card):
        mana_value = 0
        price = f(card)
        for c in price:
            if not c.isalpha():
                mana_value += int(c)
                continue
            mana_value += 1
        return str(mana_value)
    return pack
    
class Card:

    def __init__(self):
        self.name = ''
        self.cost = '3W'
        self.card_type = ''
        self.card_subtype = ''
        self.isTaped = False
        self.isPermanent = True
        
    

    def __str__(self) -> str:
        return f'Card \'{self.name}\' mana_cost = {self.cost} power = {self.power}'
    
    @converted_mana_cost
    def mana_cost(self) -> int:
          return self.cost
      
    def tap(self):
        self.isTaped = not self.isTaped
        

card = Card()
print(card.mana_cost())


class CreatureCard(Card):
    def __init__(self):
        super().__init__
        power = 1
        health = 1
        
class InstantCard(Card):
    pass
class SorceryCard(Card):
    pass
class ArtifactCard(Card):
    pass
class EnchantmentCard(Card):
    pass