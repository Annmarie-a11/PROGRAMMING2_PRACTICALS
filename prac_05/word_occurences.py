
"""
Word Occurrences
Estimate: 30 minutes
Actual:   51 minutes
"""


def main():
    """
    Counts the occurrences of words in a string, then prints the counts
    sorted and neatly aligned.
    """
    word_counts = {}

    # 1. Ask the user for a string
    text = input("Text: ")

    # Clean the text and split into words
    words = text.split()

    # 2. Count word occurrences
    for word in words:
        # Normalize the word to lowercase for accurate counting
        clean_word = word.lower()

        # Hint: check if word is in the dictionary (LBYL approach)
        if clean_word in word_counts:
            word_counts[clean_word] += 1
        else:
            word_counts[clean_word] = 1

    # 3. Sort the words
    # Get a list of the words (keys) and sort them alphabetically
    sorted_words = sorted(word_counts.keys())

    # 4. Find the longest word for alignment
    # The max() function can find the maximum length of a word in the list
    if sorted_words:
        # Calculate the length of the longest word
        longest_word_length = max(len(word) for word in sorted_words)
    else:
        longest_word_length = 0

    # Print the counts, sorted and aligned
    print("--- Word Counts ---")
    for word in sorted_words:
        count = word_counts[word]
        # Use f-string formatting with a variable width for alignment
        # {word:<{longest_word_length}} ensures left alignment up to the longest length
        print(f"{word:<{longest_word_length}} : {count}")

if __name__ == "__main__":
    main()
