 # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve user inputs
        tag = request.form.get("symbol")
        company = lookup(tag)

        # Check is symbol is valid
        if company is None:
            return apology("invalid symbol")

        title = company[name]
        price = company[price]
        symbol = company[symbol]

        return render_template("quoted.html", title = title, price = price, symbol = symbol)

    else:
        return render_template("quote.html")