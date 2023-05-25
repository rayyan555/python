def display_multiplication_table(start, end):
    for i in range(1, 11):
        for j in range(start, end+1):
            print(f"{j} * {i} = {j * i}\t", end="")
        print()

start_table = int(input("Start Table: "))
end_table = int(input("End Table: "))

display_multiplication_table(start_table, end_table)
