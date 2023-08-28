#create a dictionary from another dictionary
dictionary1={
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New york'
}
key=['name','salary']#keys to extract
dictionary2=dict()
#dictionary2={i: dictionary1[i] for i in key}
for i in key:
    dictionary2.update({i:dictionary1[i]})#add key with its value from dictionary1
print(dictionary2)