import os
import datetime
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user = session["user_id"]
    stocks = db.execute(
        "SELECT symbol, title, SUM(shares) as shares, share_price as price, SUM(total_value) as total FROM stockpurchases WHERE userid = ? GROUP BY symbol HAVING SUM(shares) > 0;", user)
    userinfo = db.execute("SELECT * FROM users WHERE id = ?;", user)
    cashworth = userinfo[0]["cash"]
    stockval = db.execute("SELECT SUM(total_value) as total FROM stockpurchases WHERE userid = ?;", user)
    stockworth = stockval[0]["total"]
    if stockworth is None:
        stockworth = 0
    networth = cashworth + stockworth
    return render_template("index.html", stocks=stocks, cashworth=cashworth, networth=networth)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve user inputs
        tag = request.form.get("symbol")
        quantity = request.form.get("shares")

        # Check is symbol is valid
        company = lookup(tag)
        if company is None:
            return apology("invalid symbol")

        # Check quantity requested is greater than 0
        if quantity == '':
            return apology("invalid quantity")

        if not quantity.isdigit():
            return apology("invalid quantity")

        if float(quantity) < 1:
            return apology("invalid quantity")

        # Set company attributes
        label = company["name"]
        cost = company["price"]
        code = company["symbol"]

        # Check if user has sufficient funds
        total = float(quantity) * cost
        user = session["user_id"]
        userinfo = db.execute("SELECT * FROM users WHERE id = ?", user)
        funds = userinfo[0]["cash"]
        if total > funds:
            return apology("insufficient funds")

        # Update database with stockpurchases details
        balance = funds - total
        time = datetime.datetime.now()
        action = "buy"
        db.execute("INSERT INTO stockpurchases (userid, title, symbol, shares, share_price, total_value, date_time, new_balance) VALUES(?, ?, ?, ?, ?, ? ,? , ?);",
                   user, label, code, quantity, cost, total, time, balance)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, user)

        # Redirect to quoted page
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of stockpurchases"""

    user = session["user_id"]

    transactions = db.execute("SELECT symbol, shares, share_price, date_time FROM stockpurchases WHERE userid = ?;", user)

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve user inputs
        tag = request.form.get("symbol")

        # Check is symbol is valid
        company = lookup(tag)
        if company is None:
            return apology("invalid symbol")

        # Set company attributes
        label = company["name"]
        cost = company["price"]
        code = company["symbol"]

        # Redirect to quoted page
        return render_template("quoted.html", label=label, cost=cost, code=code)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve user inputs
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if username is blank
        if username == '':
            return apology("username field cannot be left blank")

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
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?);", username, hash)

        # Redirect to login page
        return render_template("registered.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # Retrieve user inputs
        tag = request.form.get("symbol")
        quantity = request.form.get("shares")

        # Check is symbol is valid
        company = lookup(tag)
        if company is None:
            return apology("invalid symbol")

        # Check quantity requested is greater than 0
        if quantity == '':
            return apology("invalid quantity")
        if float(quantity) <= 0:
            return apology("invalid quantity")

        # Set company attributes
        label = company["name"]
        cost = company["price"]
        code = company["symbol"]

        # Check if user has sufficient shares
        user = session["user_id"]
        sharesowned = db.execute("SELECT SUM(shares) as shares FROM stockpurchases WHERE userid = ? AND symbol = ?;", user, code)
        if float(quantity) > float(sharesowned[0]["shares"]):
            return apology("insufficient shares")

        total = float(quantity) * cost
        userinfo = db.execute("SELECT * FROM users WHERE id = ?", user)
        funds = userinfo[0]["cash"]
        time = datetime.datetime.now()
        balance = funds + total
        quantity = float(quantity) * -1
        total = total * -1
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, user)
        db.execute("INSERT INTO stockpurchases (userid, title, symbol, shares, share_price, total_value, date_time, new_balance) VALUES(?, ?, ?, ?, ?, ? ,? , ?);",
                   user, label, code, quantity, cost, total, time, balance)

        return redirect("/")

    else:
        user = session["user_id"]
        stocks = db.execute("SELECT DISTINCT(symbol) as symbol from stockpurchases WHERE userid = ?;", user)
        return render_template("sell.html", stocks=stocks)