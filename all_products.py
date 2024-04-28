#!/usr/bin/python3

print("Content-Type: text/html\n\n") 
import cgi
import cgitb; cgitb.enable()  # for debugging purposes


def read_products(filename):
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    products.append({
                        'id': parts[0],
                        'name': parts[1],
                        'description': parts[2],
                        'price': parts[3],
                        'image_url': parts[4]
                    })
    except FileNotFoundError:
        print("<p>Error: The file containing the products was not found.</p>")
    return products

def print_product_table(products):
    table_html = '<table class="table">\n<thead>\n<tr>\n'
    table_html += '<th>Image</th>\n<th>Name</th>\n<th>Description</th>\n<th>Price</th>\n</tr>\n</thead>\n<tbody>\n'
    for product in products:
        table_html += f'<tr>\n<td><img src="{product["image_url"]}" alt="{product["name"]}" style="width:100px;"></td>\n'
        table_html += f'<td>{product["name"]}</td>\n<td>{product["description"]}</td>\n'
        table_html += f'<td>${product["price"]}</td>\n</tr>\n'
    table_html += '</tbody>\n</table>\n'
    return table_html



print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All Products</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/all_products.css">
</head>
<body>
<div class="navbar-wrapper">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">NYUAD Marketplace</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="index.html">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="shop.html">Shop</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="add_product.html">Add Product</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="why_us.html">Why Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="testimonials.html">Testimonials</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="contact.html">Contact Us</a>
                </li>
            </ul>
        </div>
    </nav>
</div>
<div class="container mt-5">
    <h1 class="mb-4">All Products</h1>

""")

products = read_products('products.txt')
print(print_product_table(products))

print("""
</div> <!-- /container -->
<footer class="footer bg-dark text-white mt-5">
    <div class="container text-center py-3">
        &copy; <span id="displayYear"></span> All Rights Reserved By NYUAD Marketplace
    </div>
</footer>
<script src="/js/jquery-3.4.1.min.js"></script>
<script src="/js/popper.min.js"></script>
<script src="/js/bootstrap.min.js"></script>
<script>
    document.getElementById('displayYear').textContent = new Date().getFullYear();
</script>
</body>
</html>
""")

