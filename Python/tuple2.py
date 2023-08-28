#sort a tuple using 2nd index of inside tuple
tuple1=(('a',23),('b',37),('c',11),('d',29))
x=list(tuple1)#convert tuple to list as tuple can't muted
print(x)
print(type(x[0]))
x.sort(key=lambda k:k[1])#sort using 2nd index of tuple
print(x)
tuple1=tuple(x)#covert list to tuple
print(tuple1)
#swapping values of tuple
a, b = 7, 18
temp = a
a = b
b = temp
print(a, b)