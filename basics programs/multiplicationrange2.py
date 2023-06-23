def display_multiplication_table(start, end):
    for i in range(start, end+1):
        for j in range(1, i+1):
            print(f"{i} * {j} = {i*j}")
        print()

start_table = int(input("Enter the start table: "))
end_table = int(input("Enter the end table: "))

display_multiplication_table(start_table, end_table)
