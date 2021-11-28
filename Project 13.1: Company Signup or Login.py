import re

#stored ID and Password
def login ():
    login01 = 'john.aldrin@gmail.com'
    return login01
x = login ()

def password ():
    password1 = "Aldrin12345"
    return password1
y = password ()


#print ("State Farm")
print ('Company A')



while True:

    question1 = input ('(1) for Login, (2) for Signup: ')
    print (' ')


    if question1 == ('2'):
        signup1 = input ('Create your username: ')
        print (' ')

        print ('The password must consists of 10 characters')
        print ("The password must consists of some numbers")
        print ("The password must consists of some capital letters")
        print ('The password must consists of some symbols')


#parameters for the password
        while True:

            signup2 = input ('Enter password: ')

            if len (signup2) < 10:
                print ("The password must consists of 10 characters.")

            elif re.search ('[0-9]', signup2) is None:
                print ("The password must consists of some numbers.")

            elif re.search ('[A-Z]', signup2) is None:
                print ("The password must consists of some capital letters.")

            elif re.search ('[!@#$%^&*]', signup2) is None:
                print ('The password must consists of some symbols.')
            else:
                print("ID and Password successfully created")
                break
        
        print (' ')

        signup3 = input ('Please reenter your username: ')
        if signup3 == signup1:
            print ('User ID matches')
            print (' ')

        signup4 = input ('Please reenter your password: ')
        if signup4 == signup2:
            print ('Password matches')
            print (' ')

        
        print ("Account successfully created")
        print ('Sign in to access your account')
        print (' ')
        continue


    elif question1 == ('1'):


        print (' ')
        print ("Log in to view and manage your account")

#Choose from either stored ID and Pass or newly created ID and Pass
        while True:

            login2 = input ("User ID: ")
            if login2 == x or signup3:
                print ('Correct ID')
                print (' ')
        

            elif login2 != x or signup3:
                print ('Incorrect ID, Try again')
                print (' ')
                continue


            password2 = input ("Password: ")
            if password2 == y or signup4:
                print ('Correct Password')
                print (' ')
                break

            elif password2 != y or signup4:
                print ('Incorrect Password, Try again')
                print (' ')
                continue

            break

        break

    

