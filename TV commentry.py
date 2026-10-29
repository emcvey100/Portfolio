#Write a progam that:
#-asks the user how long on average they spend watching TV each day
#-if it is less than 2 hours, outputs 'That shouldn't rot your brain too much'; if it is less than 4 hours per day, outputs 'Aren't you getting square eyes?', otherwise outputs 'Fresh air beats channel flicking'

#asks user hours of tv watched
hours_of_TV_watched = int(input("Hours watching TV per day:"))
#if it is less than 2 hours, outputs 'That shouldn't rot your brain too much'; if it is less than 4 hours per day, outputs 'Aren't you getting square eyes?', otherwise outputs 'Fresh air beats channel flicking'
if hours_of_TV_watched < 2:
    print("That shouldn't rot your brain too much")
elif hours_of_TV_watched < 4:
    print("Aren't you getting square eyes?")
else:
    print("Fresh air beats channel flicking")
