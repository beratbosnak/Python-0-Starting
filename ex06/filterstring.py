import sys
from ft_filter import ft_filter


def main():
    """
    This program takes a string (S) and an integer (N) as arguments,
    and outputs a list of words from S that have a length greater than N.

    It handles argument count and type errors.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        try:
            n_length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        s_text = sys.argv[1]
        if not isinstance(s_text, str):
            raise AssertionError("the arguments are bad")

        words = s_text.split(' ')

        filtered_words = ft_filter(lambda word: len(word) > n_length, words)

        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
