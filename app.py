from flask import Flask, request, render_template, session, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Add this for sessions

db = pymysql.connect(
    host="localhost", #change to your host
    user="root", #change as needed
    password="Shail1234", #change to your MYSQL password
    database="injection_demo",
    autocommit=True,
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

cursor = db.cursor(pymysql.cursors.DictCursor)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    pwd = request.form["password"]

    # intentionally vulnerable query — supports multi‑statements now
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}';"
    cursor.execute(query)

    result = cursor.fetchall()

    # log attempt
    cursor.execute(
        "INSERT INTO logs (username_attempt, success) VALUES (%s, %s)",
        (user, len(result) > 0)
    )

    if result:
        session['user'] = user  # Store user in session
        return redirect(url_for('products'))

    return render_template("login.html", error="Login failed — try again.")


@app.route("/products")
def products():
    user = session.get('user', 'Guest')  # Get user from session
    return render_template("products.html", items=get_products(), user=user)


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        
        # Vulnerable version for demo
        query = f"INSERT INTO products (name, price) VALUES ('{name}', {price})"
        cursor.execute(query)
        
        return redirect(url_for('products'))
    
    return render_template("add_product.html")


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


def get_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


if __name__ == "__main__":
    app.run(debug=True)