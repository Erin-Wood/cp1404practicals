def count_word_occurrences():
    """
    Program to count the occurrences of words in a user-provided string.
    The output will be sorted alphabetically and aligned using the longest word.

    Estimated time: 25 minutes
    """
    text = input("Text: ")

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = dict(sorted(word_count.items()))

    longest_word_length = max(len(word) for word in sorted_word_count)

    for word, count in sorted_word_count.items():
        print(f"{word:{longest_word_length}} : {count}")


count_word_occurrences()
