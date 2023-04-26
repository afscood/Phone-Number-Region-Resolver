import csv
import json
import re

#search function
def search_numbers(numbers, ranges):
    #loop for each number in the numbers list
    for number in numbers:
        
        #flagging number
        found = False
        
        #loop through each range in the list of ranges
        for lst in ranges:
            for item in lst:
                for name, r in item.items():

                    #checking if the number is within the current range
                    if number in range(r[0], r[1]+1):
                        
                        #formatting the output
                        #x = name.split()[:-2]
                        region = name.split(",")[0]
                        long = name.split(",")[1]
                        lat = name.split(",")[2]
                        print(lat)
                        #print(" ".join(x))
                        #print(f"{number} is in the range {name}")

                        #if found than set flag to True
                        found = True
                        break
                if found:
                    break

        #If the number was not found in any range, print it as not found            
        if not found:
            print("UNIDENTIFIED")
            #print(f"{number} is not in any of the given ranges")




#loading parsed ranges file in json. We will search for number in there
with open('phone_ranges.json', 'r') as f:
    ranges = json.load(f)

#loading csv from CRM. You want to make sure that it formatted in a proper way
#it is a good idea to open it in sheets and resave it from there
with open('/home/user/shared/raw_crm.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#Creating list to store parsed and formatted numbers
    clean_numbers = []
    
#Cleaning out the values with phone numbers, the idea behind this is to make all of those numbers in the same 10 digit format
    for line in csv_reader:
        clean_num = re.sub(r'\D', '', line[4])
        if clean_num.startswith('9') and len(clean_num) == 10:
            clean_numbers.append(int(clean_num))
        elif clean_num.startswith('8') or clean_num.startswith('7'):
            clean_num = clean_num[1:]
            if clean_num.startswith('9') and len(clean_num) == 10:
                clean_numbers.append(int(clean_num))
            else:
                clean_num = 0 
                clean_numbers.append(int(clean_num))
        else:
            clean_num = 0 
            clean_numbers.append(int(clean_num))

#Checkin for nulls
numbers = clean_numbers
search_numbers(numbers , ranges)


