import pandas as pd

top5 = pd.read_html ('https://en.wikipedia.org/wiki/Car_of_the_Year#Global')
hc = top5[0]

top_car = hc[['Year', 'World Car of the Year']].head(5)

print ('Listed Below are the top 5 of the "World Car of the Year."')
print (top_car)

class Car:
    def __init__ (self, wonyear ,brand, model, price):
        self.wonyear = wonyear
        self.brand = brand
        self.model = model
        self.price = price

    def car_call (self):
        print (self.wonyear, 'World Car of the Year')
        print ('Vehicle:', self.brand, self.model)
        print ('2022 model: [$]',self.price, 'MSRP')

car1 = Car ('2020', 'Kia', 'Telluride', 32790)
car2 = Car ('2019', 'Jaguar', 'Telluride', 69900)
car3 = Car ('2018', 'Volvo', 'XC60', 49900)
car4 = Car ('2017', 'Jaguar', 'F-Pace', 50900)
car5 = Car ('2016', 'Mazda', 'MX-5', 26830)



while True:
    user_input = input ('Enter the number of the vehicle (0-4) that you would like to look at or (q) to quit: ')


    if user_input == '0':
        car1.car_call()
        continue
    elif user_input == '1':
        car2.car_call()
        continue
    elif user_input == '2':
        car3.car_call()
        continue
    elif user_input == '3':
        car4.car_call()
        continue
    elif user_input == '4':
        car5.car_call()
        continue
    elif user_input == 'q':
        break
    else:
        print ('Unknown input, try again')
        continue

quit()
