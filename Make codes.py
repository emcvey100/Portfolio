from urllib.request import urlopen
netflix=[]
for one in range(10):
    for two in range(10):
        for three in range(10):
            for four in range(10):
                for five in range(10):
                    for six in range(10):
                        for seven in range(10):
                            for eight in range(10):
                                code = str(one)+ str(two) + str(three) + str(four) + str(five) + str(six) + str(seven) + str(eight)
                                url = 'https://www.netflix.com/browse?jbv=' + code
                                try:
                                    data = urlopen(url).read()
                                    data=str(data)
                                    x=data.find("<title>")
                                    y=data.find("</title>")
                                    title= data[x+7:y]
                                    line= [code, title]
                                    netflix.append(line)
                                except:
                                    pass
import csv
with open('Netflix_Codes', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(netflix)
