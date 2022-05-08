import random
import string
import sys


class User:
    def __init__(self, name):
        self.name = name


class User2:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        # Work with indexes instead of strings.
        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


def random_string():
    """Simulate a name"""
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for x in range(8)])


if __name__ == "__main__":
    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    # Work with the class User.
    # Combine first and last names.
    # Total number of names storing them in: 10.000.
    users = []
    for first in first_names:
        for last in last_names:
            users.append(User(f"{first} {last}"))

    # Work with the class User2.
    u2 = User2("Jim Jones")
    u3 = User2("Frank Jones")
    print(u2.names)
    print(u3.names)
    print(User2.strings)

    users2 = []
    for first in first_names:
        for last in last_names:
            users2.append(User2(f"{first} {last}"))

    print("Number of strings with:")
    print(f"- User: {len(users)}") # 10.000.
    print(f"- User2: {len(User2.strings)}") # 203 strings. 10.000 indexes.
    print(f"- users2: {len(users2)}") # 10.000 indexes.

