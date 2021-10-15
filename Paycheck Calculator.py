#Employee 1: John (pay rate = $15) 
#Employee 2: David (pay rate = $20)
#Employee 3: Kyle (pay rate = $30)

def payment (hrs, rte):

    if hrs > 40:
        pay = (40 * rte + ( hrs - 40 ) * rte * 1.5)

    elif hrs < 40:
        pay = (hrs * rte)

    return pay

while True:
    print ("Enter the employee's name or type 'done' if you are finished")    
    name = input ('Please enter the name of the employee: ')


    if name == 'John':
        print ('You have chosen', name)

        monday = input ('Please enter how many hours this employee worked for Monday: ')
        mon = float (monday)
        tuesday = input ('Please enter how many hours this employee worked for Tuesday: ')
        tue = float (tuesday)
        wednesday = input ('Please enter how many hours this employee worked for Wednesday: ')
        wed = float (wednesday)
        thursday = input ('Please enter how many hours this employee worked for Thursday: ')
        thur = float (thursday)
        friday = input ('Please enter how many hours this employee worked for Friday: ')
        fri = float (friday)

        hrs = (mon + tue + wed + thur + fri)
        rte = 15

        x = payment (hrs, rte)
        print ('Paycheck amount for this week: $', x)  #print the total paycheck

        largest = None
        smallest = None

        while True:
            x_value = [mon, tue, wed, thur, fri]
            for x in x_value:

                if largest is None or x > largest:
                    largest = x

                elif smallest is None or x < smallest:
                    smallest = x

            print ('This is the maximum of hours worked for this week', largest)
            print ('This is the minimum of hours worked for this week', smallest)
            break
        
        continue


    if name == 'David':
        print ('You have chosen', name)

        monday = input ('Please enter how many hours this employee worked for Monday: ')
        mon = float (monday)
        tuesday = input ('Please enter how many hours this employee worked for Tuesday: ')
        tue = float (tuesday)
        wednesday = input ('Please enter how many hours this employee worked for Wednesday: ')
        wed = float (wednesday)
        thursday = input ('Please enter how many hours this employee worked for Thursday: ')
        thur = float (thursday)
        friday = input ('Please enter how many hours this employee worked for Friday: ')
        fri = float (friday)

        hrs = (mon + tue + wed + thur + fri)
        rte = 20

        x = payment (hrs, rte)
        print ('Paycheck amount for this week: $', x)  #print the total paycheck

        largest = None
        smallest = None

        while True:
            x_value = [mon, tue, wed, thur, fri]
            for x in x_value:

                if largest is None or x > largest:
                    largest = x

                elif smallest is None or x < smallest:
                    smallest = x

            print ('This is the maximum of hours worked for this week', largest)
            print ('This is the minimum of hours worked for this week', smallest)
            break
        
        continue


    if name == 'Kyle':
        print ('You have chosen', name)

        monday = input ('Please enter how many hours this employee worked for Monday: ')
        mon = float (monday)
        tuesday = input ('Please enter how many hours this employee worked for Tuesday: ')
        tue = float (tuesday)
        wednesday = input ('Please enter how many hours this employee worked for Wednesday: ')
        wed = float (wednesday)
        thursday = input ('Please enter how many hours this employee worked for Thursday: ')
        thur = float (thursday)
        friday = input ('Please enter how many hours this employee worked for Friday: ')
        fri = float (friday)

        hrs = (mon + tue + wed + thur + fri)
        rte = 30

        x = payment (hrs, rte)
        print ('Paycheck amount for this week: $', x)  #print the total paycheck

        largest = None
        smallest = None

        while True:
            x_value = [mon, tue, wed, thur, fri]
            for x in x_value:

                if largest is None or x > largest:
                    largest = x

                elif smallest is None or x < smallest:
                    smallest = x

            print ('This is the maximum of hours worked for this week', largest)
            print ('This is the minimum of hours worked for this week', smallest)
            break
        
        continue


    else:
        print ('You have indicated that you are done with the program, the program is now shutting off, Thank you.')
        quit ()