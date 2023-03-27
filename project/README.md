# SCOOTER BOI

## Video Demo:  <https://youtu.be/8ZxvKgdQDEI>

## Description:


### Introduction

For my final project I decided to create an e-commerce site for a fictitious company called Scooter Boi. With the increase in the costs of fossil fuels and as well as our overall concern for the environment, many people are looking at alternative ways to travel. Scooter Boi is an online store that would sell personal electric vehicles (e.g., scooter, bikes, etc.), to bridge the gap between fully electric vehicles and traditional bicycles, allowing more people access to cost effective and environmentally friendly transport.


### How it Works

The website was made in Python using the Flask web framework, with many of the aesthetic features made using the Bootstrap CSS framework. SQLITE3 was used as the database to store user, product, and order information and credit cart payments were handled using the Stripe payment processing platform.

Navigating to the Scooter Boi page for the first time will take users to the homepage. From there they can navigate to several pages:

-	The products page to add items to their cart
-	The cart page to view, modify, and checkout the items in their cart
-	The register page to become a member if they are not already logged in
-	The login page to log in to their account and gain access to their   own order history

If users are logged in, they will lose access to the register and login page, but gain access to the following pages:

-	The account page, where every order placed by the member will be displayed, along with an option to view the contents of each order
-	The log out page for users to log out of their account


### Key Features

When opening the Scooter Boi webpage, every user is assigned a temporary user ID. This temporary user ID will be used to associate the user to the items they add to their cart. Should a user login to their account after having already added items to their cart anonymously, the items will now be associated to the user’s actual account ID stored in the SQLITE3 “users” table. If that same user would happen to log out before checking out, the items in their cart will become associated to the temporary user ID originally assigned when they opened the Scooter Boi webpage so that they may continue their shopping experience uninterrupted.

After a user check out the items in their cart, an email receipt is generated using the email address input during the check out process. As this project uses test API keys for the Stripe payment platform, the email receipt will not be sent automatically, but can be seen from the Visual Studio Code Terminal or Stripe website and sent using the Stripe dashboard. If production API keys were to be used, then the emails would be sent automatically.

Once check out is complete and the success page has loaded, if a user is logged in then they can navigate to their account page to view the order information from the user’s entire order history.


### Project Contents

The project contains the following files.

Two Python files:

    1.	app.py
    2.	helpers.py

One SQLITE3 database:

    1.	scooter.db

One style sheet:

    1.	styles.css

Twelve HTML templates:

    1.	account.html
    2.	apology.html
    3.	cart.html
    4.	charge.html
    5.	emptycart.html
    6.	emptyorders.html
    7.	homepage.html
    8.	layout.html
    9.	login.html
    10.	orderinfo.html
    11.	products.html
    12.	register.html

Five images:

    1.	check_mark.png
    2.	empty-cart.png
    3.	no-orders.jpg
    4.	scooterboi.jpg
    5.	scootericon.png


### Future improvements

There are numerous ways of improving the website. Some ideas include:

-	Adding an option to filter or search for products on the products page
-	Adding images of products and individual product pages with detailed spec information
-	Improving the code associated with the orderupdate route to make it more robust
-	Improving the general aesthetic of the homepage and the success page
-	Updating the Stripe payment platform from the legacy version to the current version
-	Improve the algorithm used to set the temporary user ID to prevent potential conflicts with registered users.
-	Adding functionality for an administrator to easily add or remove products without editing the sites HTML code