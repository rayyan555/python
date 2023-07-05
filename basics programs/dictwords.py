digit_word = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

number = input("Enter an integer: ")

result = " ".join([digit_word[int(digit)] for digit in number])

print(result)
