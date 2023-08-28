#adding sublist in the list in a specific point
list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
sub_list=['h','i','j']
A=list1[2]
print(A)
B=A[1]
print(B)
C=B[2]
print(C)
C.extend(sub_list)
print(C)
print(list1)