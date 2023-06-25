def invert_dictionary(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    return inverted_dict

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dictionary(my_dict)
print(inverted_dict)
