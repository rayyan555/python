vowels = {'a', 'e', 'i', 'o', 'u'}

def count_vowels(string):
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")

vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
