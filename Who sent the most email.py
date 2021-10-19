#Find the "Sent by" to identify the names of the senders and print all the names who sent the emails
#Find the person who sent the most email. 

file_input = input ('Please enter the name of the file: ')
file_open = open (file_input)

file_dict = dict ()

for file in file_open:
    if not file.startswith ('Sent by'):
        continue
    file = file.rstrip ()
    file = file.split ()
    file = file [2]
    #print (file)
    
    file_dict [file] = file_dict.get (file, 0) + 1
    #print (file_dict)



for (word, count) in file_dict.items():
    print (word,'sent', count, 'emails.')


xword = None
ycount = None
for (word, count) in file_dict.items ():
    if ycount is None or ycount < count:
        ycount = count
        xword = word
print (xword,'sent the most emails.', 'A total of', ycount, 'emails.')
