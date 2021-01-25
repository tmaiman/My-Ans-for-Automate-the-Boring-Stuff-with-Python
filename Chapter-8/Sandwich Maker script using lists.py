#Sandwich Maker script using lists inside a tuple
import pyinputplus as pyin

class Sandwich:
    MENU = ([], [], [], [])    #Menu objects are stored here
    layer = 0                  #Tracks layer selection
    totalPrice = 0.0           #Tracks total costs
    def __init__(self, set_layer, menu, price):
        self.menu, self.price = menu, price
        Sandwich.MENU[set_layer].append(self)

    def addPrice(self, choice):
        Sandwich.totalPrice +=  Sandwich.MENU[Sandwich.layer][int(choice) - 1].price
        return choice
    
def generateList():
        for sw in Sandwich.MENU[Sandwich.layer]:
            yield sw.menu
    
#To add menu item, add line below
#Layer: Bread = 0, Protein = 1, Cheese = 2, Garnish = 3
#Sandwich(layer, 'Name', price)

Sandwich(0, 'Wheat', 3.0)
Sandwich(0, 'White', 2.0)
Sandwich(0, 'Sourdough', 4.0)

Sandwich(1, 'Chicken', 2.0)
Sandwich(1, 'Turkey', 3.0)
Sandwich(1, 'Ham', 4.0)
Sandwich(1, 'Tofu', 2.0)

Sandwich(2, 'Cheddar', 2.0)
Sandwich(2, 'Swiss', 3.0)
Sandwich(2, 'Mozzarella', 3.0)

Sandwich(3, 'Mayo', 0.5)
Sandwich(3, 'Mustard', 1.0)
Sandwich(3, 'Lettuce', 0.5)
Sandwich(3, 'Tomato', 0.5)

Sandwich.layer = 0
bread = pyin.inputMenu([*generateList()], prompt='Choose your bread\n', blank=True, numbered=True, applyFunc=Sandwich.addPrice)

Sandwich.layer = 1
protein = pyin.inputMenu([*generateList()], prompt='Choose your protein\n', numbered=True, applyFunc=Sandwich.addPrice)

if pyin.inputYesNo('Do you want cheese?') == 'yes':
    Sandwich.layer = 2
    cheese = pyin.inputMenu([*generateList()], numbered=True,
                            applyFunc=Sandwich.addPrice)
else:
    cheese = "no"

if pyin.inputYesNo('Do you want to add garnish?') == 'yes':
    Sandwich.layer = 3
    garnish = pyin.inputMenu([*generateList()], numbered=True, applyFunc=Sandwich.addPrice)
else:
    garnish = "no"

sandwich_number = pyin.inputInt('How many such sandwiches that you want? ', min=1)

print(f'You ordered {sandwich_number} sandwich(es) with {bread} bread, {protein} protein, {cheese} cheese and {garnish} garnish')
      
print(f'\nTotal price is = RM{(Sandwich.totalPrice * sandwich_number):.2f}')

#end of code#
