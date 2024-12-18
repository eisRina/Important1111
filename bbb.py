from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    @abstractmethod
    def build(self) -> Any:
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_cost(self, cost):
        pass

    @abstractmethod
    def set_card_type(self, card_type):
        pass

    @abstractmethod
    def set_card_subtype(self, card_subtype):
        pass

    @abstractmethod
    def set_power(self, power):
        pass

    @abstractmethod
    def set_health(self, health):
        pass

class CardBuilder(Builder):

    def __init__(self):
        self.empty_card = Card()

    def build(self) -> Any:
        builded_card = self.empty_card
        self.empty_card = Card()
        return builded_card

    def set_name(self, name):
        self.empty_card.name = name
        return self

    def set_cost(self, cost):
        self.empty_card.cost = cost
        return self

    def set_card_type(self, card_type):
        self.empty_card.card_type = card_type
        return self

    def set_card_subtype(self, card_subtype):
        self.empty_card.card_subtype = card_subtype
        return self

    def set_power(self, power):
        self.empty_card.power = power
        return self

    def set_health(self, health):
        self.empty_card.health = health
        return self