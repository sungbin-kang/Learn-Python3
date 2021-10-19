# You’ve started position as the lead programmer for the family-style Italian
# # restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing
# fantastically and seen a lot of growth lately. You’ve been hired to keep
# things organized.
from datetime import datetime

# Making the Menues
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items

        # Convert strings to datetime objects
        try:
            self.start_time = datetime.strptime(start_time, "%I%p")
            self.end_time = datetime.strptime(end_time, "%I%p")
        except ValueError:
            print("Time data must match format {2-digit number}{am or pm}")

    def __repr__(self):
        # Convert datetime objects to strings
        start_time = datetime.strftime(self.start_time, "%I%p")
        end_time = datetime.strftime(self.end_time, "%I%p")

        return f"{self.name} is available from {start_time} to {end_time}"

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total

brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}

brunch = Menu("Brunch", brunch_items, "11am", "4pm")
early_bird = Menu("Early-bird Dinner", early_bird_items, "3pm", "6pm")
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")
kids = Menu("Kid's Menu", kids_items, "11am", "9pm")


# test __init__() and __repr__()
print(brunch)
print(early_bird)
print(dinner)
print(kids)

# test calculate_bill()
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


# Creating the Franchises
class Franchise:

    def __init__(self, address, menus):
        self.address = address
        # verify menu is Menu objects
        if all(type(n) is Menu for n in menus):
            self.menus = menus
        else:
            raise Exception("List of menus must contain Menu objects only")

    def __repr__(self):
        return f"{self.address}"

    def available_menues(self, time):
        available = []

        # Convert time string to datetime object
        time_datetime = datetime.strptime(time, "%I%p")

        for menu in self.menus:
            if menu.start_time <= time_datetime <= menu.end_time:
                available.append(menu.name)

        return available


flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# test available_menues()
print(flagship_store.available_menues("12pm"))
print(flagship_store.available_menues("5pm"))


# Creating Businesses!
class Business:
    def __init__(self, name, franchises):
        self.name = name
        if all(type(n) is Franchise for n in franchises):
            self.franchises = franchises
        else:
            raise Exception("List of menus must contain Franchise objects only")


basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50,
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
    }
arepas_menu = Menu("Arepas Menu", arepas_items, "10am", "8pm")
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepas = Business("Take a Arepa", [arepas_place])


# empty line
