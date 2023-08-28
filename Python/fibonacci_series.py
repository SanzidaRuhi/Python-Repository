a=0
b=1
c=0
for i in range(30):
    print(c)
    a=b
    b=c
    c=a+b
#print a list that contains fibonacci series of 100 numbers
a=0
b=1
c=0
fibonacci_list=[]
for i in range(100):
    fibonacci_list.append(c)
    a=b
    b=c
    c=a+b
print(fibonacci_list)