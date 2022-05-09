# Required parts:
# - Event broker. It needs an event, we will generate the event thanks to the observer pattern.
# - Observer. Required by the event broker.
# - CQS (command-query separation).

from abc import ABC
from enum import Enum


class Event(list):
    """A list of functions that I can call."""
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value  # bidirectional
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self):
        """
        Game is the broker. It takes care of the chain of
        responsability. The broker is game as every creature is
        part of the game.
        """
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class Creature:
    def __init__(self, game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle) # We need to handle de queries event.

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Object removal from chain."""
        self.game.queries.remove(self.handle)


# We use the event broker approach, this class inherits from CreatureModifier.
class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQuery.DEFENSE
        ):
            query.value += 3


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print(goblin) # Value of 2/2

    # As soon as the modifiers get out of scope, their effects end.
    with DoubleAttackModifier(game, goblin):
        print(goblin) # Value of 4/2.
        with IncreaseDefenseModifier(game, goblin):
            print(goblin) # Value of 4/5.

    print(goblin) # Value reset to 2/2.
