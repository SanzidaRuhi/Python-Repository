def demo(number):
    print("This is a function")
    return number
def print_lyrics():
    print("I'm a computer scientist, and I'm okay.")
    print("I work all night and I sleep all day.")
print_lyrics()#calling the function
print(type(print_lyrics))#printing type of the defining thing
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
def print_twice(value):
    print(value)
    print(value)
print_twice('Stamford')
print_twice(42)
import math
print_twice(math.pi)
print_twice('Spam '*4)
michael = 'Eric, the half a bee.'
print_twice(michael)
def message_twice(part1, part2):
    message = part1 + part2
    print_twice(message)
line1 = 'Hello '
line2 = 'World'
message_twice(line1, line2)
def add_num(x , y):
    res = x + y
    return res
print("Let's see the function in action!")
result = add_num(100,25)
print("The addition of 100 and 25 is", result)
def series_sum(num_1, num_2, inc):
    sum = 0
    current_num = num_1
    while(current_num <= num_2):
        sum = sum + current_num
        current_num = current_num + inc
    return sum
# Let's sum the series 1,3,5,7,9,.....,1235
# The first_num = 1, second_num = 1235 and increment inc is 2
result = series_sum(1, 1235, 2) 
print("The summation of the series from 1 to 1235 is: ", result)
import cmath # As the result is complex, we imported complex math module
def solve_x(a,b,c):
    numerator = -b + cmath.sqrt(b**2 - 4*a*c)
    denominator = 2*a
    x_value = numerator-denominator
    return x_value
# Suppsoe we have an equation 7x^2 - 8x + 3 = 0
# Then a = 7, b = -8 and c = 3
a, b, c = 7, -8, 3
x = solve_x(a, b, c)
print("The value of x is: ", x, "or", -x)
def my_function(*kids):#If the number of arguments is unknown, add a * before the parameter name
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")#adding key=value syntax will remove the matter of order
def my_function(**kid):#If the number of keyword arguments is unknown, add a double ** before the parameter name
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()#the default value of parameter will only work here as there is no given initialize value
my_function("Brazil")
def my_function(x):
  return 5 * x
print(my_function(3))#print the return value
print(my_function(5))
print(my_function(9))
def myfunction():
  pass#this will erase the error
def tri_recursion(k):#recursion example
  if(k > 0):
    result = k + tri_recursion(k - 1)#calls recursion until value returns 0
    print(result)
  else:
    result = 0
  return result#returns result each time and add in recursive process
print("Recursion Example Results")
tri_recursion(6)