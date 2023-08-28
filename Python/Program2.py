num1=10
num2=5
num3=num1#num3=10
num1=num2#num1=5
num2=num3#num2=10
print("num1=",num1)
print("num2=",num2)
n = 17
print(n,25)
print(n+25)
miles = 26.2
print(miles * 1.61)
name = "charlie chaplin"
print(name.title())#title() method makes the string look like a title
name = "Charlie Chaplin"
print(name.upper())#upper() method make all the alphabets in upper case
print(name.lower())#lower() method make all the alphabets in lower case
first_name = "charlie"
last_name = "chaplin"
full_name = f"{first_name} {last_name}"# use f-strings to compose complete messages using the information associated with a variable
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!" 
print(message)
print("\tPython")#adding whitespaces
print("Languages:\nPython\nC\nJavaScript")#making new lines
print("Languages:\n\tPython\n\tC\n\tJavaScript")#making new lines with adding whitespaces
print("multiplication:",2 * 3)#using * means multiplication
print("square:",3 ** 2)#using ** means exponents
print(2 + 3 * 4)#using expressions according orders
universe_age = 13_770_000_000#python erases all underscores in a digit
print(universe_age)
x, y, z = 0, 0, 0
MAX_CONNECTIONS = 5000
#Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed
