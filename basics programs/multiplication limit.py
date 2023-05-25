def display_multiplication_table(start_table, end_table):
    for i in range(1, 11):
        for j in range(start_table, end_table + 1):
            print(f"{j} * {i} = {j * i}\t", end="")
        print()

start_table = 5  # Change the start table value here
end_table = 8    # Change the end table value here

display_multiplication_table(start_table, end_table)
