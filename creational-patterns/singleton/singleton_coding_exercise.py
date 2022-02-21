# Quiz solution

# Since implementing a singleton is easy, you have a different challenge: write a function called `is_singleton()`. This method takes a factory method that returns an object and it's up to you to determine whether or not that object is a singleton instance.

objects = []
def is_singleton(factory):
    objects.append(factory())
    if len(objects) == 1:
        return True
    return id(objects[-1]) == id(objects[-2])
