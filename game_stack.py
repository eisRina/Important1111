from card import Card

class GameStack:

    def __init__(self, stack: list[Card] | None = None):
        self.__stack = stack or []
    
    def push_for_hold(self, card):
        self.__stack.append(card)

    def pop_for_raise(self) -> Card:
        return self.__stack.pop() 