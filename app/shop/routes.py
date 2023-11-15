from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this!

# Replace with your product retrieval logic from the database
products = [
    {"id": 1, "name": "Product 1", "price": "20$", "image": "image_url_1"},
    {"id": 2, "name": "Product 2", "price": "30$", "image": "image_url_2"},
    # Add more products...
]

cart = []

@app.route('/')
def index():
    return redirect(url_for('product_list'))

@app.route('/products')
def product_list():
    products = Product.query.all()
    print(products)

    products.append({
        "name":"Hair Cream",
        "Price": "20$",
        "Image":"https://m.media-amazon.com/images/I/51eZn9z+E3L._SY300_SX300_.jpg"
    })
    products.append({
        "name":"LATTAFA QAED AL FURSAN",
        "Price": "20$",
        "Image":"https://m.media-amazon.com/images/I/51+kkdlWlAL._SX679_.jpg"
    })
    products.append({
        "name":"SheaMoisture",
        "Price": "13$",
        "Image":"https://m.media-amazon.com/images/I/61xIOun2OIL._SX679_.jpg"
    })
    products.append({
        "name":"Shiva Face & Body Scrub",
        "Price": "10$",
        "Image":"https://m.media-amazon.com/images/I/511w09Z0o9L._AC_SX679_.jpg"
    })
    products.append({
        "name":"Happiness Beauty Hair Color Shampoo",
        "Price": "20$",
        "Image":"https://m.media-amazon.com/images/I/61tHQdtGj4L._AC_SY879_.jpg"
    })
    products.append({
        "name":"Lattafa Ana Abiyedh",
        "Price": "20$",
        "Image":"https://m.media-amazon.com/images/I/41E547cb+eL._SX679_.jpg"
    })
    return render_template('product_list.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product_details.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        cart.append({"product": product, "quantity": quantity})

    return redirect(url_for('product_list'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    cart.clear()
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)