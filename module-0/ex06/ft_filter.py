import types


def ft_filter(func, iterable):
    """
    Function to replicate the filter behavior
    """
    try:
        if not (callable(func) and isinstance(func, types.FunctionType)):
            raise TypeError
        iter(iterable)
        filtered_iterable = [i for i in iterable if func(i)]
        return filtered_iterable

    except TypeError:
        print("First arg must be a function and Second arg an iterable")
