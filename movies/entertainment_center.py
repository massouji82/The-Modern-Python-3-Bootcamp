import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story', 'A Story of a boy and his toys that come to life', 'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc')

# print(toy_story.storyline)
avatar = media.Movie('Avatar', 'A marine on an alien planet', 'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg', 'https://www.youtube.com/watch?v=aVdO-cx-McA')

# print(avatar.storyline)
# avatar.show_trailer()

interstellar = media.Movie('Interstellar', "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", 'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg', 'https://www.youtube.com/watch?v=zSWdZVtXT7E')
# interstellar.show_trailer()

movies = [toy_story, avatar, interstellar]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__dict__)