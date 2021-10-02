#user_input = input ('please enter the name of the file: ')
#user_open = open (user_input)


user_open = open ('food.txt')
#user_open = user_open.read()
#print (user_open)

for user_open1 in user_open:
    user_open2 = user_open1.rstrip()
    #user_open2 = user_open1.split (';')

    if  user_open2.startswith ('Asian'):
        asian_file = user_open2.split (';')
        #print (asian_file)
 
    elif  user_open2.startswith ('American'):
        american_file = user_open2.split (';')
        #print (american_file)

    elif user_open2.startswith ('Mexican:'):
        mexican_file = user_open2.split (';')
        #print (mexican_file)
  
    elif user_open2.startswith ('Comfort food:'):
        comfort_food_file = user_open2.split (';')
        #print (comfort_food_file)

    elif user_open2.startswith ('Healthy food:'):
        healthy_food_file = user_open2.split(';')
        #print (healthy_food_file)
 
    elif user_open2.startswith ('Fast food:'):
        fast_food_file = user_open2.split(';')
        #print (fast_food_file)



print ('Hello Welcome to ChosenMeal')
name_input = input ('Before we start can you tell me your name: ')



while True:
    print ('Ok', name_input)
    user_input = input ('What would you like to do? press (X) for choose a meal or (Y) for randomized meal: ')

    if user_input == 'X':
        user_question = input ('What type of food would you like? Asian, American, Mexican, Comfort food, Healthy food, or Fast food: ')

        if user_question == 'Asian':
            print('Here is the selection for', asian_file)
            asian_question = input ('Which one would you like to choose? ')
            print ("You've selected", asian_question, 'Thank you for choosing Chosenmeal')
            quit()
            #break
            
        elif user_question == 'American':
            print ('Here is the selection for', american_file)
            american_question = input ('Which one would you like to choose? ')
            print ("You've selected", american_question, 'Thank you for choosing Chosenmeal')
            quit()       
            #break

        elif user_question == 'Mexican':
            print ('Here is the selection for', mexican_file)
            mexican_question = input ('Which one would you like to choose? ')
            print ("You've selected", mexican_question, 'Thank you for choosing Chosenmeal')
            quit()       
            #break

        elif user_question == 'Comfort food':
            print ('Here is the selection for', comfort_food_file)
            comfort_food_question = input ('Which one would you like to choose? ')
            print ("You've selected", comfort_food_question, 'Thank you for choosing Chosenmeal')
            quit()        
            #break

        elif user_question == 'Healty food':
            print ('Here is the selection for', healthy_food_file)
            healthy_food_question = input ('Which one would you like to choose? ')
            print ("You've selected", healthy_food_question, 'Thank you for choosing Chosenmeal')
            quit()           
            #break

        elif user_question == 'Fast Food':
            print ('Here is the selection for', fast_food_file)
            fast_food_question = input ('Which one would you like to choose? ')
            print ("You've selected", fast_food_question, 'Thank you for choosing Chosenmeal')
            quit()           
            #break

        else:
            print ('Please type the exact word that you see in the given selection')
            continue
    

    elif user_input == 'Y':
        
        for asian_file1 in asian_file:
            asian2 = (asian_file1[1:])
        #print (asian2)

        for american_file1 in american_file:
            american2 = (american_file1[1:])
        #print (american2)

        for mexican_file1 in mexican_file:
            mexican2 = (mexican_file1[1:])
        #print (mexican2)       
            
        for comfort_food1 in comfort_food_file:
            comfort_food2 = (comfort_food1[1:])
        #print (comfort_food2)

        for healthy_food1 in healthy_food_file:
            healthy_food2 = (healthy_food1[1:])
        #print (healthy_food2)        

        for fast_food1 in fast_food_file:
            fast_food2 = (fast_food1[1:])
        #print (fast_food2)        

        import random
        restaurant = [asian2, american2, mexican2, comfort_food2, healthy_food2, fast_food2]
        ABC = (random.sample(restaurant, 1))
        print (ABC)
        print ('The random feature has given you', ABC, 'Thank you for choosing ChosenMean')
        quit()

    else: 
        print ('Please enter the exact letter given in the selection.')
        continue

