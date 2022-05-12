class CreatureBad:
    """Incorrect class as is difficult to add more attributes
    because all other methods must be updated manually.
    """
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.agility + self.intelligence

    @property
    def max_stat(self):
        return max(self.strength, self.agility, self.intelligence)

    @property
    def average_stat(self):
        # Incorrect to use the number 3.0 because if we add more 
        # attributes and 3.0 is not modified, the result is wrong.
        return self.sum_of_stats / 3.0


class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]
        # This example uses one list but, if we group values
        # in different lists we could manage these groups for
        # easier calculations.

    @property
    def strength(self):
        return self.stats[self._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[self._agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stats[self._intelligence]

    @agility.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return float(sum(self.stats) / len(self.stats))


if __name__ == "__main__":
    creature_bad = CreatureBad()
    creature = Creature()
    print("Sum of stats")
    print(creature_bad.sum_of_stats)
    print(creature.sum_of_stats)
    print("Max stat")
    print(creature_bad.max_stat)
    print(creature.max_stat)
    print("Average stat")
    print(creature_bad.average_stat)
    print(creature.average_stat)

