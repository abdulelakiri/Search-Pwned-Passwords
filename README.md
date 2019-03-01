# Search-Pwned-Passwords (Rainbow table from HaveIBeenPwned)

Python Search tool that queries a MongoDB database populated with compromised passwords from HaveIBeenPwned.com.
To use this tool, you will need to download the SHA1 list of pwned passwords from https://haveibeenpwned.com/Passwords.

This repository contains the following scripts:

    1. check pwhash.py - This script will search for a matching password by searching through thetext file containing
    the list of passwords. Using this method to search for a matching password will take a while for each search.
     
    2. movetodb.py - This script will populate a MongoDB database with the passwords in the text file. It may take a
    2-3 days to populate the database with passwords from the list since it contains about 551 million passwords (at
    the time of writing this)
    
    3. checkhashfromdb.py - This script will search for a password by querying the MongoDB database. Make sure to 
    index the database to significantly reduce the time it takes to query ( from ~10 mins to less than 0.06 s ).
    
    4. comparecsvhashlist.py - this script will take in a list of passwords in a csv file and report which password 
    and corresponding user is compromised.

Other files included:
    
    1. test movetodb.py - test script to populate mongoDB database.
    2. pw.txt - just a list of plaintext passwords accompanied with the hash value and pwned status.
    3. hashpwlist - hashes of passwords from pw.txt assigned to userid
    4. pwned-passwords-sha1-ordered-by-count-v4-edit - sample hashed passwords list for testing.
  
