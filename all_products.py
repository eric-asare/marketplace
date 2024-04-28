#!/usr/bin/python3

print("Content-Type: text/html\n\n") 
import cgi
import cgitb; cgitb.enable()  # for debugging purposes

form = cgi.FieldStorage()
search_query = form.getvalue('search', '').lower()

def read_products(filename, search_query):
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5 and (search_query in parts[1].lower() or not search_query):
                    products.append({'id': parts[0], 'name': parts[1], 'description': parts[2], 'price': parts[3], 'image_url': parts[4]})
    except FileNotFoundError:
        print("<p>Error: The file containing the products was not found.</p>")
    return products

def print_product_table(products):
    table_html = '<table class="table">\n<thead>\n<tr>\n'
    table_html += '<th>Image</th>\n<th>Name</th>\n<th>Description</th>\n<th>Price</th><th>Delete</th>\n</tr>\n</thead>\n<tbody>\n'
    for product in products:
        table_html += f'<tr>\n<td><img src="{product["image_url"]}" alt="{product["name"]}" style="width:100px;"></td>\n'
        table_html += f'<td>{product["name"]}</td>\n<td>{product["description"]}</td>\n'
        table_html += f'<td>${product["price"]}</td>\n'
        table_html += f'<td><a href="delete-product.py?id={product["id"]}" class="delete-btn">Delete</a></td>\n'
    table_html += '</tbody>\n</table>\n'
    return table_html


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All Products</title>
    <link rel="stylesheet" href="css/style.css?v=1.0">
    <link rel="stylesheet" href="css/all_products.css?v=1.01">
</head>
<body>

<!-- Header section -->
<div class="header-container">
    <h1 class="marketplace-name">NYUAD Marketplace</h1>
</div>

<!-- Navigation bar -->
<nav class="navbar navbar-expand-lg">
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

<!-- Search form -->
<div class="container mt-5">
    <!-- Search form -->
    <div class="search-container">
        <form action="all_products.py" method="get">
            <input type="text" name="search" placeholder="Search by name" value="">
            <input type="submit" value="Search">
        </form>
    </div>
    
    <h1 class="mb-4">All Products</h1>
    """)
products = read_products('products.txt', search_query)
print(print_product_table(products))

print("""
</div> <!-- /container -->
<!-- Footer -->
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


