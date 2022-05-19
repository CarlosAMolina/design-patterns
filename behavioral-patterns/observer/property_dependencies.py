class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    """The can_vote property depends on the age property."""
    @property
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    #@age.setter
    #def age(self, value):
    #  if self._age == value:
    #    return
    #  self._age = value
    #  self.property_changed('age', value)
    #  self.property_changed('can_vote', value) # Incorrect, because 
    #  # it will be always be called and should only
    #  # be called when the age is >= 18.
    #  # The correct way is to only perform the notification if the 
    #  # value should change.

    @age.setter
    def age(self, value):
        if self._age == value:
            return

        # This solution works for few properties, it does not
        # escale correctly.
        old_can_vote = self.can_vote

        self._age = value
        self.property_changed("age", value)

        if old_can_vote != self.can_vote:
            self.property_changed("can_vote", self.can_vote)


if __name__ == "__main__":

    def person_changed(name, value):
        if name == "can_vote":
            print(f"Voting status changed to {value}")

    p = Person()
    p.property_changed.append(person_changed)

    for age in range(16, 21):
        print(f"Changing age to {age}")
        p.age = age
