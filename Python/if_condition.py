#program to check if a number is odd or even
x = 5 # Change this value to see the effect in following code
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
#program to check if 2 numbers are equal, greater or lesser
x=5 # Change this value to see the effect in following code
y=5 # Change this value to see the effect in following code
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
#checking if else condition using functions
def draw_a():
    print('a')
def draw_b():
    print('b')
def draw_c():
    print('c')
choice = 'a' # Change this value to see the effect in following code
if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()
#program to check if x is a positive single digit number
#if 0 < x and x < 10:#can write both conditions in one line
#if 0 < x < 10:#can also write in this way
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')
#one line if else condition
a = 2
b = 330
if b > a:
  pass#having a pass argument will show nothing but not having pass will show an error
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")#the middle one is for elif
#program for AND & OR
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")
#program for nested if
x = 22
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")