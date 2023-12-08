"""
Word Occurences
Estimate :1hour
Actual Time: 58mins
"""


def main():
    user_input_text = input("Enter Text: ")
    word_occurrences = {}
    words = user_input_text.split()
    words.sort()
    calculate_word_occurrences(word_occurrences, words)
    display_word_occurrences(word_occurrences)

def display_word_occurrences(word_occurrences):
    """Display word occurrences"""

    for word, count in word_occurrences.items():
        word, width = word, 10
        print(f"{word:{width}} = {count}")

def calculate_word_occurrences(word_occurrences, words):
    """Strip unnecessary characters from words and count occurrences"""

    for word in words:
        clean_word = word.strip(". , ! ? /")
        word_occurrences[clean_word] = word_occurrences.get(clean_word, 0) + 1

main()
