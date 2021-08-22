#Question and choose your own adventure game.

print ('Hello, welcome to the toughest game on earth')
player = input ('Are you ready to play this game? ')
if player != 'yes':
    quit ()

elif player == 'yes':
    name = input ("Very well, let's begin with your name. What is your name? ")
    print (name, "oh what an interesting name")
    print (name, 'I hope youve prepared yourself, we are now about to start')


quizquestion = input ('Answer this riddle, I walk with 4 limbs in the morning, 2 limbs in the afternoon, and 3 limbs at night. What am i? ')
if quizquestion == 'Human Being':
    print ('You are correct.')
if quizquestion == 'Man':
    print ('You are correct.')
if quizquestion == 'Person':
    print ('You are correct.')