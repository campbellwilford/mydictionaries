import csv

#open the vendorlist file 
infile = open('VendorList.csv','r')

#create a csv object from the file object
csvfile = csv.reader(infile, delimiter=',')

#create an output file
outfile = open('marketinglistFINAL.csv','w')

#create an exmpty dictionary
dictionary = {}

#iterate through the csv object
next(csvfile)
for record in csvfile:
    #add the key-value pair to the dicionary
    dictionary['email'] = record[4]
    dictionary['phone'] = record[5]
    dictionary = {(record[1] + ' '+ record[2]):{dictionary['email'],dictionary['phone']}}

#print the dicionary after the loop is finished
print(dictionary)

#iterate through the dicionary and write to the output file

for key in dictionary:
    outfile.write(key)
    outfile.write(': ')
    outfile.write(str(dicionarty[key]))
    outfile.write('\n')

#close your output file
outfile.close()