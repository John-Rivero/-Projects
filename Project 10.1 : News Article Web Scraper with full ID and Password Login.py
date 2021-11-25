#Go to 'THE VERGE.COM'for the URL

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

cert_none = ssl.create_default_context()
cert_none.check_hostname = False
cert_none.verify_mode = ssl.CERT_NONE


login = input ('Create A Username:  ')
password = input ('Create A Password:  ')


#loop for login and password
while True:

    login2 = input ('Please enter your created username: ')
    if login2 == login:
        print ('Username matches')
        break

    elif login2 != login:
        print ('Username does not match, try again.')
        continue


while True:

    password2 = input ('Plase enter your created password ')
    if password2 == password:
        print ('Password matches')
        break

    elif password2 != password:
        print ('Password does not match, try again.')
        continue


print ('Welcome to The Verge Article Scraper.')


#scraper
url = input ('Enter the url of the website: ')
html = urllib.request.urlopen (url, context=cert_none).read()
soup = BeautifulSoup (html, 'lxml')





while True:

    question1 = print ('What data would you like to scrape.')
    title1 = print ("'Title', for the Article's Title.")
    date_published1 = print ('"Date", for date when the article was published.')
    author1 = print ('"Author", for the name of the Author.')
    author_social1 = print ("'Social', for the Author's social media.")
    article1 = print ('"Article", for the entire article.')
    all = print ('"All", for all the data mentioned above. ')

    answer = input ('-')


    #loop for the title
    if answer == ('Title'):

        try:

            title = soup.find ('div', class_='c-entry-hero__header-wrap').h1.text
            print ('ARTICLE TITLE:    ', title)
            x = input ('Are you finished with this program? Y or N: ')

            if x == ('Y'):
                print ('Thank you for using this program. Goodbye for now.')
                quit()

            elif x == ('N'):
                continue

        except:
            print ('ARTICLE TITLE: No data for this section')
            continue


    #loop for date when the article was published
    elif answer == ('Date'):

        try:

            date_published = soup.find ('time', class_='c-byline__item').text
            print ('PUBLISHED DATE:    ', date_published)
            x = input ('Are you finished with this program? Y or N: ')

            if x == ('Y'):
                print ('Thank you for using this program. Goodbye for now.')
                quit()

            elif x == ('N'):
                continue

        except:
            print ('PUBLISHED DATE: No data for this section')
            continue


    #loop for the author
    elif answer == ('Author'):

        try:

            author = soup.find ('span', class_='c-byline__author-name').text
            print ('AUTHOR:    ', author)
            x = input ('Are you finished with this program? Y or N: ')

            if x == ('Y'):
                print ('Thank you for using this program. Goodbye for now.')
                quit()

            elif x == ('N'):
                continue

        except:
            print ('AUTHOR: No data for this section')
            continue


    #loop for the author's social media
    elif answer == ('Social'):

        try:

            author_social = soup.find ('a', class_='c-byline__twitter-handle').text
            print ('AUTHOR SOCIAL MEDIA:    ', author_social)
            x = input ('Are you finished with this program? Y or N: ')
            if x == ('Y'):
                print ('Thank you for using this program. Goodbye for now.')
                quit()

            elif x == ('N'):
                continue

        except:
            print ('No data for this section')
            continue


    #loop for the main article
    elif answer == ('AUTHOR SOCIAL MEDIA: Article'):

        try:

            article = soup.find ('div', class_='c-entry-content').text
            print ('ARTICLE:    ',article.rstrip())
            x = input ('Are you finished with this program? Y or N: ')
            if x == ('Y'):
                print ('Thank you for using this program. Goodbye for now.')
                quit()

            elif x == ('N'):
                continue

        except:
            print ('ARTICLE: No data for this section')
            continue          


    #loop to print all data at once
    elif answer == ('All'):

        try:
            title = soup.find ('div', class_='c-entry-hero__header-wrap').h1.text
            print ('ARTICLE TITLE:    ', title)            
        except:
            print ('ARTICLE TITLE: No data for this section')

        try:
            date_published = soup.find ('time', class_='c-byline__item').text
            print ('PUBLISHED DATE:    ', date_published)
        except:
            print ('PUBLISHED DATE: No data for this section')

        try:
            author = soup.find ('span', class_='c-byline__author-name').text
            print ('AUTHOR:    ', author)
        except:
            print ('AUTHOR: No data for this section')

        try:
            author_social = soup.find ('a', class_='c-byline__twitter-handle').text            
            print ('AUTHOR SOCIAL MEDIA:    ', author_social)
        except:
            print ('AUTHOR SOCIAL MEDIA: No data for this section')

        try:
            article = soup.find ('div', class_='c-entry-content').text
            print ('ARTICLE:    ',article.rstrip())
        except:
            print ('ARTICLE: No data for this section')            

        x = input ('Are you finished with this program? Y or N: ')
        if x == ('Y'):
            print ('Thank you for using this program. Goodbye for now.')
            quit()

        elif x == ('N'):
            continue


    else:
        print ('Incorrect input, Try again!')
        continue
