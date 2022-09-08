import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))

phone = phonebook ['Chris']

print(phone)

print(len(phonebook))

mydictionary = dict(m=8, n=9)
print(mydictionary)

mydict = {}
print(mydict)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'

if name in phonebook: 
    print(phonebook[name])
else:
    print(name,'not found')




print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()


print(phonebook)
phonebook ['Chris'] = '555-0123'
phonebook ['Joe'] = '555-4444'
print(phonebook)


print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


#del phonebook['Chris']
#print(phonebook)



print()
print('*****  end section 4 ********')
print()





print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for key in phonebook:
    print(key)
    print(phonebook[key]) #this will give the values as well

#automatically iterates through keys. if you wan to look through values you will have to give a different command

for value in phonebook.values():
    print(value)


for k,v in phonebook.items():
    print('key:',k,'value:', v)


for tuple in phonebook.items():
    print(tuple)



print()
print('*****  end section 5 ********')
print()




print()
print('*****  start section 6 - using get and clear ********')
print()



phone = phonebook.get('Chris', 'ket not found')
print(phone)


#phonebook.clear()
#print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#'pop' will take take it out of the dictionalry in your output

#remove = phonebook.pop('Chris', 'key not found')

#print(remove)
#print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()



#a = phonebook.popitem()

#print(a)
#print(phonebook)

#there is an error where it doesn't randomize it, it picks the last vale in your dictionary 



print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

#these do the same thing, the line below is just more effecient 

print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()








