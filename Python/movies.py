movies=["the holy grail","the life of brian","the meaning of life"]
print("the movies are:",movies)
print("movie from the list using arreay: ",movies[2])
print("the length of the movie:",len(movies))
movies.append("temple of grail")
print("after appending, the movies are: ",movies)
movies.pop()
print("after pop, the movies are:",movies)
movies.extend(["way of life","365 days"])
print("after adding a group of movies, the movies are:",movies)
movies.remove("way of life")
print("after removing a certain movie, the movies are:",movies)
movies.insert(2,"way of life")
print("after inserting a movie in a certain position, the movies are:",movies)
movies.insert(0,"temple of grail")
print(movies)
print(len(movies))
movies.insert(1,1955)
movies.insert(3,1958)
movies.insert(5,1968)
movies.insert(7,1978)
movies.insert(9,1988)
movies.insert(11,2000)
print(movies)
print("the length of the movies after adding numbers and strings:",len(movies))
movies=['temple of grail', 1955, 'the holy grail', 1958, 'the life of brian', 1968, 'way of life', 1978, 'the meaning of life', 1988, '365 days', 2010]
print(movies)
fav_movies=["temple of grail","way of life"]
print("favourite movie is ",fav_movies[1])
print("length of favourite movies:",len(fav_movies))
fav_movies=["temple of grail","the life of brian","way of life"]
for each_step in fav_movies:
    print("favourite movie is",each_step)
movie_details=[
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]],"123"]
print("movie deatails:",movie_details)
print("movie details for a certain position:",movie_details[4][1][3])
print(movie_details[4][0])
print(movie_details[2])
print(movie_details[4][1][2])
print(len(movie_details))
print(len(movie_details[4][1]))
print(len(movie_details[4]))
for each_item in movie_details:
    print(each_item)
print("showing movie items below using for loop:")
for each_item in movie_details:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for nested_item2 in nested_item:
                    print(nested_item2)
            else:
                print(nested_item)
    else:
        print(each_item) 
print("showing movie items below using a function module:")
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)   
print_lol(movie_details)