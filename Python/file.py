'''The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode.
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)'''
f=open("text.txt")
f=open("text.txt","rt")
#To open the file, use the built-in open() function. The open() function returns a file object, which has a read() method for reading the content of the file:
print(f.read())
#f = open("D:\\myfiles\welcome.txt", "r")[use this for a different file location]
#print(f.read(5))#read 5 characters
#print(f.readline())#read a line
for x in f:
  print(x)
f.close()#close the file using close() method
f = open("text.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("text.txt", "r")#need to open the file again for read after appending
print(f.read())
'''f = open("text.txt", "w")#used for overwrite
f.write("Woops! I have deleted the content!")
f.close()
f = open("text.txt", "r")
print(f.read())'''
#f = open("myfile.txt", "x")
'''import os
os.remove("myfile.txt")'''
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#os.rmdir("myfolder")#use rmdir to delete an empty folder