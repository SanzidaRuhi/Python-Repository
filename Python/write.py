out=open("data.out","w")#out is the data file object, data.out is the file name, w is the access model to use
#use a model to append a file, use w+ to read and write without clobbering, use w to create a file and write or to write on a file with clobbering
print("hello world!",file=out)#hello world is what is written into the file
out.close()#flusing and it's important
#open() by default uses r mode for reading