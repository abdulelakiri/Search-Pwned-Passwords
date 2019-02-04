import getpass
import hashlib
import pymongo
import os
import time

#connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pwhashes"]
mycol = mydb["passwordhash"]

#passwordcheck function
def passwordcheck():
    os.system('cls')  # For Windows

    #Ask for Password
    print('Please type your password and press enter')
    password = getpass.getpass()
    start = time.time()

    #Hash Password
    SHA1_pass = hashlib.sha1(password.encode('utf-8'))
    SHA1_done = SHA1_pass.hexdigest().upper()

    os.system('cls')
    print(SHA1_done)
    #query function
    def check():
        #query database for same hash
        myquery = {"Hash": SHA1_done}
        mydoc = mycol.find(myquery)

        #set X to None to satisfy if condition
        x = None
        for x in mydoc:
            x
        end = time.time()
        total = (end - start)
        if x is None:
            print("Good News Everyone !!!")
            print("There is nothing in the database")
            print("This test took: {}s".format(total))
        else:
            print("Bad News, found matching Hash: {}".format(x.get("Hash")))
            print("Number of times your password appeared is: {}".format(x.get("Prevalance")))
            print("You should probably change it :)")
            print("This test took: {}s".format(total))
    check()
checknext = "y"
while checknext == "y":
    passwordcheck()
    print("Would you like to check another one? [y/n]")
    checknext = input()