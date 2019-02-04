
import pymongo
import time
import csv

#connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pwhashes"]
mycol = mydb["passwordhash"]
hashlist = open('hashpwlist.csv', 'r')
#passwordcheck function

start = time.time()
compaccounts = []
with hashlist:
    reader = csv.reader(hashlist)
    for row in reader:
        Hash = row[1]

        #query database for same hash
        myquery = {"Hash": Hash}
        mydoc = mycol.find(myquery)

        #set X to None to satisfy if condition
        x = None
        for x in mydoc:
            x
        if x is not None:
            compaccounts.append(int(row[0]))
            print("Account Compromised: " + row[0] + "      Password Hash: " + row[1])

end = time.time()
total = (end - start)
print("This test took: {}s".format(total) + " or {}ms".format(total*1000))
print(compaccounts)