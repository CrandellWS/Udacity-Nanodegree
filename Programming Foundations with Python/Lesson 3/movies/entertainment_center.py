import media
from ud036_StarterCode import fresh_tomatoes

## using a dictionary of dictionaries {} = dict()
movie_dictionary = {
    "1_divergent":{
        "title":"Divergent",
        "storyline":"A thrilling action-adventure film set in a world where people are divided into distinct factions based on human virtues.",
        "poster_image_url":"https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
        "trailer_youtube_url":"https://youtu.be/336qJITnDi0"
    },
    "2_insurgent":{
        "title":"The Divergent Series: Insurgent",
        "storyline":"Insurgent raises the stakes for Tris as she searches for allies and answers in the ruins of a futuristic Chicago.",
        "poster_image_url":"https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg",
        "trailer_youtube_url":"https://youtu.be/sX9-l0iO5w4"
        },
    "3_allegiant":{
        "title": 'The Divergent Series: Allegiant',
        "storyline": "After the earth-shattering revelations of INSURGENT, Tris must escape with Four and go beyond the wall enclosing Chicago.",
        "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/f/f8/Allegiantfilmposter.jpg",
        "trailer_youtube_url": "https://youtu.be/5PSNL1qE6VY"
        },
    "4_ascendant":{
        "title": "The Divergent Series: Ascendant",
        "storyline": "After Allegiant is Ascendant which is to arrive in 2017",
        "poster_image_url": "http://www.thedivergentseries.movie/ascendant/assets/img/poster/poster.jpg",
        "trailer_youtube_url": "https://youtu.be/6DWqWGwIATQ"
        },
    "5_star_trek":{
        "title": "Star Trek",
        "storyline": "The greatest adventure of all time begins with Star Trek, the incredible story of a young crew's maiden voyage onboard the most advanced starship ever created: the U.S.S. Enterprise.",
        "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
        "trailer_youtube_url": "https://youtu.be/iGAHnZ555nI"
        },
    "6_star_trek_into_darkness":{
        "title": "Star Trek Into Darkness",
        "storyline": "When a ruthless mastermind, Khan (Benedict Cumberbatch,) declares a one-man war on the Federation, Captain Kirk (Chris Pine), Spock (Zachary Quinto), and the crew of the U.S.S. Enterprise set out on their most explosive manhunt of all time.",
        "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",
        "trailer_youtube_url": "https://youtu.be/sJNyGFqgyag"
        }
    }

movies = []

for movie_name in sorted(movie_dictionary.keys()):
    movies.append(media.Movie(movie_dictionary[movie_name]))
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
