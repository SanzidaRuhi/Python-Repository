from http.server import HTTPServer, CGIHTTPRequestHandler
port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
import athlete_model
import yate
import glob
data_files = glob.glob("G:\Doc\Python\Head First Python\Chapter 7\webapp\webapp\data"+"/*.txt")
athletes = athlete_model.put_to_store(data_files)
print(yate.start_response())#Always start with a Content-type line.
print(yate.include_header("Coach Kelly's List of Athletes"))#Start generating the web page, providing an appropriate title.
print(yate.start_form("generate_timing_data.py"))#Start generating the form, providing the name of the serverside program to link to.
print(yate.para("Select an athlete from the list to work with:"))#A paragraph telling your user what to do
for each_athlete in athletes:#Generate a radiobutton for each of your athletes.
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))#End the form generation with a custom “Submit” button.
print(yate.include_footer({"Home": "/index.html"}))