import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


# Incorrect. Example 1
address = Address("123 London Road", "London", "UK")
john = Person("John", address)
jane = john
jane.name = "Jane" # John's data is modified too
print("Incorrect. Example 1")
print(john)
print(jane)

# Incorrect. Example 2
address = Address("123 London Road", "London", "UK")
john = Person("John", address)
jane = Person("Jane", address)
jane.address.city = "Cuenca" # John's data is modified too
print("Incorrect. Example 2")
print(john)
print(jane)

# Correct
john = Person("John", Address("123 London Road", "London", "UK"))
jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "124 New Address"
print("Correct")
print(john)
print(jane)
