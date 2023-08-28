#open each of data files, read the lines from the data files and create a list from the data files
with open ('james.txt') as jaf:#open the file
    data=jaf.readline()#read the line of data
james=data.strip().split(',')#convert the data to a list
with open ('julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open ('mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open ('sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')
print('james=',sorted(james))
print('julie=',sorted(julie))
print('mikey=',sorted(mikey))
print('sarah=',sorted(sarah))
def sanitize(time_string):
    if '-' in time_string:#use the in operator to check whether '-' is in the time string or not
        splitter = '-'
    elif ':' in time_string:#use the in operator to check whether ':' is in the time string or not
        splitter = ':'
    else:
        return(time_string)#do nothing if the string does not need to be sanitized
    (mins, secs) = time_string.split(splitter)#split the string to differentiate minutes and seconds
    return(mins + '.' + secs)
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
#clean_james = [sanitize(each_t) for each_t in james]
for each_t in james:
    clean_james.append(sanitize(each_t))#take items from the list, sanitize then and then append to the new list
#clean_julie = [sanitize(each_t) for each_t in julie]
for each_t in julie:
    clean_julie.append(sanitize(each_t))
#clean_mikey = [sanitize(each_t) for each_t in mikey]
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
#clean_sarah = [sanitize(each_t) for each_t in sarah]
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))
print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)
'''mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print(secs)
meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)
lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)
dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)
clean = [float(s) for s in clean]
print(clean)
clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)'''
unique_james=[]
for each_t in clean_james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])
unique_julie=[]
for each_t in clean_julie:
    if each_t not in unique_james:
        unique_julie.append(each_t)
print(unique_julie[0:3])
unique_mikey=[]
for each_t in clean_mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])
unique_sarah=[]
for each_t in clean_sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])
distances=set()
distances = {10.6, 11, 8, 10.6, "two", 7}#any duplicates in the list will be ignored
distances = set(james)
#a function to use the files
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('file error:',str(ioerr))
        return(None)
james=get_coach_data('james.txt')
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
sarah=get_coach_data('sarah2.txt')
#(sarah_name, sarah_dob)=sarah.pop(0), sarah.pop(0)
#print(sarah_name +"'s fastest times are: " +str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
sarah_data={}
sarah_data['name']=sarah.pop(0)
sarah_data['dob']=sarah.pop(0)
sarah_data['times']=sarah
print(sarah_data['name'],' fastest times are: ',str(sorted(set([sanitize(t) for t in sarah_data['times']]))[0:3]))
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        temporary_list=data.strip().split(',')
        return ({'name':temporary_list.pop(0),'dob':temporary_list.pop(0),'times':str(sorted(set([sanitize(t) for t in temporary_list]))[0:3])})
    except IOError as ioerr:
        print("file error:"+str(ioerr))
        return(None)
james=get_coach_data('james2.txt')
print(james['name']+"'s fastest times are: "+james['times'])
julie=get_coach_data('julie2.txt')
print(julie['name']+"'s fastest times are: "+julie['times'])
mikey=get_coach_data('mikey2.txt')
print(mikey['name']+"'s fastest times are: "+mikey['times'])
sarah=get_coach_data('sarah2.txt')
print(sarah['name']+"'s fastest times are: "+sarah['times'])
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,list_of_times):
        self.times.extend(list_of_times)
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
print(type(sarah))
print(sarah)
print(sarah.name,sarah.dob,sarah.times)
print(james.name,james.dob,james.times)
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return Athlete(templ.pop(0),templ.pop(0),templ)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
james = get_coach_data('james2.txt')
print(james.name+ "'s fastest times are: " + str(james.top3()))
julie = get_coach_data('julie2.txt')
print(julie.name+ "'s fastest times are: " + str(julie.top3()))
mikey = get_coach_data('mikey2.txt')
print(mikey.name+ "'s fastest times are: " + str(mikey.top3()))
sarah = get_coach_data('sarah2.txt')
print(sarah.name+ "'s fastest times are: " + str(sarah.top3()))
vera=Athlete('vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob=a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
vera=AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0),templ.pop(0),templ)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
james = get_coach_data('james2.txt')
print(james.name+ "'s fastest times are: " + str(james.top3()))
julie = get_coach_data('julie2.txt')
print(julie.name+ "'s fastest times are: " + str(julie.top3()))
mikey = get_coach_data('mikey2.txt')
print(mikey.name+ "'s fastest times are: " + str(mikey.top3()))
sarah = get_coach_data('sarah2.txt')
print(sarah.name+ "'s fastest times are: " + str(sarah.top3()))