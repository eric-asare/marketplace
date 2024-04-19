#!/usr/bin/python3

import cgi

# Function to save user data to a text file
def save_user_info(name, email, password):
    with open("registered_users.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password: {password}\n")

# Print HTTP header
print("Content-type: text/html\n\n")

# Get form data
form = cgi.FieldStorage()

# Extract form values
name = form.getvalue("name")
email = form.getvalue("email")
password = form.getvalue("password")

# Save user info to file
if name and email and password:
    save_user_info(name, email, password)
    print("<h2>Registration Successful!</h2>")
    print("<a href='index.html'>Homepage</a>")
else:
    print("<h2>Registration Failed. Please fill in all fields.</h2>")
