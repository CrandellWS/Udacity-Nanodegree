import media
from ud036_StarterCode import fresh_tomatoes

## using a dictionary of dictionaries {} = dict()
movie_dictionary = {
    "toy_story":{
        "title":"Toy Story",
        "storyline":"A story of a boy and his toys that come to life",
        "poster_image_url":"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "trailer_youtube_url":"https://youtu.be/vwyZH85NQC4"
        },
    "avatar":{
        "title": "Avatar",
        "storyline": "A marine on an alien planet",
        "poster_image_url": "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
        "trailer_youtube_url": "https://youtu.be/5PSNL1qE6VY"
        },
    "the_lion_gaurd":{
        "title": "The Lion Guard: Return of the Roar",
        "storyline": "Meet Kion, son of Simba and Nala, and his best friend Bunga in this sneak peek from The Lion Guard: Return of the Roar, a television movie event premiering in November on Disney Channel!",
        "poster_image_url": "http://cdn03.cdn.justjaredjr.com/wp-content/uploads/headlines/2015/10/disney-dates-lion-guard-movie-key-art.jpg",
        "trailer_youtube_url": "https://youtu.be/2toXxKBg-kk"
        }
    }


the_lion_gaurd = media.Movie(movie_dictionary["the_lion_gaurd"])
toy_story = media.Movie(movie_dictionary["toy_story"])
avatar = media.Movie(movie_dictionary["avatar"])

movies = [avatar, toy_story, the_lion_gaurd, avatar, toy_story, the_lion_gaurd]

fresh_tomatoes.open_movies_page(movies)
