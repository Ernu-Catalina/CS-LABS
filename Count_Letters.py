from collections import Counter


def count_letters(input_string):
    # Remove non-letter characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalpha())

    # Count the frequency of each letter
    letter_counts = Counter(cleaned_string)

    # Sort the letters by frequency (most to least)
    sorted_letters = [letter for letter, _ in sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)]

    return sorted_letters