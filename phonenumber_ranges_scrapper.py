from bs4 import BeautifulSoup
import re


#Load html file
#I took ranges from here: https://phonenum.info/mobile-operators/mts
with open("/home/user/Downloads/yota.html", 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")
    tags_reg = soup.findAll('div', class_='region_diapasons_start')
    tags = soup.findAll('div', class_="diapasons")

#Scrapping Regions here, YOU MUST VERIFY THE LEGHT FIRST and put it into "range":
regions = []
for i in range(0,82):
    regions.append(tags_reg[i].text.split()[1]+ " " +tags_reg[i].text.split()[2])


    
#This is the loop that print out ranges for all the regions
for number, obl in enumerate(regions):
    

#Cleaning out numbers

    reg = tags[number].text.split()

    sps=[]
    b = []
    c = []
    clean = []

#Getting rid of special chars and first seven
    for i in reg:
        if i == "+7":
            continue
        if i == "...":
            continue
        sps.append(i)

    
#Filtering numbers only
    for i in sps:
        b.append(re.findall('\d+', str(i)))

#Joining numbers
    i = 0
    while i < int(len(b)):
        clean.append(str(b[i][0]+str(b[i+1][0]+str(b[i+1][1]+str(b[i+1][2])))))

        i += 2

#Printing out

    i = 0
    ind = 1

    print('\t[')
    print('\t\t{')
    while i < int(len(clean)):

#We add "mts" here because we scrapped mts ranges, so you want to put a different operator when you scrape a different one
        print("\t\t\t" f'"{obl} mts {ind}"', ":", (int(clean[i]), int(clean[i+1])),",")
        i = i+2
        ind = ind+1
    print('\t\t}')
    print('\t],')

