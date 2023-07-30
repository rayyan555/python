def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into individual words
    longest_word = max(words, key=len)  # Find the word with the maximum length
    longest_length = len(longest_word)  # Get the length of the longest word
    return longest_word, longest_length

# Get user input for the sentence
sentence = input("Enter a sentence: ")

# Find the longest word and its length
longest_word, longest_length = find_longest_word(sentence)

# Display the result
print("Longest Word:", longest_word)
print("Length of Longest Word:",longest_length)
