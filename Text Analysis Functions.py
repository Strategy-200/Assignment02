# Text Analysis Functions

def count_words(text):
    return len(text.split())


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    processed = text.replace(" ", "").lower()
    return processed == processed[::-1]


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def longest_word(text):
    words = text.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    print("Palindrome:", "Yes" if is_palindrome(text) else "No")

    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print(f"Longest word: {lw} ({len(lw)} letters)")

    freq = word_frequency(text)

    print("Word Frequency:", end=" ")
    freq_list = [f"{word}: {count}" for word, count in freq.items()]
    print(", ".join(freq_list))


# Main input
user_text = input("Enter text: ")
analyze_text(user_text)