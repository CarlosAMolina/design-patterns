from abc import ABC


class Expression(ABC):
    """Required to allow use print as `e.print(buffer)`."""

    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        """Will fail silently on a missing case.
        The name reflective is because checking the
        type is called a reflection operation in some
        languages.
        """
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(e.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(")")

    # Allow to use print as `e.print(buffer)`
    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


# Still breaks OCP because new types require M×N modifications.
# For example, if a SubstracExpression is added, the ExpressionPrinter should be modified.

if __name__ == "__main__":
    # represents 1+(2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    buffer = []

    # ExpressionPrinter.print(e, buffer)

    # IDE might complain here
    e.print(buffer)

    print("".join(buffer))
