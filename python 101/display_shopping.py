##shopping = ["bread", "cheese", "apple", "tomato", "biscuits"]
##count = 0
##
##for item in shopping:
##    print(item)
##    count = count + 1
##
##print(count)
##print(len(shopping))
shopping = []
how_many = input("how many items of shopping do you have? ")
how_many = int(how_many)

for item_number in range(how_many):
    item = input("what is item number " + str(item_number) + "? ")
    shopping.append(item)

print(shopping)
for item in shopping:
    print(item)
    count = count + 1

print(count)
print(len(shopping))
