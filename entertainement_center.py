# import media module for Movie() class
# import fresh_tomatoes for the html css and js part
import media
import fresh_tomatoes

# define a short list of some film with title, box art, and trailer
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
limitless = media.Movie("Limitless",
                        "https://upload.wikimedia.org/"
                        "wikipedia/en/1/17/Limitless_Poster.jpg",
                        "https://www.youtube.com/watch?v=jOLqNOfzus4")

xXx = media.Movie("xXx",
                  "https://i.ytimg.com/vi/uO5yyDCQ9JU/maxresdefault.jpg",
                  "https://www.youtube.com/watch?v=MQEFmHsseaU")

school_of_Rock = media.Movie("School of Rock",
                             "http://upload.wikimedia.org/"
                             "wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
kong = media.Movie("Kong: Skull Island",
                   "http://bn9.tpa.bhn.net/content/dam/news/"
                   "images/2015/05/2/universal-king-kong-"
                   "skull-island-3.jpg ",
                   "https://www.youtube.com/watch?v=AP0-9FBs2Rs")
miib = media.Movie("Men in Black II",
                   "https://upload.wikimedia.org/wikipedia/"
                   "en/3/3d/Men_in_Black_II_Poster.jpg",
                   "https://www.youtube.com/watch?v=p4NJHqoojOU")

# define an array with the name of our movies
movies_list = [toy_story, limitless, xXx, school_of_Rock, kong, miib]
# use the function open_movies_page() to open a web page with our movies
fresh_tomatoes.open_movies_page(movies_list)


