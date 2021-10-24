#XTractor the email and phone number extractor

name = input ('Please enter your name: ')
print ('Hello', name, ", welcome to XTractor. ")
file_input = input ('Please enter the name of the file: ')
file_open = open (file_input)

import re

while True:

    question = input ('What would you like to extract, (X) for emails or (Y) for phone numbers, (Z) for quit: ')

    if question == ('X'): #extract emails
        print ('You have chosen to extract emails')

        for file in file_open:
            x1 = re.findall ('\w.*@.*', file)
            for x2 in x1:
                print (x2)

        continue



    elif question == ('Y'): #extract phone numbers
        print ('You have chosen to extract phone numbers')

        for file in file_open:
            x1 = re.findall ('\d.*[-]\d.*', file)
            for x2 in x1:
                print (x2)
                
        continue


    else:
        print ('The program will now be shutting off, thank you for using XTractor')
        quit ()
