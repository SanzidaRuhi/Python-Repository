#We can add, remove, count, sort, search, and do quite a few other things to python lists.

print('first we need an example list:')
x = [4,6,2,7,9,2,6,2,6,1]
print("this is the customized list:",x)

print( 'lets add something. For that use .append, which will add something to the end of the list')
x.append(5)
print("after appending the list is:",x)

print("what if you have an exact place that you'd like to put something in a list?")
x.insert(4,3)
print("after inserting in a fixed position the list is:",x)

# so the reason that went in the 3rd place, again, is because we start at the zero element, then go 1, 2.. .and so on.
# now we can remove things. remove will remove the first instance of the value in the list. If it doesn't exist, there will be an error:
print('Lets remove the number 7 from the list')
x.remove(7)
print("after removing 7, the list is:",x)

#next, remember how we can reference an item by index in a list? like:
print('Lets reference an item at index four, position five')
print("the item on the index 4 is:",x[4])

print('We can also print the index of an element say for number 2')
print("the index number for the first 2 is:",x.index(2))

# now here, we can see that it actually returned a 2, meaning the third element was a 2. when we knew there were more indices of 5. so instead we might want to know before-hand how many examples there are.
print("Lets print how many 2's are present in the list")
print("the number of 2's presented in the list is:",x.count(2))

# so we see there are actually 3 of them
print("we can also sort the list as well")
x.sort()
print("after sorting the list is:",x)

print("what if these were strings? like: the list below")
y = ['Jan','Feb','Mar','April','May','June']
print("the list of strings is:",y)

y.sort()
print("That's how the sorted list of strings be printed ", y)

# noooo problemo!
# You can also just reverse a list, but, before we go there, we should note that all of these manipulations are mutating the list. 
# keep in mind that any changes you make will modify the existing variable.
