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

#Conditional Chapter #3
question = input ("what is the capital of Texas? ")
if question == "Austin":
    print ("Good job")

elif question == "austin":
    print ("Good job")

else:
    print ("wrong answer")

#Try and Except Chapter #3
question1 = input ('2 + 2? ')
try:
    answer = int (question1)
except:
    answer = -1

if answer > 1:
    print ('Good job')
else:
    print ("Wrong answer, please enter a numerical value")


#Store and Reuse Chapter #4
question = input ("Hi, What is your name? ")

def welcome ():
    print ("What a strange name")

print (question)
welcome ()

question2 = input ("What is your last name? ")
print (question2)
welcome ()

