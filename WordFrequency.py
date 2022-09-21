with open('sometext (1).txt','r') as infile:
    sometext = infile.read().rstrip()

sometext_list = sometext.split()


times = {list: sometext_list.count(list) for list in sometext_list}
print(times)

for i in sometext_list:
    print(i,'-', sometext_list.count(i))

