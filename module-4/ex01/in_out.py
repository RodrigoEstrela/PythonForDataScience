def square(x: int | float) -> int | float:
    """Returns the input number squared"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of the input number by itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an object
    When called returns the result of the arguments calculation
    """
    count = 0

    def inner() -> float:
        """Inner function"""
        nonlocal count
        result = x
        count += 1
        for _ in range(count):
            result = function(result)
        return result

    return inner
