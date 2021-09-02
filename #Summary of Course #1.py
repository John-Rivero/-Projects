#Summary of Course #1

#print text
print ('Hello, welcome to my program')

#conversion Chapter #2
question = input ("What is 1+1? ")
answer = float (question)
print (answer)

question = input ("What is the value of 4.0 + 1.0? " )
answer =  int(float(question))
if answer == '5':
    print ("Correct")
else:
    print ('Not Correct')

a = '123'
b = int (a)
question = input (b + 1)
print (question)

#---------------------------------------------------------------------------------

#**********Chapter 3**************

#Conditional 
question = input ("what is the capital of Texas? ")
if question == "Austin":
    print ("Good job")

elif question == "austin":
    print ("Good job")

else:
    print ("wrong answer")


#Try and Except 
question1 = input ('2 + 2? ')
try:
    answer = int (question1)
except:
    answer = -1

if answer > 1:
    print ('Good job')
else:
    print ("Wrong answer, please enter a numerical value")

#---------------------------------------------------------------------------------

#**********Chapter 4**************

#Store and Reuse 
question = input ("Hi, What is your name? ")

def welcome ():
    print ("What a strange name")

print (question)
welcome ()

question2 = input ("What is your last name? ")
print (question2)
welcome ()

#----------------------------------------------------------------------------------



#*********Chapter 5***********


#Repeated Steps 
n = 10
while n > 0:
    print (n)
    n = n -2 
print ('Blastoff!')
print (n)

#An Infinite Loop 
#n = 5
#while n > 0:
#    print ('Lather')
#    print ('Rinse')
#print ('Dry OFf')

#No Loop 
#n = 0
#while n > 0: 
#    print ('Lather')
#    print ('Rinse')
#print ('Dry Off')

#Breaking Out of a Loop 
while True:
    line = input ('> ')
    if line == 'done':
        break
    print (line)
print ('Done')

#Finishing an Iteration with Continue 
while True:
    line = input ('> ')
    if line [0] == '#' :
        continue
    if line == 'done' :
        break
    print (line)
print ('Done! ')

#Simple Definite Loop
for i in [5, 4, 3, 2, 1] :
    print (i)
print ('Blastoff')


friends = ['John', 'Karlene']
for friend in friends:
    print ('Merry Christmas:', friend)
print ('Done')

#Counting in a loop
zork = 0
print ('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print (zork, thing)
print ('After, zork')

#Summing in a Loop
zork = 0
print ('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print (zork, thing)
print ('After, zork')

#Finding the Average in a Loop
count = 0
sum = 0
print ('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print (count, sum, value)
print ('After', count, sum, sum/count)

#Filtering in a Loop
print ('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print ('Large number', value)
    print ('After')


#Searh Using a Boolean Varaiable
found = False
print ('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print (found, value)
print ('After', found)

#How to find the largest value
largest_so_far = -1
print ('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print (largest_so_far, the_num)
print ("After", largest_so_far)


#How to find the smallest value
smallest = None
print ('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print ('After', smallest)













largest = None
smallest = None

while True:
    
    try:
        num = input ("Enter a number: ")
        if num == 'done':
            break
        n = int (num)
        
        if largest is None or n > largest:
            largest = n
            
        elif smallest is None or n < smallest:
            smallest = n

    except:
        print ("Invalid input")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
