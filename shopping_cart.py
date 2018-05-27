#POS.py

import datetime #invoking the time module
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

checkout_start_at = datetime.datetime.now()

#print("______________________")
#print("Ken's Random Provisions")
#print("Phone: (Please don't call me)")
#print("www.kennethhuynh.com")
#print("______________________")
#print(checkout_start_at.strftime("%A, %B %d, %Y at %I:%M %p"))

#Capture inputs here

#product_ids = []

#while True:
#    product_id = input(" Hey, please input a product identifier: ")
#    if product_id == "DONE":
#        break #stop the infinite loop
#    else:
#        product_ids.append(product_id)


product_ids = [3,2,1,1]



#for product_id in product_ids:
    #print(product_id)

#Print everything (receipt) at the sametime, after capturing inputs

raw_total = 0
running_total_price = 0

print("                     ")
print("---------------------")
print("Ken's Random Provisions")
print("Phone: (Please don't call me)")
print("www.kennethhuynh.com")
print("---------------------")
print(checkout_start_at.strftime("%A, %B %d, %Y at %I:%M %p"))

print("PURCHASE ITEMS: ")
for product_id in product_ids:
    matching_products = [product for product in products if product ["id"] == product_id]
    matching_product = matching_products[0] #assumes only one match per product ID (no dupes)
    running_total_price += matching_product["price"] #Accumulate a runing total of all items being inputted
    price_usd = ' (${0:.2f})'.format(matching_product["price"]) #Print the price in USD dollar with formatting
    print(" + " + matching_product["name"] + price_usd )

print("---------------------")
running_total_price_usd = ' ${0:.2f}'.format(running_total_price) #for printing in dollar format
print("RUNNING TOTAL:" + str(running_total_price_usd))
print("---------------------")


tax_owed = running_total_price * 0.08875
tax_owed_usd = ' ${0:.2f}'.format(tax_owed)
print("NYC SALES TAX: " + str(tax_owed_usd))
print("---------------------")

#Total amount owed including sales tax_owed
total_owed = running_total_price + tax_owed
total_owed_usd = ' ${0:.2f}'.format(total_owed)
print("YOUR TOTAL OWED IS: " +str(total_owed_usd))

print("THANK YOU FOR SHOPPING KEN'S RANDOM PROVISIONS!")
