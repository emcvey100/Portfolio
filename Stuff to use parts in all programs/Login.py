import hashlib
from tkinter.ttk import *
from tkinter import *
import mysql.connector
import uuid
import time

def makeSalt():
    salt     = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return salt

def hashpass(mystring):
    hashed= hashlib.md5(mystring.encode())
    hashed=hashed.hexdigest()
    return hashed

def hashit(hashstring,saltpart):
    hashpass(hashstring)
    part = hashlib.sha512()
    part.update(hashstring+saltpart)
    hashed =  base64.urlsafe_b64encode(part.digest())
    return hashed

def connect2database():
    connect = mysql.connector.connect(host='db4free.net',
                                         database='computerscience',
                                         user='computerscience',
                                         password='@YWf6iWTtijx79E')
    return connect

def connectorCursor(connection):
    database_cusor = connection.cursor()
    return database_cusor

def createTableUsers():
    conn = connect2database()
    cursor = connectorCursor(conn)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
                        username varchar(30) PRIMARY KEY     NOT NULL,
                        hashedpass text NOT NULL,
                        salt text NOT NULL,
                        passmonth char(2) NOT NULL,
                        passyear char(4) NOT NULL,
                        passday char(2) NOT NULL,)""")
    cursor.commit()
    conn.close()

def selectpass(given_username):
    conn = connect2database()
    cursor = connectorCursor(conn)
    password=cursor.execute('''SELECT hashedpass
                            from Users
                            where username=?''',(given_username))
    conn.close()
    return password

def selectsalt(given_username):
    conn = connect2database()
    cursor = connectorCursor(conn)
    salt=cursor.execute('''SELECT salt
                            from Users
                            where username=?''',(given_username))
    conn.close()
    return salt

def selectpassday(given_username):
    conn = connect2database()
    cursor = connectorCursor(conn)
    date=cursor.execute('''SELECT passday
                            from Users
                            where username=?''',(given_username))
    conn.close()
    return int(date)

def selectpassmonth(given_username):
    conn = connect2database()
    cursor = connectorCursor(conn)
    date=cursor.execute('''SELECT passmonth
                            from Users
                            where username=?''',(given_username))
    conn.close()
    
    return int(date)

def selectpassyear(given_username):
    conn = connect2database()
    cursor = connectorCursor(conn)
    date=cursor.execute('''SELECT passyear
                            from Users
                            where username=?''',(given_username))
    conn.close()
    return int(date)

def changepasswords():
    #on change passwords section
    pass

login = Tk()
logo=Frame(login)

photo = PhotoImage(file = "emoji.png")
#login.configure(bg = 'pink')
login.geometry("300x350")
login.wm_title("Login")

login.iconphoto(False, photo)
image = PhotoImage(file = "emoji.png")
img = image.subsample(15, 15)
imglable=Label(logo, image = img)
title=Label(logo, text="Name title", fg="Black", font=("Garamond", 35))
inputs=Frame(login)
def checkPasswords(username, password):
    salt = selectsalt(username)
    real_password = selectpass(username)
    if hashit(password,salt) == real_password:
        changepasswords(username, password)
    else:
        inncorect=Label(logo, text="This login is incorrect!", fg="Red", font=("Garamond", 20))
        inncorect.pack()
user=Label(inputs, text="Username:", fg="Black", font=("Garamond",15))
userenter=Entry(inputs, show=None, fg="Black", font=("Garamond",15))

passw=Label(inputs, text="Password:", fg="Black", font=("Garamond",15))
passenter=Entry(inputs, show="*", fg="Black", font=("Garamond",15))
def check():
    username=userenter.get()
    password=passenter.get()
    checkPasswords(username, password)
go=Button(inputs, text="Next", command=check)

logo.pack()
imglable.pack()
title.pack()
inputs.pack()
user.pack()
userenter.pack()
passw.pack()
passenter.pack()
go.pack()

login.mainloop()



###place
#logo
#imglable
#title
#inputs
#user
#userenter
#passw
#passenter
#go


