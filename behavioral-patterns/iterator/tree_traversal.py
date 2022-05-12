class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:
    def __init__(self, root):
        """
        - current: the current element
        """
        self.root = self.current = root
        self.yielded_start = False
        # Move to the most left element.
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        # Call:
        # - 1º: left
        # - 2º: middle
        # - 3º: right
        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


# Implement the iterator in a better way.
# With `yield` the code is more understandable.
def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == "__main__":
    #   1
    #  / \
    # 2   3

    # in-order: 213
    # preorder: 123
    # postorder: 231

    root = Node(1, Node(2), Node(3))

    it = iter(root)

    # Example, how to use the iterator
    print([next(it).value for x in range(3)]) # [2, 1, 3]

    # Use the iterator implicitly.
    for x in root:
        print(x.value)

    # Work with the better implementation.
    for y in traverse_in_order(root):
        print(y.value)
