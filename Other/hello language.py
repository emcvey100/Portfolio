#hello
print ("hello")
#start loop
start ="yes"
while start !="no":
  lang=input("What language do you want hello in?")
  lang=lang.lower()
  #languages with hello
  if lang=="french":
    print("Bonjour!")
  elif lang=="spanish":
    print("Hola!")
  elif lang=="afrikaans":
    print("Hallo!")
  elif lang=="welsh":
    print("Helo!")
  else:
    print("Sorry not on our system.")
  start=input("Do you want to translate another language? Put no if you do not.")
  start=start.lower()
print("goodbye")