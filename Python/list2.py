#check if a list contains the number 20 and change its value to 200 for the first one
list1=[5,10,15,20,25,50,20]
'''if 20 in list1:
    print("20 is in the list")
else:
    print("20 is not in the list")
for num in range(len(list1)):
    if (list1[num]==20):
        list1[num]=200
        break'''
if 20 in list1:
    for num in range(len(list1)):
        if (list1[num]==20):
            list1[num]=200
            break
else:
    print("20 is not in the list")
print(list1)