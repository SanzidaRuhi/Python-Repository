#implementation of best fit memory placement algorithm
block_size=[200,150,300,400,600,500]
process_size=[175,250,470,550]
allocation=[]
allocating_list=[]
block_size.sort()
print(block_size)
for i in range(len(process_size)):
    for j in range(len(block_size)):
        if block_size[j]>=process_size[i]:
            allocation.append(block_size[j])
            block_size[j]=block_size[j]-process_size[i]
            allocating_list.append(i)
            break
for i in range(len(process_size)):
    if i not in allocating_list:
        allocation.append("not allocated")
#print(allocation)
print("best fit placemnt:")
print("ProcessName\t ProcessSize\t BlockSize\t")
for i in range(len(process_size)):
    print(i,"\t\t",process_size[i],"\t\t",allocation[i])