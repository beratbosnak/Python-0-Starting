import sys


def main():
    """
    Checks if a number provided as a command-line argument is even or odd.

    - Exits silently if no arguments are given.
    - Prints an assertion error if more than one argument is provided.
    - Prints an assertion error if the argument is not an integer.
    - Prints "I'm Even." or "I'm Odd." based on the number.
    """
    try:
        num_args = len(sys.argv)

        if num_args > 2:
            raise AssertionError("more than one argument is provided")

        if num_args == 1:
            return

        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
