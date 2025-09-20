import sys


def analyze_text(text: str):
    """
    Analyzes a given string to count upper-case letters, lower-case letters,
    punctuation marks, spaces, and digits. Then, it prints the results.

    Args:
        text (str): The string to be analyzed.
    """
    total_chars = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())

    punct_count = total_chars - (upper_count + lower_count +
                                 space_count + digit_count)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
    Main function to handle command-line arguments and run the text analyzer.
    - If one argument is provided, it's analyzed.
    - If no arguments, it prompts the user for input.
    - If more than one argument, it prints an assertion error.
    """
    try:
        num_args = len(sys.argv)

        if num_args > 2:
            raise AssertionError("more than one argument is provided")
        elif num_args == 2:
            text_to_analyze = sys.argv[1]
        else:
            print("What is the text to count?")
            text_to_analyze = sys.stdin.read()

        analyze_text(text_to_analyze)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        print("\nInput stream closed. Exiting.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
