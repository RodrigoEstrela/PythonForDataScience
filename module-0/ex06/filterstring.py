import sys
from ft_filter import ft_filter


def main():
    """
    Program that makes use of custom ft_filter function.
    Receives a string(S) and an integer(N).
    Outputs the words in S that have a length greater than N.
    """
    try:
        assert len(sys.argv) - 1 != 2, "the arguments are bad"
        assert isinstance(sys.argv[1], str) \
               or isinstance(sys.argv[2], int), "the arguments are bad"

    except AssertionError:
        print(AssertionError)


if __name__ == "__main__":
    main()
