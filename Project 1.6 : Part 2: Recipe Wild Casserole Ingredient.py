file_name = input ('Please enter the name of the file: ')
file_open = open (file_name)

while True:

    question1 = input ('Hello user, what would you like to do? type (X) to view the steps / (Y) to view ingredients / (Z) to exit the program: ')


    file_list = list()
    if question1 == 'X':
        print ("You've chosen to view the steps")
        for file1 in file_open:
            if not file1.startswith ('Ingredient:'):  #if not file1.startwith will exclude everything that starts with 'Ingredient'
                file1 = file1.rstrip ()
                #print (file1)
                if file1 not in file_list:          #this loop will add everything to the list
                    file_list.append (file1)
        print (file_list)
        continue


    elif question1 == 'Y':
        print ("You've chosen to view the ingredients")
        ingredient = dict ()                        #add all the keys and values
        ingredient ["cup uncooked wild rice"] = .75
        ingredient ["tablespoon and teaspoon of olive oil"] = 1
        ingredient ["ounces onions"] = 4
        ingredient ["cloves garlic"] = 2
        ingredient ["ounces eggpant"] = 8
        ingredient ["ounces zucchini"] = 4
        ingredient ["cup canned, diced tomatoes, drained"] = 1
        ingredient ["dash basil"] = 1
        ingredient ["dash pepper"] = 1
        ingredient ["cup grated Monterey Jack cheese"] = 1
        ingredient ["cup grated Parmesan Cheese"] = 1
        print (ingredient)
        continue

    else:
        print ("You've chosen to exit the program, thank you")
        quit ()

