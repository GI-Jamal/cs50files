import re
import random
import stripe

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from datetime import date
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd

app = Flask(__name__)

# Declare stripe keys dictionary
stripe_keys = {
    "secret_key": "sk_test_51MFK6ZHree8PKu8Lo2xoBN4JRY8OSo27bwGJOKuSa0WsoHLB01caC6opZSprIeI0vqv5QTlpcv6YPd8ltA8A0jHg00gjhDilFH",
    "publishable_key": "pk_test_51MFK6ZHree8PKu8Lc8b8DzDSKjZ6e36V2oADi5r7bNuCYYjUO88eJdaJpC1I0xlU3TB1nJF1nmgi8VuBWGvBWPYH00iBa7FvOa"
}

# Set test stripe secret key
stripe.api_key = stripe_keys["secret_key"]

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///scooter.db")

# Set temporary user id and check if id already exists in user table
temp_user = random.randint(1, 100000000)
rows = db.execute("SELECT * FROM users WHERE id = ?;", temp_user)

# Change temporary user id if it already exists
while len(rows) > 0:
    temp_user = random.randint(1, 100000000)
    rows = db.execute("SELECT * FROM users WHERE id = ?;", temp_user)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def homepage():

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("homepage.html")


@app.route("/products", methods=["GET", "POST"])
def products():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        if session.get("user_id") is None:
            user = temp_user

        else:
            user = session["user_id"]

        count = request.form.get("quantity")
        item = request.form.get("item")

        if not count.isdigit():
            return apology("invalid quantity")

        if int(count) > 0:

            rows = db.execute("SELECT * FROM cart WHERE product_id = ? AND user_id = ?", item, user)

            if len(rows) > 0:


                amount = db.execute("SELECT quantity FROM cart WHERE user_id = ? AND product_id = ?;", user, item)
                current_amount = amount[0]["quantity"]
                combined_amount = int(count) + int(current_amount)

                if current_amount >= 100:
                    flash("Item(s) not added. Individual item quantity cannot exceed 100")
                    return render_template("products.html")

                elif combined_amount > 100:
                    difference = 100 - current_amount
                    message = "%i item(s) added. Individual item quantity cannot exceed 100" % (difference)
                    flash(message)
                    db.execute("UPDATE cart SET quantity = 100 WHERE user_id = ? AND product_id = ?;", user, item)
                    return render_template("products.html")


                else:
                    db.execute("UPDATE cart SET quantity = quantity + ? WHERE user_id = ? AND product_id = ?;", count, user, item)


            else:
                db.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES(?, ?, ?);", user, item, count)

            message = "%s item(s) added to cart successfully" % (count)
            flash(message)
            return render_template("products.html")

        else:
            return apology("Purchase quantity must be at least 1")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("products.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Forget any user_id
        session.clear()

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Username field cannot be left blank")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Passworld field cannot be left blank")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        user = session["user_id"]

        temp_user

        rows = db.execute("SELECT * FROM cart WHERE user_id = ?", temp_user)

        if len(rows) > 0:
            db.execute("UPDATE cart set user_id = ? WHERE user_id = ?;", user, temp_user)

        # Redirect user to home page
        flash("You have been successfully logged in")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/account")
@login_required
def account():

    user = session["user_id"]
    items = db.execute("SELECT * FROM orders WHERE user_id = ?", user)

    if len(items) == 0:
        return render_template("emptyorders.html")

    else:
        return render_template("account.html", items=items)


@app.route("/orderinfo", methods=["POST"])
@login_required
def orderinfo():

    order_id = request.form.get("order_id")

    items = db.execute("SELECT P.product_name, P.price, O.quantity, O.quantity*P.price AS subtotal FROM order_info AS O JOIN products AS P ON P.product_id = O.product_id WHERE order_id = ? GROUP BY P.product_id;", order_id)
    rows = db.execute("SELECT total FROM orders WHERE order_id = ?", order_id)
    total = rows[0]["total"]

    return render_template("orderinfo.html", items=items, total=total)


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    user = session["user_id"]
    rows = db.execute("SELECT * FROM cart WHERE user_id = ?", user)

    if len(rows) > 0:
        db.execute("UPDATE cart set user_id = ? WHERE user_id = ?;", temp_user, user)

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    flash("You have successfully logged out")
    return redirect("/")


