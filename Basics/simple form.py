#Write a sign-up program for an after-school club; it should ask the user for the following details and store them in a file:
#-First Name
#-Last Name
#-Gender
#-Form

#inputs
f_name = input("First name:")
l_name = input("Last name:")
gender = input("Gender:")
form = input("Form:")
#outputs
file = open("sign_up.txt", "a")
file.write("\nFirst name: "+f_name+", Last name: "+l_name+", Gender: "+gender+", Form: "+form)
file.close()
