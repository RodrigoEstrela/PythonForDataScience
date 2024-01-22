import math


def std_dev(nums):
    """Calculates the standard deviation"""
    m = sum(nums) / len(nums)
    return math.sqrt(sum((x - m) ** 2 for x in nums) / len(nums))


def variance(nums):
    """Calculates the variance"""
    m = sum(nums) / len(nums)
    return sum((x - m) ** 2 for x in nums) / len(nums)


def ft_statistics(*args, **kwargs) -> None:
    """
    Receives a variable quantity of numbers as *args
    Receives what to do with the numbers on the **kwargs
    """

    for arg in args:
        if not isinstance(arg, int):
            print("Error: args must be numbers!")
            return

    for key, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif value == "mean":
            mean = sum(args) / len(args) if len(args) > 0 else 0
            print(f"mean : {mean}")
        elif value == "median":
            sort = sorted(args)
            l_args = len(sort)
            if l_args % 2 == 1:
                median = sort[l_args // 2]
            else:
                median = (sort[l_args // 2 - 1] + sort[l_args // 2]) / 2
            print(f"median : {median}")
        elif value == "quartile":
            sorted_args = sorted(args)
            n = len(sorted_args)
            index_q1 = int(0.25 * (n - 1))
            index_q3 = int(0.75 * (n - 1))
            q1 = sorted_args[index_q1] if n % 4 != 0 \
                else (sorted_args[index_q1] + sorted_args[index_q1 + 1]) / 2
            q3 = sorted_args[index_q3] if n % 4 != 0 \
                else (sorted_args[index_q3] + sorted_args[index_q3 + 1]) / 2
            print(f"quartile : [{float(q1)}, {float(q3)}]")
        elif value == "std":
            print(f"std : {std_dev(args)}")
        elif value == "var":
            print(f"var : {variance(args)}")
        else:
            return
