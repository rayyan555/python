# Read the value of n from the user
n = int(input("Enter the number of words (n): "))

# Read n words from the user and store them in a list
words = []
for i in range(n):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

# Display the length of each word
print("Length of each word:")
for word in words:
    print(f"Length of {word}: {len(word)}")

# Find the longest word
longest_word = max(words, key=len)

# Display the longest word
print("Longest word:", longest_word)
