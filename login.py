#!/usr/bin/python3

import cgi
import cgitb

# Enable debugging
cgitb.enable()

# Function to check if user is registered
def is_user_registered(email, password):
    with open("registered_users.txt", "r") as file:
        for line in file:
            name, reg_email, reg_password = line.strip().split(', ')
            if email == reg_email and password == reg_password:
                return True
    return False

# Print HTTP header
print("Content-type: text/html\n")
print()

# Get form data
form = cgi.FieldStorage()

# Extract form values
email = form.getvalue("email")
password = form.getvalue("password")

# Check if user is registered and display a message
if email and password:
    if is_user_registered(email, password):
        print("<h2>Welcome back! You are registered.</h2>")
    else:
        print("<h2>Sorry, you are not registered.</h2>")
else:
    print("<h2>Please provide both email and password.</h2>")
