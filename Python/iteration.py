#for loop
for i in range(4):#print hello for 4 times counting 0 to 3
    print('Hello!')
for i in range(10):#print i 10 times
    print(i)
for i in range(10):#print multiplication
    print(i*i)
for i in range(10):#print power
    print(i**2)
sum = 0 # initialize the value of the sum with 0
for i in range(10): # the loop runs for a 100 times
    sum = sum + i # in each iteration a number is added to the sum
    #sum += i #can write the above ine as this too
print(sum) # prints the new sum
sum = 0 
for i in range(5,10): # the loop runs for 5 times from 5 to 9
    sum += i  
    print(sum)
print(sum)
#while loop
n = 10
while n > 0:
    print(n)
    n = n - 1
print('while loop is Finished!')
i = 0
while True:#The loop condition is  𝑇𝑟𝑢𝑒 , which is always true, so the loop runs until it hits the break statement
    if i == 10:
        break
    print(i)
    i = i + 1
print('Done!')