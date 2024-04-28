#!/usr/bin/python3

import cgi

print("Content-Type: text/html\n\n")

def delete_product(product_id):
    with open("products.txt", "r") as file:
        lines = file.readlines()
    with open("products.txt", "w") as file:
        for line in lines:
            if line.split(',')[0] != product_id:
                file.write(line)

print("Content-type: text/html\n\n")
form = cgi.FieldStorage()

product_id = form.getvalue("product_id")

if product_id:
    delete_product(product_id)
    print("<h2>Product Deleted Successfully!</h2>")
    print("<a href='index.html'>Return to Homepage</a>")
else:
    print("<h2>Failed to delete product. Please provide a valid product ID.</h2>")
