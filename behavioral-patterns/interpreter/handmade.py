from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


def lex(input):
    result = []

    i = 0
    while i < len(input):  # Check each character.
        if input[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif input[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif input[i] == "(":
            result.append(Token(Token.Type.LPAREN, "("))
        elif input[i] == ")":
            result.append(Token(Token.Type.RPAREN, ")"))
        else:  # must be a number
            digits = [input[i]]  # first digit
            for j in range(i + 1, len(input)):  # other digits
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1  # Increment to avoid repeat again in the main while loop.
                else:  # If no more digits, we have to managed all accumulated digits.
                    result.append(Token(Token.Type.INTEGER, "".join(digits)))
                    break
        i += 1

    return result


# ↑↑↑ lexing ↑↑↑

# ↓↓↓ parsing ↓↓↓


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryOperation()
    have_lhs = False  # Left part has been parsed or not.
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryOperation.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1 : j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j  # advance
        i += 1
    return result


def eval(input):
    tokens = lex(input)
    # Print each token to check they are correct.
    print(" ".join(map(str, tokens)))

    parsed = parse(tokens)
    print(f"{input} = {parsed.value}")


if __name__ == "__main__":
    eval("(13+4)-(12+1)")
    eval("1+(3-4)")

    # this won't work
    eval("1+2+(3-4)")
