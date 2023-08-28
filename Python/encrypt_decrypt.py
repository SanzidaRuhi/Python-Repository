list=[]
quantity=[]
quantity.append(input("""Write the number of words and the value of "K"
for example: 2 3: """))
quantity =" ".join(quantity)
quantity=quantity.replace(" ", ",")
i=0
while i<int(quantity[0]):
    list.append(input("Write the words separated by space and end with 'point'. : "))
    i=i+1
list=" ".join(list)
list=list.replace("", ",")
list=list.split(",")
k=int(quantity[2])
listn=[]
listl=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
j=0
while j < len(list):
    i=0
    while i < len(listl):
        if list[j]==listl[i]:
            listn.append(listl[i-k])
        i=i+1
    if list[j]==" ":
        listn.append(" ")
    if list[j]==".":
        listn.append(". ")
    j=1+j
listn="".join(listn)
print ("decrypted message: ")
print(listn)
exit = input("EXIT")