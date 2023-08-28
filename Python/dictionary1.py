#If you hear other programmers talking about a “mapping,” a “hash,” or an “associative array,” they are talking about a “dictionary.”
#dictionaries are ordered and mutable
#dictionaries don't allow duplicates. it cannot have two items with the same key
#dictionary items can be of String, int, boolean, list and tuple data types
cleese = {}
palin = dict()
type(cleese)
type(palin)
cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}
palin['Name']#indexing lists using keys not numbers
cleese['Occupations'][-1]#last item associated with the list
palin['Birthplace'] = "Broomhill", 'Sheffield', "England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"
print(palin)
print(len(palin))#dictionary show length as per keys
print(cleese)
print(len(cleese))
eng2sp = dict()
print(eng2sp)#will print {} that shows an empty dictionary
eng2sp['one'] = 'uno'#adding key and value
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['three'])#printing value using key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020#dictinary will overwrite value
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))
x = thisdict["model"]#acces the value using key
print(x)
x = thisdict.get("model")#access the value using get() method
print(x)
x = thisdict.keys()#The keys() method will return a list of all the keys in the dictionary.
print(x)
y = thisdict.values()#values() method will return a list of all the values in the dictionary.
print(y)
z = thisdict.items()#items() method will return each item in a dictionary, as tuples in a list.
print(z)
thisdict["color"] = "white"#adding key will update key and value
#thisdict.update({"color": "red"})#add key and a value
thisdict["year"] = 2018#change value of the key
#thisdict.update({"year": 2020})#also change the value of the key
print(x) #after the change
print(y)
print(z)
if "model" in thisdict:#to check if a key is in the dictionary
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict.pop("model")#pop() method removes the item with the specified key name
print(thisdict)
thisdict.popitem()#popitem() method removes the last inserted item 
print(thisdict)
del thisdict["year"]#del keyword removes the item with the specified key name
print(thisdict)
del thisdict#del keyword can also delete the dictionary completely
thisdict = {
  "brand": "Ford"
}
thisdict.clear()#clear() method empties the dictionary
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:#Print all key names in the dictionary, one by one
#for x in thisdict.keys():#keys() method to return the keys of a dictionary
  print(x)
for x in thisdict:#Print all values in the dictionary, one by one
#for x in thisdict.values():#values() method to return values of a dictionary
    print(thisdict[x])
for x, y in thisdict.items():#Loop through both keys and values, by using the items() method
  print(x, y)
mydict = thisdict.copy()#copy() method copies the dictionary
print(mydict)
mydict = dict(thisdict)#dict() function copies the dictionary
print(mydict)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("nested dictionary:",myfamily)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print("after creating the nested dictionary:",myfamily)