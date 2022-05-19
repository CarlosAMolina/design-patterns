class Event(list):
    """List of functions to run when an event happens."""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f"{name} needs a doctor at {address}")


if __name__ == "__main__":
    person = Person("Sherlock", "221B Baker St")

    # Add event subscription.
    person.falls_ill.append(call_doctor)

    # Append a function to the event.
    person.falls_ill.append(lambda name, addr: print(f"{name} is ill"))

    person.catch_a_cold()

    print()

    # You can remove subscriptions too.
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
