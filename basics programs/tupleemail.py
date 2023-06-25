email_address = input("Enter an email address: ")
username, domain = email_address.split('@')
result = (username, domain)

print("Result:", result)
