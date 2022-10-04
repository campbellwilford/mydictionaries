file = open('bookofJohntext.txt','r') 

words = ['Father','God','Christ','Spirit','life','man']

for line in file:
    John = line.strip()
    John_list = John.split()

word_count = {list: John_list.count(list) for list in John_list}

for word in word_count:
    if word in words:
        print(word, '-', John_list.count(word))




