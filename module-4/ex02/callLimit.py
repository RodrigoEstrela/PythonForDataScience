def callLimit(limit: int):
    """Decorator to stop running a function after [limit] times"""
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwargs):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
