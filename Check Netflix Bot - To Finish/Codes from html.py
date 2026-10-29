with open("films.txt") as f:
    data = f.read()
netflix=[]
i = 0
while True:
    x = data.find('<a href="/watch')
    if x == -1 or x == "-1":
        break
    else:
        data = data[x:]
        x = data.find("/watch/")
        number = data[x+7:x+15]
        x = data.find('aria-label=')
        y = data.find('" tabindex="0" aria-hidden="false" class="slider-refocus">')
        title = data[x+12:y]
        data=data[y:]
        row = [number, title]
        print(row)
        netflix.append(row)
    i+=1
import csv
with open('Netflix_Codes_UK_films.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(netflix)
print("done")
with open("Tv series.txt") as f:
    data = f.read()
netflix=[]
i = 0
while True:
    x = data.find('<a href="/watch')
    if x == -1 or x == "-1":
        break
    else:
        data = data[x:]
        x = data.find("/watch/")
        number = data[x+7:x+15]
        x = data.find('aria-label=')
        y = data.find('" tabindex="0" aria-hidden="false" class="slider-refocus">')
        title = data[x+12:y]
        data=data[y:]
        row = [number, title]
        print(row)
        netflix.append(row)
    i+=1
with open('Netflix_Codes_UK_TV.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(netflix)
print("done")
