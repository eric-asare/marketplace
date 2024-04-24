#!/usr/bin/python3

import cgi

# Function to save review info to a text file
def save_review(customer_name, review_text, customer_email=""):
    with open("reviews.txt", "a") as file:
        file.write(f"{customer_name},{customer_email},{review_text}\n")

print("Content-type: text/html\n\n")
form = cgi.FieldStorage()

customer_name = form.getvalue("customer_name")
review_text = form.getvalue("review_text")
customer_email = form.getvalue("customer_email")  # Optional field

if customer_name and review_text:
    save_review(customer_name, review_text, customer_email)
    print("<h2>Thank you for your feedback!</h2>")
    print("<a href='review.html'>Read More reviews</a>")
    print("<br><a href='index.html'>Return to Homepage</a>")
else:
    print("<h2>Failed to submit your review. Please ensure all required fields are filled.</h2>")
    print("<a href='review.html'>Return to the review Submission Form</a>")
