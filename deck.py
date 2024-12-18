
from card import Card

class Deck:

    def __init__(self, card_list: list[Card] | None = None):
        self.card_list = card_list or []

    def __str__(self) -> str:
        return str([str(card) for card in self.card_list])

    def deck_sorting_mana_value(self):
        self.card_list.sort(key=lambda card: Card.mana_value_define(card))
          