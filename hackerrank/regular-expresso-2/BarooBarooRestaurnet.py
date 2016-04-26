import re

regex = r'[batr]$|te$'
print(len(regex))
def test(regex,word):
    return str(bool(re.search(regex,word))).lower()

good = ["Fiesta Omelette","Meat Plate","Prime Rib","Chicken Pasta",\
        "Pineapple Blast","Red Lobster","Pizzeria","Steakburger"]
bad = ["Greek Roast Fish","Euro Pulled Chicken","Egg Foo Young","Chicken Tacos","Maki Rolls","Warm Chorizo","Courgetti Bolognese","Szechwan Shrimp"]

for word in good:
    print(test(regex,word),word)
print()
for word in bad:
    print(test(regex,word),word)
    
