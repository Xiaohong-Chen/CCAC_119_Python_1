inputVegetarian = input("Is anyone in your party a vegetarian?")
inputVegan = input("Is anyone in your party a vegan?")
inputGlutenFree = input("Is anyone in your party gluten-free?")
if inputVegetarian == "yes" and inputVegan=="yes" and inputGlutenFree =="yes":
    print("Here are your restaurant choices:")
    print("   Corner Cafe")
    print("   The Chef's Kitchen")
else:
    if inputVegetarian == "yes" and inputVegan=="no" and inputGlutenFree =="yes":
        print("Here are your restaurant choices:")
        print("   Main Street Pizza Company")
        print("   Corner Cafe")
        print("   The Chef's Kitchen")
    else:
        if inputVegetarian == "yes" and inputVegan=="no" and inputGlutenFree =="no":
            print("Here are your restaurant choices:")
            print("   Mama's Fine Italian")
        else:
            if inputVegetarian == "yes" and inputVegan=="yes" and inputGlutenFree =="no":
                print("Here are your restaurant choices:")
                print("   Corner Cafe")
                print("   The Chef's Kitchen")
            else:
                print("Here are your restaurant choices:")
                print("   Joe's Counrmet Burgers")