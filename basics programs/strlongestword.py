def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    longest_word = max(words, key=len)
    longest_length = len(longest_word)
    return longest_word, longest_length

# Read input from the user
input_sentence = input("Enter a sentence: ")

# Call the find_longest_word function
longest_word, longest_length = find_longest_word(input_sentence)

# Print the result
print("Longest word:", longest_word)
print("Length of the longest word:", longest_length)
