#value
x = 5
y = "John"
print(x)
print(y)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)
print(x)
print(y)
print(z)
#type
x = 5
y = "John"
print(type(x))
print(type(y))
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#though both cases are same but it is better to use commas then + for adding values as + goes for sum
#using a function
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#using a global keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x) #convert from int to float:
b = int(y) #convert from float to int:
c = complex(x) #convert from int to complex:
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#string
a="hello world"
print(a)
print(a[4])
print(a[2:5])#slicing middle of the string
print(a[:4])#slicing starting of string
print(a[3:])#slicing ending of string
print(a[-5:-2])#negative indexing
for x in "banana":
  print(x)
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print(a.upper())
print(a.lower())
print(a.strip())#remove spaces in the starting and ending of the string
print(a.replace("h", "J"))
print(a.split(" ")) # returns ['hello', 'world']
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#boolean
print(5 == 5)
print(5 == 6)
print(type(True))