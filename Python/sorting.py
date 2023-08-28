data = [6, 3, 1, 2, 4, 5]
data.sort()#sort() method uses in place sorting which ordered a data and changed its original version
print(data)
data = [6, 3, 1, 2, 4, 5]
data2 = sorted(data)#sorted() method uses copied sorting which ordered a data and unchanged its original version
print(data2)