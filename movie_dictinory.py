from tkinter import END


current_movies={'movie1':'10.30AM',
                'movie2':'1.30PM',
                'movie3':'4.00PM'}

current_movies1={}
current_movies1['movie1'] = '10.30AM'
current_movies1['movie2'] = '1.30PM'
current_movies1['movie3'] = '4.00PM'
current_movies1['movie4'] = '7.00PM'

print("we are showing the below movies\n")
for i in current_movies:
    print(i)
movie=input("What time you would like to go for movie?")

show_time= current_movies.get(movie)
if show_time == None:
    print("requested movie is not playing\n")
else:
    print(movie +" show time is "+ show_time)