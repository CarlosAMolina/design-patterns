import random


class Database:
    initialized = False

    def __init__(self):
        self.id = random.randint(1, 101)
        print("Generated an ID of", self.id)

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == "__main__":
    print("Init db 1")
    d1 = Database()
    print("Database memory IDs:", id(d1))
    print("Init db 2")
    d2 = Database()
    print("Database memory IDs:", id(d2))

    print("Both dbs have been initialized")
    print("Databases IDs:", d1.id, d2.id)
    print("Databases memory IDs:", id(d1), id(d2))
    print("The databases are the same object:")
    print(d1 == d2)
