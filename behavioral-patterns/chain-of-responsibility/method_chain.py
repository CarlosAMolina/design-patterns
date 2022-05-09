class Creature:
    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack = attack
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        """This method propagates de chain of responsibility principle."""
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you!")
        # I the parent `handle()` is not called, the chain is stopped.


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        # To apply the chain of responsibility principle, the parent
        # `handle()` must be called.
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.defense += 1
        super().handle()


if __name__ == "__main__":
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)  # Value 1/1.

    root.add_modifier(DoubleAttackModifier(goblin))  # Future value 2/1.
    root.add_modifier(
        NoBonusesModifier(goblin)
    )  # The folloging modifiers have no effect.
    root.add_modifier(DoubleAttackModifier(goblin))  # No effect.
    root.add_modifier(IncreaseDefenseModifier(goblin))  # No effect.

    root.handle()  # Apply modifiers.
    print(goblin)  # 2/1
