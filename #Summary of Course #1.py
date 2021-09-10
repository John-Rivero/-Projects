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
value = 0
numbers = [4, 123, 543, 325]
for n in numbers:
    value = value + 1
    print (value, n)
print ('success')

value = 0
numbers = [9, 8, 6, 43, 2]
for n in numbers:
    value = value + 1
    print (value, n)
print ('done')

#Summing in a Loop
value = 0
numbers = [123, 5435, 123, 6546]
for n in numbers:
    value = (value + n)
    print (value, n)
print ('done')


values = 0
numbers = [5, 2, 4, 6, 7]
for n in numbers:
    values = (values + n)
    print (values , n)

number = 0
numbers = [4, 2, 5, 67, 2]
for n in numbers:
    number = (number + n)
    print (number, n)
print ('done')

#Finding the Average in a Loop
value = 0
values = 0
numbers = [123, 6456, 2343, 656]
for n in numbers:
    value = values + 1
    values = values + n
    print (values / value)
print ('done')


x = 0
y = 0
numbers = [1, 4, 5 ,2 ,6]
for n in numbers:
    x = x + 1
    y = x + n
    print ( y / x )

#Filtering in a Loop
numbers = [124, 43543, 1234, 6543]
for n in numbers:
    if n > 1000:
        print (n)
print ('success')


y = [100, 200, 400, 500]
for n in y:
    if n < 400:
        print (n)


#Searh Using a Boolean Varaiable
x = False
number = [ 1, 2, 5, 7, 43, 3]
for n in number:
    if n == 7:
        x = True
    print (x, number)

check = False
names = ['John', 'Karlene', 'Kiana', 'Derill', 'Ashley']
for n in names:
    if n == 'Karlene':
        check = True
    print (x, n)

#How to find the largest value
largestvalue = 0
number = [2, 3, 534, 123, 5434, 123]
for n in number:
    if n > largestvalue:
        largestvalue =  n
    print (largestvalue, n)


#How to find the smallest value
smallest = None
number = [123, 32423, 12321, 1, 4]
for n in number:
   if smallest is None:
      smallest = n

   elif n < smallest:
      smallest = n

   print (smallest, n)












price = 50
while price > 10:
    print (price)
    price = price -5
print (price)


while True:
    number = input ("Please Enter Number: ")
    if number == '0':
        break
    print (number)
print ('Thank You')


while True:
    names = input ('Please Enter Names: ')
    if names == 'restart':
        continue
    elif names == 'done':
        break
    print (names)
print ('Thank you')


























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
