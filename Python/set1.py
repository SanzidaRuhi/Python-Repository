#A set is a collection which is unordered, unchangeable*, and unindexed
#Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#print the set ignoring the duplicates
print(len(thisset))
set1 = {"abc", 34, True, 40, "male"}#set can contain different data types
print(type(thisset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
for x in thisset:#accessing items using loop
  print(x)
print("banana" in thisset)#check if banana is present in the set
thisset.add("orange")#adding to a set
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)#updating a set
print(thisset)
mylist = ["kiwi", "orange"]
thisset.update(mylist)#updating with a list
print(thisset)
thisset.remove("banana")#remove() method remove an item
print(thisset)
thisset.discard("kiwi")#discard() method also remove item
print(thisset)
x = thisset.pop()#pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
print(x)
print(thisset)
thisset.clear()#clear() method empties the set
print(thisset)
del thisset#del keyword will delete the set completely
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)#union() method returns a new set with all items from both sets
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)#update() method inserts the items in set2 into set1
print(set1)
#Both union() and update() will exclude any duplicate items.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)#intersection_update() method will keep only the items that are present in both sets.
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)#intersection() method will return a new set, that only contains the items that are present in both sets
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)#symmetric_difference_update() method will keep only the elements that are NOT present in both sets
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)#symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
print(z)