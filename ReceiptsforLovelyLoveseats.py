lovely_loveseat_description = """
Lovely Loveseat. Turfed ployester blended on wood.
 32 inches high x 40 inches wide x 30 inces deep. Red or white.
 """

lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Sette. Faux leather on birch. 
29.50 inches high x 54.75 inches wide x 28 inces deep. Black"""

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

sales_tax = .088

# Customer One
customer_one_total = 0
customer_one_itemization = ""

# customer one buys Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + "\n"

# customer one buys Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description + "\n"

# customer one ready to purchase
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# print customer one receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

# empty line
