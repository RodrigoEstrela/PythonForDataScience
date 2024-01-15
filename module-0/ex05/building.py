import sys
import string


def counting_function(str_in: str):
    """
    Goes through the string counting the number of:
    - Upper-case, lower-case and punction chars,
    - Digits,
    - Spaces.
    """
    upper_count = 0
    lower_count = 0
    digit_count = 0
    punct_count = 0
    space_count = 0

    for c in str_in:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
        elif c.isdigit():
            digit_count += 1
        elif c in string.punctuation:
            punct_count += 1
        elif c.isspace():
            space_count += 1

    return upper_count, lower_count, digit_count, punct_count, space_count


def main():
    """
    Takes a string and sends to counting function after:
    evaluating argv[1] or user input.
    """
    try:
        str_in = ""
        if len(sys.argv) - 1 == 0:
            while len(str_in) == 0:
                try:
                    str_in = input(str("Please provide a string: \n"))
                except EOFError:
                    continue
        else:
            assert len(sys.argv) - 1 == 1, "more than 1 str was provided!"
            str_in = sys.argv[1]

        print(f"The text contains {len(str_in)} characters:")
        u_cnt, l_cnt, d_cnt, p_cnt, s_cnt = counting_function(str_in)
        print(f"{u_cnt} upper letters")
        print(f"{l_cnt} lower letters")
        print(f"{p_cnt} punctuation marks")
        print(f"{s_cnt} spaces")
        print(f"{d_cnt} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
