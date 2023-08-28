import os
os.getcwd()#check the current directory
os.chdir('/Doc/Python/Head First Python/Chapter 3')#change the directory
os.getcwd()
data = open('sketch.txt')#open text file
print(data.readline(), end='')#print the first line
print(data.readline(), end='')#print the 2nd line
#printing all lines from starting using for loop
data.seek(0)
for each_line in data:
    print(each_line, end='')
data.close()#close text file
#splitting role and spoken lines using split method
'''data = open('sketch.txt')
for each_line in data:
    (role, line_spoken) = each_line.split(':')
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')'''
#sometimes for having too much variables it shows valuetime error
#help(each_line.split)#use help() method to know more about a method
'''data = open('sketch.txt')
for each_line in data:
    (role, line_spoken) = each_line.split(':',1)
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')'''
#use find method to determine id there is a colon or not
each_line = "I tell you, there's no such thing as a flying circus."
print("\n",each_line.find(':'))
each_line = "I tell you: there's no such thing as a flying circus."
print("\n",each_line.find(':'))
#use this code to determine if there is a colon
data = open('sketch.txt')
for each_line in data:
    if not each_line.find(':')==-1:#use not keyword to determine the value
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
data.close()
#use try except mechanism for exception handling
try:
    if os.path.exists('sketch.txt'):
        data = open('sketch.txt')
        for each_line in data:
            try:#this code is protected from runtime errors
                (role, line_spoken) = each_line.split(':', 1)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')
            except:
                pass#if a error occurs,this code is executed
        data.close()
    else:
        print('The data file is missing!')
except:
    print('The data file is missing!')
#using specific errors
try:
    if os.path.exists('sketch.txt'):
        data = open('sketch.txt')
        for each_line in data:
            try:#this code is protected from runtime errors
                (role, line_spoken) = each_line.split(':', 1)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')
            except ValueError:
                pass#if a error occurs,this code is executed
        data.close()
    else:
        print('The data file is missing!')
except IOError:
    print('The data file is missing!')
#assigning empty  file
man=[]
other=[]
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()#the strip method removes unwanted whitespace from a string
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
try:
    #open your two files and assign each to file objects
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    #w is used to insert write mode
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('file error')
man_file.close()
other_file.close()
try:
    data1 = open('missing.txt')
    print(data1.readline(), end='')
except IOError as err:
    print('\nFile error: ', err)
finally:
    if 'data1' in locals():#the in operator test for membership
        data1.close()
try:
    data = open('its.txt', "w")
    print("It's...", file=data)
except IOError as err:
    print('File error: ' + str(err))
finally:
    if 'data' in locals():
        data.close()
try:
    with open('its.txt', "w") as data:#use of with negate use of finally
        print("It's...", file=data)
except IOError as err:
    print('File error: ' + str(err))
#if we use with, we don't need to close the file as python do it itself
#The with statement takes advantage of a Python technology called the context management protocol.
with open('man_data.txt') as mdf:
    print(mdf.readline())

import pickle
...
with open('mydata.pickle', 'wb') as mysavedata:#here b tells python to open in file in binary mode
    pickle.dump([1, 2, 'three'], mysavedata)#to save data we use dump
...
with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)#restore data from file using load 
print(a_list)

'''import module_nester
try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        module_nester.print_lol(man, fh=man_file)
        module_nester.print_lol(other, fh=other_file)
except IOError as err:
    print('File error: ' + str(err))'''

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('pickling error:'+str(perr))

new_man=[]
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
#module_nester.print_lol(new_man)