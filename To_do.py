
import shelve
import sys
import datetime
import argparse

fileshow = shelve.open("mythings", writeback=True)
list_to_do = []  
update = ''
date = datetime.date.today()
date = date.strftime("%B-%d-%Y -> ")

parser = argparse.ArgumentParser(description="Add To-Do List")
parser.add_argument('-s','--show',action='store_true',help="Displays the task To-Do")
parser.add_argument('-u','--update',action='store_true', help="Update the list To-Do in your current task")
parser.add_argument('-n','--new',action='store_true', help="Re-Creates a new list To-Do")
parser.add_argument('-r','--remove',action='store_true', help="Remove the specific task in list To-Do")
args = parser.parse_args()

if len(sys.argv) < 2:
    print("Usage:python To_do.py [-h]")

if args.update:
    print("Add To-Do List, 'Type exit to stop'")
    while True:
        update = input()
        if update == 'exit':
            break
        update = date + update
        fileshow['list_to_do'].append(update)
    
elif args.show:
    print('')
    print("No   Registered \t Things To Do")
    print(" ".rjust(50,'-'))
    for i in range(len(fileshow['list_to_do'])):
        print("%d - %s" % (i,fileshow['list_to_do'][i]))
        print(" ".rjust(50,'-'))
    sys.exit()        
    
elif args.remove:
    print("Enter Item Number To Remove The From List")
    rem = int(input())
    fileshow['list_to_do'].pop(rem)
    print("Removed..")
    sys.exit()
    
elif args.new:
    print("Welcome To-Do!)")
    print("Add To-Do items.")
    print("If you're done adding type 'exit'")
    
    while True:
        add = input()
        if add == 'exit':
            break
        add = date + add
        list_to_do += [add]
        fileshow['list_to_do'] = list_to_do
        
    fileshow.sync()
    fileshow.close()

      
