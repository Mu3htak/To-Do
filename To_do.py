
import shelve
import sys
import datetime

fileshow = shelve.open("mythings", writeback=True)
list_to_do = []  
update = ''
date = datetime.date.today()
date = date.strftime("%B-%d-%Y -> ")

try:
    if sys.argv[1] == 'update':
        print("Add To-Do List, 'Type exit to stop'")
        while True:
            update = input()
            if update == 'exit':
                break
            update = date + update
            fileshow['list_to_do'].append(update)
       # print(fileshow['list_to_do'])
    
    elif sys.argv[1] == 'show':
        print('')
        #print("Things to Do".center(46, '-'))
        print("No   Registered \t Things To Do")
        print(" ".rjust(50,'-'))
        for i in range(len(fileshow['list_to_do'])):
            print("%d - %s" % (i,fileshow['list_to_do'][i]))
            print(" ".rjust(50,'-'))
        sys.exit()        
    
    elif sys.argv[1] == 'remove':
        print("Enter Item Number To Remove The From List")
        rem = int(input())
        fileshow['list_to_do'].pop(rem)
        print("Removed..")
        sys.exit()
    
    elif sys.argv[1] == 'new':
        print("Welcome To-Do!, Mushtak :)")
        print("Add To-Do items.")
        print("If you're done adding type 'exit'")
    
        while True:
            add = input()
            if add == 'exit':
                break
            add = date + add
            list_to_do += [add]
            fileshow['list_to_do'] = list_to_do
    else:
        print("Invalid argument!")
        print("Usage: python To_do.py [show] [update] [new] [remove]")
    fileshow.sync()
    fileshow.close()
        
except IndexError:
    if len(sys.argv) < 2:
        print("Usage: python To_do.py [show] [update] [new] [remove]")
      
