#Project 3 Objectives:
#1st Objective: Find how many characters there are in the given sentence.
#2nd Objective: Find how many characters there are in the given word.
#3rd Objective: Find the nth place of the given word within the sentence.
#4th Objective: Use string slice to confirm that the nth position of the word + the numbers of characters in the given word is = to 'jRiv@gmail.com'.
#5th Objective: Find the word 'jRiv@gmail.com' in the string of words and replace it with 'thisisanewemail@gmail.com'
#6th Objective: Find the word 'randomsentence' and capitalize all of it


quote = ("This is all random: !* $@ CC: From who??? - jRiv@gmail.com / 0123456789 (http://www.randomsentence.com)")

#Use len to find the number of characters in the sentence
amount_of_word_in_sentense = len (quote)
print ('1st objective: ',amount_of_word_in_sentense, 'This is how many characters are in this sentence')


#Use counting in loop to find the number of characters in the word
value = 0
word = 'jRiv@gmail.com'
for w in word:
    value = value + 1
print ('2nd objective: ',value, 'This is how many characters are in this word') 



#Use .find to find the nth position of the word
word_position = quote .find ('jRiv@gmail.com')
print ('3rd objective: ','jRiv@gmail.com is in', word_position,'th place')


#Use string slice to confirm that the nth position of the word + the numbers of characters in the given word is = to 'jRiv@gmail.com'.
#Use the position of the word and add the number of the character in the word to confirm that it is equals to 'jRiv@gmail.com'.
string_slice = (quote [44:44+14])
#print ('4th objective: ',string_slice)
if string_slice == 'jRiv@gmail.com':
    print ('4th Objective:  matches')
else:
    print ('No it does not match')


#Use .replace to replace'jRiv@gmail.com' to 'thisisanewemail@gmail.com'
new = string_slice.replace ('jRiv@gmail.com', 'thisisanewemail@gmail.com')
print ('5th objective: ',new)

#Find the word 'randomsentence' and capitalize all of it
x = quote
y = x.find ('randomsentence')
#print (y)
# = 84

value = 0
xx = 'randomsentence' 
for xxx in xx:
    value = value + 1
#print (value)
# = 14

yy = (quote [84:84+14])
print (yy)

capitalize = yy . upper ()
print ('6th objective', capitalize)

quit()
