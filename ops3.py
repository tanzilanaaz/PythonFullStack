username = "tanu"
password = "tanu123"

username_in = input("Enter the username:::")
password_in = input("Enter the password:::")

if username == username_in and password == password_in:
    print("Welcome {} , you are a valid user".format(username))
else:
    print("Sorry {}, Please enter a valid username/password".format(username))


#to make this case insensitive, there are 2ways,
# 1. either use .lower() or .upper()
# 2. other inbuilt python function is .casefold()

