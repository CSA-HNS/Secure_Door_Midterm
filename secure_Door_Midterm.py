import uuid
import passlib
from passlib.hash import pbkdf2_sha256
import time
from subprocess import call

files =open('logins_file.txt')
grades = [x.strip() for x in files.readlines()] #gets encrypted username/password from file and stores as list
lastget = grades[-1] #gets the last encrypted username/password in list to check when to break for loop below
lastentry = lastget.split(',') #splits username and password

def check_password(encrypted_password, entered_password):
    test1=pbkdf2_sha256.verify(entered_password,encrypted_password)
    return test1

def check_username(encrypted_username, entered_username):
    test2 = pbkdf2_sha256.verify(entered_username, encrypted_username)
    return test2

usern = input("Please enter your User ID: ")
passw = input("Please enter your PIN number: ")
for x in grades:
    logins = x.split(',')

    if check_username(logins[0], usern): #checks username
        if check_password(logins[1], passw): #checks password
            print('Logged in!')
            mytime = time.ctime(time.time())  # my time
            timefile = (usern+" logged in on "+str(mytime))
            outfile = open("loghistory.txt", "a")
            outfile.write(timefile+'\n')
            outfile.close()
            call(["python", "open.py"])
            break
        elif logins[1] == lastentry[1]: #checks to see if password last in list if password wrong, to see if for loop should check next one(if there is one)
            print('Incorrect Login! ')
            mytime2 = time.ctime(time.time())  # my time
            timefile2 = (usern + " attempted to log in on " + str(mytime2))
            outfile2 = open("loghistory.txt", "a")
            outfile2.write(timefile2 + '\n')
            outfile2.close()
            break
        else:
            pass

    elif logins[0] == lastentry[0]: #checks to see if username last in list if username wrong, to see if for loop should check next one(if there is one)
        print('Incorrect Login! ')
        mytime2 = time.ctime(time.time())  # my time
        timefile2 = (usern+" attempted to log in on "+str(mytime2))
        outfile2 = open("logfiles.txt", "a")
        outfile2.write(timefile2+'\n')
        outfile2.close()
        break
    else:
        pass