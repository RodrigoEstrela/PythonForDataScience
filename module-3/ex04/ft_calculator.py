class Calculator:
    """
    Calculator to operate on two vectors
    Dot product
    Addition
    Subtraction
    """
    @staticmethod
    def dot_product(v1: list[float], v2: list[float]) -> None:
        """Prints dot product between two vectors"""
        result = 0
        for a in range(len(v1)):
            result += v1[a] * v2[a]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Prints the resulting vector from the addition of two vectors"""
        result = [float(v1[a] + v2[a]) for a in range(len(v1))]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Prints the resulting vector from the subtraction of two vectors"""
        result = [float(v1[a] - v2[a]) for a in range(len(v1))]
        print(f"Sous Vector is: {result}")
