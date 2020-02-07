import datetime
import time

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


####Master List of ID's####


product_all_id = []

x = 0

while x < len(products):
    dictionary = products[x]
    product_all_id.append(dictionary["id"])
    x = x+1


####Chashier Input####


purchased_products = []
cashier_input = ""


while True:
    cashier_input = input("Please input a product identifier: ")
    if cashier_input == "DONE":
        break
    elif int(cashier_input) in product_all_id:
        matching_products = [item for item in products if item["id"] == int(cashier_input)]
        purchased_products.append(matching_products[0])
    else:
        print("Product not found.")
        #cashier_input = input("Product not found. Please input another product identifier: ")
        #if cashier_input == "DONE":
        #    break


####Receipt####

##Header##

#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------


print("---------------------------------")
print("The Zen of Python Grocery Store")
print("www.zen-python-grocery.com")
print("---------------------------------")


##Date and Time##

#> ---------------------------------
#> CHECKOUT AT: 2019-06-06 11:31 AM
#> ---------------------------------


t = time.localtime() #Code from https://www.programiz.com/python-programming/datetime/current-datetime
current_time = time.strftime("%I:%M %p", t) # code from https://www.programiz.com/python-programming/datetime/current-datetime
                                           #Time format was edited by me to make it more readable to the user

print("---------------------------------")
print(f"CHECKOUT AT: {str(datetime.date.today())} {current_time}")
print("---------------------------------")


##Products##

print("SELECTED PRODUCTS:")

#y=0
#
#
#while y < len(purchased_products):
#    dictionary = purchased_products[y]
#    print("..." + str(dictionary["name"]) + " ($" + str(dictionary["price"]) + ")" )
#    y = y + 1

for each_product in purchased_products:
    #print("..." + str(each_product["name"]) + " ($" + str(each_product["price"]) + ")" )
    print("..." + str(each_product["name"]) + " " + to_usd(each_product["price"]))
exit()

##Subtotal, Tax, and Total##

#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $5.35
#> TOTAL: $66.59
#> ---------------------------------


###Subtotal###

subtotal = 0 #need to figure out the subtotal

while subtotal < len(purchased_product):
    dictionary = purchased_product[subtotal]
    subtotal = subtotal + purchased_product["price"]
price_usd_subtotal = "${0:.2f}".format(subtotal)


###Tax###

def sales_tax(subtotal):
    return subtotal*.06

tax = sales_tax(subtotal)
price_usd_tax = "${0:.2f}".format(tax)


###Total###

sum =  subtotal + tax
price_usd_sum = "${0:.2f}".format(sum)

print("---------------------------------")
print("SUBTOTAL: " + str(price_usd_subtotal))
print("TAX: " + str(price_usd_tax))
print("TOTAL: " + str(price_usd_sum))
print("---------------------------------")
