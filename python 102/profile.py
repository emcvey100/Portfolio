am = "Good Morning"
pm = "Good Evening"

def get_profile(msg):

    print (msg)
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ")
    age = int(input("What is your age? "))

    return firstname, lastname, age

#Function called passing in variable from global scope
fname,lname,user_age = get_profile(am)
