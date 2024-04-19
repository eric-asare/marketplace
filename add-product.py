#!/usr/bin/python3

import cgi

# Function to save product info to a text file
def save_product_info(product_name, description, price, image_url):
    with open("products.txt", "a") as file:
        file.write(f"{product_name},{description},{price},{image_url}\n")

print("Content-type: text/html\n\n")
form = cgi.FieldStorage()

product_name = form.getvalue("product_name")
description = form.getvalue("description")
price = form.getvalue("price")
image_url = form.getvalue("image_url")

if product_name and description and price:
    save_product_info(product_name, description, price, image_url)
    print("<h2>Product Added Successfully!</h2>")
    print("<a href='index.html'>Return to Homepage</a>")
else:
    print("<h2>Failed to add product. Please ensure all fields are filled.</h2>")
