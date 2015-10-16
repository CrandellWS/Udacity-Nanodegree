import media

## using a dictionary of dictionaries {} = dict()
movies = {
    "toy_story":{
        "title":"Toy Story",
        "storyline":"A story of a boy and his toys that come to life",
        "poster_image_url":"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "trailer_youtube_url":"https://youtu.be/vwyZH85NQC4"
        },
    "avatar":{
        "title": "Avatar",
        "storyline": "A marine on an alien planet",
        "poster_image_url": "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.",
        "trailer_youtube_url": "https://youtu.be/5PSNL1qE6VY"
        },
    "the_lion_gaurd":{
        "title": "The Lion Guard: Return of the Roar",
        "storyline": "Meet Kion, son of Simba and Nala, and his best friend Bunga in this sneak peek from The Lion Guard: Return of the Roar, a television movie event premiering in November on Disney Channel!",
        "poster_image_url": "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.",
        "trailer_youtube_url": "https://youtu.be/2toXxKBg-kk"
        }
    }


the_lion_gaurd = media.Movie(movies["the_lion_gaurd"])
print(the_lion_gaurd.storyline)

the_lion_gaurd.show_trailer()


##toy_story = media.Movie(movies["toy_story"])
##print(toy_story.storyline)

##avatar = media.Movie(movies["avatar"])
##print(avatar.storyline)

##avatar.show_trailer()


#### The way that was shown
##
##title = "Toy Story"
##storyline = "A story of a boy and his toys that come to life"
##poster_image_url = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
##trailer_youtube_url = "https://www.youtube.com/watch?v=vwyZH85NQC4"
##
##toy_story = media.Movie(title, storyline, poster_image_url, trailer_youtube_url)
####print(toy_story.storyline)
##
##
##title = "Avatar"
##storyline = "A marine on an alien planet"
##poster_image_url = "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster."
##trailer_youtube_url = "http://www.youtube.com/watch?v=-9ceBgWV8io"
##
##avatar = media.Movie(title, storyline, poster_image_url, trailer_youtube_url)
##print(avatar.storyline)
