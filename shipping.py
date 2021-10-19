weight = float(input("Type in your package weight: "))

# Ground Shipping
ground_price_per_weight = 0
ground_flat_charge = 20.00

if weight <= 2:
    ground_price_per_weight = 1.50
elif 2 < weight <= 6:
    ground_price_per_weight = 3.00
elif 6 < weight <= 10:
    ground_price_per_weight = 4.00
else:
    ground_price_per_weight = 4.75

cost_of_ground_shipping = weight * ground_price_per_weight + ground_flat_charge
print("Ground Shipping price for " + str(weight) + " lbs package is $" + str(cost_of_ground_shipping))


# Premium Ground Shipping
cost_of_premium_ground_shipping = 125.00
print("Premium Ground Shipping price for any package is flat rate of $" + str(cost_of_premium_ground_shipping))


# Drone Shipping
drone_price_per_weight = 0
drone_flat_charge = 0
if weight <= 2:
    drone_price_per_weight = 4.50
elif 2 < weight <= 6:
    drone_price_per_weight = 9.00
elif 6 < weight <= 10:
    drone_price_per_weight = 12.00
else:
    drone_price_per_weight = 14.25

cost_of_drone_shipping = weight * drone_price_per_weight + drone_flat_charge
print("Drone Shipping price for " + str(weight) + " lbs package is $" + str(cost_of_drone_shipping))

# empty line
