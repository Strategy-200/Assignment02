# String Manipulator Program
# This program performs various operations on a user-entered sentence

# Taking input from the user
sentence = input("Enter a sentence: ")

# Checking for empty input
if len(sentence) == 0:
    print("You entered an empty sentence!")
else:
    # Original sentence
    print("\nOriginal:", sentence)

    # Total characters with spaces
    total_chars_with_spaces = len(sentence)
    print("Characters (with spaces):", total_chars_with_spaces)

    # Total characters without spaces
    total_chars_without_spaces = len(sentence.replace(" ", ""))
    print("Characters (without spaces):", total_chars_without_spaces)

    # Splitting sentence into words
    words = sentence.split()
    total_words = len(words)
    print("Words:", total_words)

    # Uppercase
    print("UPPERCASE:", sentence.upper())

    # Lowercase
    print("lowercase:", sentence.lower())

    # Title Case
    print("Title Case:", sentence.title())

    # First word
    print("First word:", words[0])

    # Last word
    print("Last word:", words[-1])

    # Reversed sentence
    reversed_sentence = sentence[::-1]
    print("Reversed:", reversed_sentence)