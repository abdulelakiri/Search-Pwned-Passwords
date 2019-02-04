import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pwhashes"]
mycol = mydb["testcol"]

with open('pwned-passwords-sha1-ordered-by-count-v4-edit.txt', 'r') as inF:
    for line in inF:
        HASH = line.split(':')[0]
        Prevalence = line.split(':')[1]
        mydict = { "Hash": HASH, "Prevalance": Prevalence }
        x = mycol.insert_one(mydict)