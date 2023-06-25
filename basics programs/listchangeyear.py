# List of months with years
years = ["January 2023", "February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# Update the year to 2023 for each month
updated_years = [month.replace(month[-4:], "2023") for month in years]

# Print the updated list of months with 2023
print("Updated list of months:", updated_years)
