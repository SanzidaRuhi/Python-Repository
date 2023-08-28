#printing yes or no if wewight is even
weight=int(input("enter weight:"))
print("watermeolon weight is:",weight)
if(weight%2==0):
    print("YES")
else:
    print("NO")
#convert and print a string while founding vowel, keeps contiue and while founding consonant, print dot(.) and the letter 
string1 = input("enter a string: ")
string_length = len(string1)
string2=string1.lower()
for i in range(string_length):
    if (string2[i] == 'a' or string2[i] =='e'or string2[i] == 'i' or string2[i] =='o' or string2[i]=='u'):
        continue
    else:
        print(("."+string2[i]),end="")
#print capacity using passenger number
number_of_stop=int(input("enter number of stop:"))
capacity=0
sum=0
for i in range(0,number_of_stop):
    exit_passenger,enter_passenger=map(int,input().split())
    sum=sum-exit_passenger
    sum=sum+enter_passenger
    if(sum>capacity):
        capacity=sum
print(capacity)
#print message when length of name is even or odd
name=input("enter an username:")
username=name.lower()
print(username)
length=len(username)
if(length%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")