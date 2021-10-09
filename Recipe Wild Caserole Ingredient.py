file_name = input ('Please enter the name of the file: ')
file_open = open (file_name)

question1 = input ('Hello user, what would you like to do? type (X) to view the ingredients or (Y) to view the steps: ')


file_list = list()
if question1 == 'X':
    print ("You've chosen to view the ingredients")
    for file1 in file_open:
        file1 = file1.rstrip()
        if not file1.startswith ('Ingredient:'):
            continue
        print (file1)
        #else:
            #file1 = file1.split()
            #file_list.append (file1[2:])
            #print (file_list)






#elif question1 == 'Y':
#    print ("You've chosen to view the steps")
