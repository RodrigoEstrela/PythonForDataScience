import sys
from ft_filter import ft_filter


def main():
    """
    Program that makes use of custom ft_filter function.
    Receives a string(S) and an integer(N).
    Outputs the words in S that have a length greater than N.
    """
    try:
        assert len(sys.argv) - 1 == 2, "the arguments are bad"
        assert isinstance(sys.argv[1], str), "the arguments are bad"
        length = int(sys.argv[2])
        words = [word for word in sys.argv[1].split()]
        print(list(ft_filter(lambda x: len(x) > length, words)))

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
