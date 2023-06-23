def generate_password(email):
    # Extract username from email
    username = email.split("@")[0]

    # Generate password by combining username and reverse uppercase of username
    password = username + username[::-1].upper()

    return username, password

# Read input from the user
email_id = input("Enter the email id: ")

# Call the generate_password function
username, password = generate_password(email_id)

# Print the result
print("Username:", username)
print("Password:", password)
