def nursery():
    print("""Jack and Jill went up the hill
To fetch a pail of water.
Jack fell down and broke his crown,
And Jill came tumbling after.

Up Jack got, and home did trot,
As fast as he could caper,
He went to bed to mend his head,
With vinegar and brown paper.""")

def birthday(name):
    print("""Happy Birthday to You
Happy Birthday to You""")
    print("Happy Birthday Dear "+name)
    print("Happy Birthday to You.")

def password():
    import random
    char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","-","_","!","?","/",".","*"]
    num= random.randint(1,1000)
    new=""
    for i in range(num):
        new+= random.choice(char)
    return new
    
print(password())
