import timeit
import media
from ud036_StarterCode import fresh_tomatoes

## using a dictionary of dictionaries {} = dict()
movie_dictionary = {
    "1_divergent":{
        "title":"Divergent",
        "duration": "2h 19m",
        "storyline":"A thrilling action-adventure film set in a world where people are divided into distinct factions based on human virtues.",
        "poster_image_url":"https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
        "trailer_youtube_url":"https://youtu.be/336qJITnDi0"
    },
    "2_insurgent":{
        "title":"The Divergent Series: Insurgent",
        "duration": "1h 59m",
        "storyline":"Insurgent raises the stakes for Tris as she searches for allies and answers in the ruins of a futuristic Chicago.",
        "poster_image_url":"https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg",
        "trailer_youtube_url":"https://youtu.be/sX9-l0iO5w4"
        },
    "3_allegiant":{
        "title": 'The Divergent Series: Allegiant',
        "duration": "unknown",
        "storyline": "After the earth-shattering revelations of INSURGENT, Tris must escape with Four and go beyond the wall enclosing Chicago.",
        "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/f/f8/Allegiantfilmposter.jpg",
        "trailer_youtube_url": "https://youtu.be/5PSNL1qE6VY"
        },
    "4_ascendant":{
        "title": "The Divergent Series: Ascendant",
        "duration": "unknown",
        "storyline": "After Allegiant is Ascendant which is to arrive in 2017",
        "poster_image_url": "http://www.thedivergentseries.movie/ascendant/assets/img/poster/poster.jpg",
        "trailer_youtube_url": "https://youtu.be/6DWqWGwIATQ"
        },
    "5_star_trek":{
        "title": "Star Trek",
        "duration": "2h 8m",
        "storyline": "The greatest adventure of all time begins with Star Trek, the incredible story of a young crew's maiden voyage onboard the most advanced starship ever created: the U.S.S. Enterprise.",
        "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
        "trailer_youtube_url": "https://youtu.be/iGAHnZ555nI"
        },
    "6_star_trek_into_darkness":{
        "title": "Star Trek Into Darkness",
        "duration": "2h 12m",
        "storyline": "When a ruthless mastermind, Khan (Benedict Cumberbatch,) declares a one-man war on the Federation, Captain Kirk (Chris Pine), Spock (Zachary Quinto), and the crew of the U.S.S. Enterprise set out on their most explosive manhunt of all time.",
        "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",
        "trailer_youtube_url": "https://youtu.be/sJNyGFqgyag"
        }
    }

movies = []

for movie_name in sorted(movie_dictionary.keys()):
    movies.append(media.Movie(movie_dictionary[movie_name]))
fresh_tomatoes.open_movies_page(movies)
##print(media.Movie.VALID_RATINGS)

##print(media.Movie.__doc__)




##movies1 = []
##movies2 = []
##
### for movie_name in sorted(movie_dictionary.keys()):
###     movies.append(media.Movie(movie_dictionary[movie_name]))
### fresh_tomatoes.open_movies_page(movies)
### print(media.Movie.VALID_RATINGS)
##
### print(media.Movie.__doc__)
##
##"""
##timeit speedtest as suggested by Peter Rowell see -> http://stackoverflow.com/questions/364519/in-python-how-to-i-iterate-over-a-dictionary-in-sorted-order/364588?noredirect=1#comment54206286_364588
##"""
##
##t1 = timeit.Timer('for k,v in sorted(movie_dictionary.items()): movies2.append(media.Movie(v))', setup="from __main__ import movie_dictionary, movies2; import media")
### while in alone returned 7.55323096123
### while in posistion 1 returned 7.61528725699
### while in posistion 2 returned 11.1439747771
##
##t2 = timeit.Timer('for k in sorted(movie_dictionary.keys()): movies1.append(media.Movie(movie_dictionary[k]))', setup="from __main__ import movie_dictionary, movies1 ; import media")
### while in alone returned 7.30837539539
### while in posistion 1 returned 7.79820640137
### while in posistion 1 returned 12.2386077339
##
##
##
##
####t1r1 = t1.timeit(number=200000)
####print(t1r1)
####t1r2 = t1.repeat(number=200000)
####print(t1r2)
####t1r2 = t1.repeat(number=200000)
####print(t1r2)
##
##t2r1 = t2.timeit(number=200000)
##print(t2r1)
##t2r2 = t2.repeat(number=200000)
##print(t2r2)
##t2r2 = t2.repeat(number=200000)
##print(t2r2)