@app.route("/cart")
def cart():

    if session.get("user_id") is None:
        user = temp_user

    else:
        user = session["user_id"]


    itemcount = db.execute("SELECT SUM(quantity) as Quantity FROM cart WHERE user_id = ? GROUP BY user_id;", user)
    try:
        itemcount = itemcount[0]["Quantity"]

    except:
        return render_template("emptycart.html")

    else:


        if itemcount is None or itemcount == 0:
            return render_template("emptycart.html")

        else:
            items = db.execute("SELECT P.product_name AS Product, SUM(C.quantity) as Quantity, P.price AS PricePerUnit, SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY P.product_id", user)
            rows = db.execute("WITH totalcost AS (SELECT  SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY C.product_id) SELECT SUM(Subtotal) AS Total FROM totalcost;", user)
            total = rows[0]["Total"]
            cent_total = total * 100

        return render_template("cart.html", items=items, total=total, cent_total=cent_total, key=stripe_keys["publishable_key"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve user inputs
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if username is blank
        if username == '':
            return apology("username field cannot be left blank")

        # Check if email is blank
        if email == '':
            return apology("email field cannot be left blank")

        # Check is password is blank
        if password == '':
            return apology("password field cannot be left blank")

        # Check is confirmation is blank
        if confirmation == '':
            return apology("confirmation field cannot be left blank")

        # Check is password matches confirmation
        if password != confirmation:
            return apology("password and confirmation do not match")

        if re.search('[0-9]', password) is None or re.search('[A-Z]', password) is None or len(password) < 8:
            return apology("password must be at least 8 characters long, and contain one number and one uppercase letter")

        # Query database for users
        usernames = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Check is username already exists
        if len(usernames) != 0:
            return apology("username already exists")

        # Generate password hash
        hash = generate_password_hash(password)

        # Input user into database
        db.execute("INSERT INTO users(username, hash, email) VALUES(?, ?, ?);", username, hash, email)

        # Redirect to login page
        flash("You have been successfully registered")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/charge", methods=["POST"])
def charge():

    if request.method == "POST":

        if session.get("user_id") is None:
            user = temp_user

        else:
            user = session["user_id"]

        rows = db.execute("WITH totalcost AS (SELECT  SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY C.product_id) SELECT SUM(Subtotal) AS Total FROM totalcost;", user)
        total = rows[0]["Total"]
        try:
            cent_total = total * 100

        except:
            return render_template("emptycart.html")

        else:
            cent_total = int(cent_total)


            try:
                customer = stripe.Customer.create(
                    source=request.form["stripeToken"]
                )

                charge = stripe.Charge.create(
                    customer=customer.id,
                    amount=cent_total,
                    currency='cad',
                    description="Check out"
                )

                email = charge["billing_details"]["name"]

                stripe.PaymentIntent.create(
                    amount=cent_total,
                    currency="cad",
                    payment_method_types=["card"],
                    receipt_email=email
                )

            except:
                return apology("Card error")

            else:
                items = db.execute("SELECT SUM(C.quantity) as quantity FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY user_id;", user)
                quantity = items[0]["quantity"]
                time = date.today()
                if session.get("user_id") is None:
                    insert_user = 0

                else:
                    insert_user = session["user_id"]


                db.execute("INSERT INTO orders (order_date, user_id, item_count, total) VALUES (?, ?, ?, ?);", time, insert_user, quantity, total)
                order_id = db.execute("SELECT order_id from orders ORDER BY order_id DESC LIMIT 1;")
                row_id = order_id[0]["order_id"]
                db.execute("WITH temptable AS (SELECT P.product_id AS Product, SUM(C.quantity) as Quantity, P.price AS PricePerUnit, SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY C.product_id, C.quantity) INSERT INTO order_info (order_id, product_id, quantity, priceperunit) SELECT ?, Product, Quantity, PricePerUnit FROM temptable;", user, row_id)
                db.execute("DELETE FROM cart WHERE user_id = ?;", user)
                return render_template("charge.html", total=total, email=email)


@app.route("/orderupdate", methods=["POST"])
def orderupdate():
    new_count = request.form.get("quantity")
    product = request.form.get("product")
    rows = db.execute("SELECT product_id FROM products WHERE product_name = ?", product)
    product_id = rows[0]["product_id"]
    count = int(new_count)

    if session.get("user_id") is None:
        user = temp_user

    else:
        user = session["user_id"]

    if count == 0:
        db.execute("DELETE FROM cart WHERE product_id = ? AND user_id = ?", product_id, user)

    else:
        db.execute("UPDATE cart SET quantity = ? WHERE product_id = ? AND user_id = ?", count, product_id, user)
        itemcount = db.execute("SELECT SUM(quantity) as Quantity FROM cart WHERE user_id = ?;", user)

    try:
        itemcount = itemcount[0]["Quantity"]

    except:
        items = db.execute("SELECT P.product_name AS Product, SUM(C.quantity) as Quantity, P.price AS PricePerUnit, SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY P.product_id", user)
        rows = db.execute("WITH totalcost AS (SELECT  SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY C.product_id) SELECT SUM(Subtotal) AS Total FROM totalcost;", user)
        total = rows[0]["Total"]
        try:
            cent_total = total * 100

        except:
            flash("You modified your cart!")
            return render_template("emptycart.html")

        else:
            flash("You modified your cart!")
            return render_template("cart.html", items=items, total=total, key=stripe_keys["publishable_key"])

    else:

        if itemcount == 0 or itemcount is None:
            return render_template("emptycart.html")

        else:
            items = db.execute("SELECT P.product_name AS Product, SUM(C.quantity) as Quantity, P.price AS PricePerUnit, SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY P.product_id", user)
            rows = db.execute("WITH totalcost AS (SELECT  SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY C.product_id) SELECT SUM(Subtotal) AS Total FROM totalcost;", user)
            total = rows[0]["Total"]
            cent_total = total * 100

        flash("You modified your cart!")
        return render_template("cart.html", items=items, total=total, cent_total=cent_total, key=stripe_keys["publishable_key"])

@app.route ("/emptycart", methods=["POST"])
def emptycart():

    if session.get("user_id") is None:
        user = temp_user

    else:
        user = session["user_id"]

    db.execute("DELETE FROM cart WHERE user_id = ?", user)

    flash("Your cart has been emptied")
    return render_template("emptycart.html")


if __name__ == '__main__':
    app.run()