print("hello world")
print("i am ruhi")
print("student of stamford university")
print("this is my first program")
names=["nihad","parisa","nuzaira","aariz"]
print(isinstance(names, list))
num_names=len(names)
print(isinstance(num_names,list))
minutes = 105
print(minutes / 60)#'/' returns floating value after division
minutes = 105
hours = minutes // 60#'//' returns integer ceil value after division
print("hours:",hours)
remainder = minutes - hours * 60
print("minutes left:",remainder)
remainder = minutes % 60
print("minutes left:",remainder)
x=5
y=5
print(x!=y)#x is not equal to y
print(x > y)#x is greater than y
print(x < y)#x is less than y
print(x >= y)#x is greater than or equal to y
print(x <= y)#x is less than or equal to y
#changing values
a = 5
b = a # a and b are now equal
a = 3 # a and b are no longer equal
print(b)