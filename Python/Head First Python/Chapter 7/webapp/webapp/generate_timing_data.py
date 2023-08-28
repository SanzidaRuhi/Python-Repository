import cgi
import athlete_model
import yate
import cgitb
cgitb.enable()
athletes = athlete_model.get_from_store()#Get the data from the model.
form_data = cgi.FieldStorage()
print(form_data)
athlete_name = form_data['which_athlete'].value()#Which athlete’s data are you working with?
@property#This decorator allows you to access the data returned by “top3()” as if it were a class attribute.
def top3(self):
    return(sorted(set([self.sanitize(t) for t in self]))[0:3])
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athlete_name + ", DOB: " +athletes[athlete_name].dob + "."))#Grab the athlete’s name and DOB.
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))#Turn the top three list into an unordered HTML list.
print(yate.include_footer({"Home": "/index.html","Select another athlete": "generate_list.py"}))
#The bottom of this web page has two links.
#generate_list is for A link back to the previous CGI script.