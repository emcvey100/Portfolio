my_list = ['apple', 'banana', 'pear']
my_string = 'fig'

for item in my_list:
	print(item)
	
for item in my_string:
	print(item)

topic = "slicing strings"

print(topic[:3])
print(topic[5:])
print(topic[2:12])

teams = ["WOLVES", "OWLS", "PANTHERS", "BEARS", "DRAGONS"]
abrteams=[]
for i in teams:
    n=i[:3]
    abrteams.append(n)
print(abrteams)
