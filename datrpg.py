from random import randint as random
import sys

debug = raw_input("Debug?")

if debug == "chglog":

    chglog = open('changelog.txt', 'r') # will supply tomorrow via Google Docs

    chglogcont = chglog.read()

    print (file_contents)

    chglog.close()

# basic local variables
inventory = "knife"
health = 10
enemy = 0
nmecount = 0
    
while True:
    
    input = raw_input("What will you do?")
    
    if input == "inventory":
        print "Inventory:" + str(inventory)
    if input == "health":
        print "Health:" + str(health)
    if input == "attack":
        print "Attacking " + enemy + "!"
        atkinput = raw_input("Will you attack, defend, or check your bag?")
            if atkinput == attack:
                if nmecount > 1:
                    print "."
                    