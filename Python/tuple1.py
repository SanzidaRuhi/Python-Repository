#Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples allow duplicate values.
from decimal import InvalidContext
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])#print value of the index
print(len(thistuple))#print length of the tuple
thistuple = ("apple",)#tuple with single element
print(type(thistuple))
t = tuple('lupins')
print(t)
t = ('A',) + t[1:]
print(t)
tuple1 = ("apple", "banana", "cherry")#tule with string
tuple2 = (1, 5, 7, 9, 3)#tuple with integer
tuple3 = (True, False, False)#tuple with boolean value
tuple4 = ("abc", 34, True, 40, "male")#tuple with string, int and boolean
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])#slicing from index 2 to index 5
print(thistuple[:4])
print(thistuple[2:])
print("negative indexing:",thistuple[-1])#negative indexing starts from ending
print(thistuple[-4:-1])
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#To change a tuple, we need to convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")#append like list
thistuple = tuple(y)
print(thistuple)
y = ("orange",)
thistuple =thistuple+ y#adding a tuple in a tuple
print(thistuple)
y = list(thistuple)
y.remove("orange")
thistuple = tuple(y)
print(thistuple)
del x
#print(x):will print error as the tuple is deleted
#will equal the tuples and print their values
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#using asterisk means starting to ending
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#for loop in tuple
for x in thistuple:
  print(x)
for i in range(len(thistuple)):
  print(thistuple[i])
#while loop in tuple
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
tuple_sum = tuple1 + tuple2#adding 2 tuples
print(tuple_sum)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2#joining tuples
print(tuple3)
tuple_multiply=tuple1*2#printing a tuple multiple times
print(tuple_multiply)
count=tuple_multiply.count("banana")#count how many time banana is in the tuple
print("the element here is ",count," times")
index=tuple_sum.index(7)#in which position the element 7 resides
print("the element reside in ",index," position")
t = divmod(7, 3)#divmod() is a built in function which takes 2 parameters and returns 2 values: 1st one is quotient and 2nd one is remainder
print(t)
quot, rem = divmod(7, 3)
print(quot)
print(rem)
def min_max(t):
    print(min(t))
    print(max(t))
t = (42,23,14,-2)
min_max(t)