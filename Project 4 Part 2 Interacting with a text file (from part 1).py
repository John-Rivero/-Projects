#Project 4: Interact with file name ('number4.txt')
#Objective 1: Open and print out  the selected file. Make sure to remove all spaces in between the paragraphs
#Objective 2: Count how many lines are in the file
#Objective 3: Count how many characters there are in the file
#Objective 4: Find what nth position and print the entire line for 'Received1992:'
#Objective 5: Find what nth position and print the entire line for 'To1992:'
#Objective 6: Change the first half of the file to upper case
#Objective 7: Change the last half of the file to lower case
#Objective 8: Find 'John Rivero' and say what nth place it is.  Calculate the amount of characters in 'John Rivero'. Reprint using slicing strings.
#Objective 9: Find 'johnr@gmail.com' and tell how many characters and in what nth position in the file


openfile = open ('number4.txt', 'r')
print (openfile)



open_file = open ('number4.txt') #Objective 1: Open and print out  the selected file. Make sure to remove all spaces in between the paragraphs
for open1 in open_file:
    open1 = open1.rstrip() #use rstrip to remove all the spaces between the paragraph.
    print (open1)



open_file = open ('number4.txt')#Objective 2: Count how many lines are in the file
value = 0
for open1 in open_file:
    value = value + 1
print ('This number of lines in the file:', value)



open_file = open ('number4.txt')#Objective 3: Count how many characters there are in the file
open1 = open_file.read()
open1 = len(open1) #use len() to count the characters in the file
print ('The number of characters in the file:', open1)



file_open = open ('number4.txt') #Objective 4: Find what nth position and print the entire line for 'Received1992:'
for file_open_1 in file_open:
    file_open_1 = file_open_1.rstrip()
    if not file_open_1.startswith ('Received1992:'):
        continue
    print (file_open_1)



file_open = open ('number4.txt') #Objective 5: Find what nth position and print the entire line for 'To1992:'
for file1 in file_open:
    file1 = file1.rstrip()
    if not file1.startswith ('To1992:'):
        continue
    print (file1)



file_open = open ('number4.txt') #Objective 6: Change the first half of the file to upper case
open1 = file_open.read()
open1 = open1[0:3913]
open1 = open1.rstrip()
open1 = open1.upper()
print (open1)



file_open = open ('number4.txt') #Objective 7: Change the last half of the file to lower case
open1 = file_open.read()
open1 = open1[3913:]
open1 = open1.rstrip()
open1 = open1.lower()
print (open1)



file_open = open ('number4.txt') #Objective 8: Find 'John Rivero' and say what nth place it is.  Calculate the amount of characters in 'John Rivero'. Reprint using slicing strings.
open1 = file_open.read()
open1 = open1.find ('John Rivero')
print ('John Rivero starts at',open1, 'th place')

word = ('John Rivero')
word = len (word)
print ('John Rivero has',word, 'words')

file_open = open ('number4.txt')
open1 = file_open.read()
print (open1[279:279+11])



file_open = open ('number4.txt') #Objective 9: Find 'johnr@gmail.com' and tell how many characters and in what nth position in the file
open1 = file_open.read()
open1 = open1.find ('johnr@gmail.com')
print ('johnr@gmail.com starts at:',open1, 'th position')

word = ('johnr@gmail.com')
word = len (word)
print('johnr@gmail.com has',word, 'words')

file_open = open ('number4.txt')
open1 = file_open.read()
print (open1[303:303+15])


question = input ('Does this complete your project? ')
if question == 'yes':
    print ('Ok, Thank you')
    quit ()

else:
    print ('This program will self quit')
    quit()