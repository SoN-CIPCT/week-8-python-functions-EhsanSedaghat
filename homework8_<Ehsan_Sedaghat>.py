#Create a function that accepts a list of sandwich ingredients.
#The function should have one parameter that can collect as many arguments as the function call provides.

def sandwich_order(*ingredient_list):

#The function should print a summary of the sandwich being ordered.

    print ("Sandwhich Order Summary:")
    for ingredients in ingredient_list:
        print(f" {ingredients}")

#Call the function two times with a different number of arguments.

sandwich_order("sourdough","roastbeef", "mayo", "onion","lettuce","Cheddar")
sandwich_order("Ciabatta","Mozzarella","Balsamic","Pesto","tomatoes")



