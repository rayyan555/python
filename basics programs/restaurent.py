#question :Restaurant Tip Calculator:
#Steps:
#Rating will be ( 1 is bad, 2 - not bad, 3 - average, 4 - good and 5 is excellent)
#Read Food Rating: 1-5 
#Read Service Rating: 1-5
#Read Ambience Rating:1-5
#Read Bill amount
#If the Food is good or excellent:
#Service and ambience is also good -excellent
#Then Tip is 10% of your Bill amount
#Service and ambience is avg/okay/bad
#Then Tip is 5% of your Bill amount
#If the Food is avg/okay/bad:
#Service and ambience is also good -excellent
#Then the Tip is 5% of your Bill amount
#Service and ambience is avg/okay/bad
#Then the Tip is 1% of your Bill amount

# Read ratings and bill amount
food_rating = int(input("Food Rating (1-5): "))
service_rating = int(input("Service Rating (1-5): "))
ambience_rating = int(input("Ambience Rating (1-5): "))
bill_amount = float(input("Bill Amount: "))

# Calculate tip amount based on ratings and bill amount
if food_rating >= 4 and (service_rating >= 4 and ambience_rating >= 4):
    tip_percent = 0.10  # 10% tip for excellent food, service, and ambience
elif food_rating >= 4:
    tip_percent = 0.05  # 5% tip for excellent food and average/bad service or ambience
else:
    tip_percent = 0.01  # 1% tip for average/bad food

# Calculate tip amount
tip_amount = bill_amount * tip_percent

# Print the tip amount
print("Tip Amount: ", tip_amount)
