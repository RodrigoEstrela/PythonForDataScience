class Calculator:
    """
    Calculator class
    addition, multiplication,
    subtraction, division
    vector with a scalar
    """
    def __init__(self, vector):
        """Constructor, initialize vector attribute"""
        self.vector = vector

    def __add__(self, other) -> None:
        """Addition method"""
        self.vector = [v + other for v in self.vector]
        print(self.vector)

    def __mul__(self, other) -> None:
        """Multiplication method"""
        self.vector = [v * other for v in self.vector]
        print(self.vector)

    def __sub__(self, other) -> None:
        """Subtraction method"""
        self.vector = [v - other for v in self.vector]
        print(self.vector)

    def __truediv__(self, other) -> None:
        """Division method"""
        if other == 0:
            print("Division by 0 is impossible!")
        else:
            self.vector = [v / other for v in self.vector]
            print(self.vector)
