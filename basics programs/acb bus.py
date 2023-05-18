current_year = 2023  # Update the current year as per the desired year

fare = 1020
age_limit = 60

# User input
year_of_birth = int(input("Enter the year of birth: "))

# Calculate the age
age = current_year - year_of_birth

# Check if the person is a senior citizen
if age > age_limit:
    discounted_fare = fare - (fare * 0.2)  # 20% concession
    print("Final traveling charge:", discounted_fare)
else:
    print("Original fare:", fare)
