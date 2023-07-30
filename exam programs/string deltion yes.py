def is_obtained_by_deletion(string1, string2):
    for char in string2:
        if char not in string1:
            return False
    return True

# Get the two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the second string can be obtained from the first string
if is_obtained_by_deletion(string1, string2):
    print("YES")
else:
    print("NO")
