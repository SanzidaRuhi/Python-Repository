import random
random_list=[]
for i in range(100):
    random_list.append(random.randint(0,50))#use random.randint(range) for generating random values in a range
print(random_list)
repeated_list=[]
for i in random_list:
    n=random_list.count(i)
    if n>1:
        if repeated_list.count(i)==0:
            repeated_list.append(i)
print(repeated_list)