#Strings in python are surrounded by either single quotation marks, or double quotation marks.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""#You can assign a multiline string to a variable by using three quotes
print(a)
a = " Hello, World! "
print("length of the string is ",len(a))
print("first letter in the string is ",a[1])
print(a.upper())
print(a.lower())
print(a.strip())#use strip() method removes any whitespace from the beginning or the end
print(a.replace("H", "J"))#replaces h with j
print(a.split(","))#split the string after getting a comma and make it a list
for x in "banana":#loop in a string
  print(x)
txt = "The best things in life are free!"
print("free" in txt)#checking if the word in in the string or not
if "free" in txt:
  print("Yes, 'free' is present.")
print("expensive" not in txt)#it will print false if we use only in
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
b = "Hello, World!"
print(b[2:5])#use colon for slicing
print(b[2:])
print(b[-5:-2])#Use negative indexes to start the slice from the end of the string
a = "Hello"
b = "World"
c = a + b#concatenate strings
print(c)
'''age = 36
txt = "My name is John, I am " + age#it will show an error as we can't combine string with integers
print(txt)'''
#we can combine strings and numbers by using the format() method. The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))#Use the format() method to insert numbers into strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."#The format() method takes unlimited number of arguments, and are placed into the respective placeholders
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
print(myorder.format(quantity, itemno, price))
txt = "We are the so-called \"Vikings\" from the north."#use \ to use double quote as a character
print(txt)