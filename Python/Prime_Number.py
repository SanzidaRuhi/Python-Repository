#check if a number is  prime number or not
number=7
count=0
for i in range(2, number):
    if (number%i==0):
        count+=1
        pass
        print("the number is not a prime number")
        break
if count==0:
    print("the number is a prime number")

#generating list of prime numbers
import math as m
lower_bound = 1
upper_bound = 10
print("Prime numbers between", lower_bound, "and", upper_bound, "are:")
'''for num in range(lower_bound, upper_bound + 1):
#for num in range(1001):
#for num in range(upper_bound + 1):
   # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(m.sqrt(num))):
            if (num % i) == 0:
                break
        else:
            print(num)'''
for num in range(lower_bound,upper_bound+1):
    for i in range(2, num-1):
        if num%i==0:
            break
    else:
        print(num)