#objectives: create a mock investment to chosen cryptocurrencies

#Stored username / password
username1 = ('johnr@gmail.com')
password1 = ('Iamawesome123')



print ('Hello, Welcome to CryptoStore')
begin = input ('For Sign In, type: A / For Sign Up, type: B > ')

if begin == ('A'):

    while True:

        sign_in = input ('Please type your Username: ')

        if sign_in == username1:
            print ("Username is correct")

            sign_in_password = input ('Please type your password: ')

            if sign_in_password == password1:
                print ('Password is correct')
                break
            else:
                print ('Password is incorrect, please try again')
                continue

        else:
            print ('Username is incorrect, Please try again')
            continue


    
elif begin == ('B'):
    sign_up_id = input ('Please type your desired username: ')
    sign_up_pass = input ('Please type your desired password: ')
    print ('Thank you')

else:
    print ('Unknown input, please enter according to instruction')
    print ('try again, program will be closing now')
    quit()

intro_question = input ('Would you like to view your investment (Y / N): ')

if intro_question == ('Y'):
    print ('Ok here is your portfolio')

else:
    print ('Ok, Thank you')
    quit()

btc = 100000
eth = 50000
ada = 10000
money = 0

print ('BTC:', btc)
print ('ETH', eth)
print ('ADA', ada)

intro_question = input ('Would you like to invest more or quit: (for invest, press: A / for quit, press: B)> ')

try:
    if intro_question == ('A'):
        investment_question = input ('Which one would you like to invest at (BTC, ETH, or ADA ?)> ')

        if investment_question == ('BTC'):
            amount = input ('How much would you like to invest, (please input according to dollar value): ')
            a = int (amount)
            btc = (btc + a)
            print ('This is your total BTC:', btc)


        elif investment_question == ('ETH'):
            amount = input ('How much would you like to invest, (please input according to dollar value): ')
            a = int (amount)
            eth = (eth + a)
            print ('This is your total ETH:', eth)           

        elif investment_question == ('ADA'):
            amount = input ('How much would you like to invest, (please input according to dollar value): ')
            a = int (amount)
            ada = (ada + a)

            print ('This is your total ADA:', ada)


    else:
        print ('Ok, Goodbye')
        quit()    


except:
    print ('Invalid input, program is exiting now')
    quit ()

totalbtc = ('BTC:', btc)
totaleth = ('ETH:', eth)
totalada = ('ADA:', ada)


investment = [totalbtc, totaleth, totalada]
for i in investment:
    print ('This is the full detail of your investment portfolio', i)

#show if your investment is over $50,000

x = False
cryptocurrencies = [btc, eth, ada]
for c in cryptocurrencies:
    if c > (50000):
        x = True
    print ('Has any of your investment exceeded $50,000:', x, c)

totalinvestment = 0
crypto = [btc, eth, ada]
for c in crypto:
    totalinvestment = totalinvestment + c
    print (totalinvestment, "is the total amount in the dollar value.")
    
lastquestion = input ('Does this complete your transaction, press A for yes / press B for no:> ')

if lastquestion == 'A':
    print ('Thank you')
    quit ()

else:
    print ('This is the end of this program, Thank you')
    quit ()