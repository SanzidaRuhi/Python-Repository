#List items are ordered, changeable, and allow duplicate values
burgers = ['Chicken', 'Tandoori', 'BBQ']
numbers = [42, 123]
empty = []
print(burgers, numbers, empty)
print(burgers[0])
numbers = [42, 123]
numbers[1] = 5
print(numbers)#change the value as list are mutable
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
for x in []:#never runs loop inside an empty list
    print('This never happens.')
list_1 = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(len(list_1))
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("concatenate the lists:",c)
print([0] * 4)#print 0 for 4 times in a list
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])#slicing from index 1 to 2
print(t[:4])#slicing from starting to index 3
print(t[3:])#slicing from index 3 to last
print(t[:])#don't do any slicing
t[1:3] = ['x', 'y']#after slicing, adding x and y in the place of b and c
print(t)
t = ['a', 'b', 'c']
t.append('d')#add value at the end
print(t)
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)#extend t1 with t2 and changes its value
print(t1)
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
#Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print("according to negative inexing, the last item is:",thislist[-1])
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")#The insert() method inserts an item at the specified index
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")#remove() method removes the specified item
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)#pop() method removes the specified index but If you do not specify the index, the pop() method removes the last item
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]#del keyword also removes the specified index
print(thislist)
del thislist#del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
thislist.clear()#clear() method empties the list. clear() method empties the list.
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
for i in range(len(thislist)):
  print(thislist[i])
[print(x) for x in thislist]#three loops give same output
#code to show a list from a list whose elements contains 'a'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
#newlist = [x for x in fruits if "a" in x] #using list comprehension
#newlist = [expression for item in iterable if condition == True](syntax of comprehension)
print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()#sort in ascending order
print(thislist)
thislist.sort(reverse = True)#sort in descending order
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
print(thislist)
thislist.sort(key = str.lower)#if you want a case-insensitive sort function, use str.lower as a key function
#thislist.sort(reverse=True)#it will just show reversely not sortedly
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
mylist = thislist.copy()#copy a list using copy() method
print(mylist)
mylist = list(thislist)#another way of copying a list
print(mylist)
list1 ,list2= ["a", "b", "c"] , [1, 2, 3]
list3 = list1 + list2#concatenate 2 lists
print(list3)
for x in list2:
  list1.append(x)#another way of joining lists
print(list1)
list1.extend(list2)#extend() also join lists
print(list1)
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():#𝑖𝑠𝑢𝑝𝑝𝑒𝑟  is a string method that returns 𝑇𝑟𝑢𝑒 if the string contains only upper case letters.
            res.append(s)
    print(res)
    return res
only_upper("Hello World")