# handles our frontend code
import fresh_tomatoes
# file that contains Trailers class
import movies


# list of movies including their Title, storyline and trailer

troy = movies.Trailers(
                    "Troy",
                    "An adaptation of Homer's great epic, the film follows\
                     the assault on Troy by the united Greek forces and\
                     chronicles the fates of the men involved.",
                    "http://www.impawards.com/2004/posters/troy_ver2.jpg",
                    "https://www.youtube.com/watch?v=IKQhUzxlml8")

creed = movies.Trailers(
                    "Creed",
                    "The former World Heavyweight Champion Rocky\
                    Balboa serves as a trainer and mentor to Adonis\
                    Johnson, the son of his late friend and\
                    former rival Apollo Creed.",
                    "http://www.impawards.com/2015/posters/creed.jpg",
                    "https://youtu.be/Uv554B7YHk4")

alfie = movies.Trailers(
                    "Alfie",
                    "A cockney womanizer learns the hard way\
                    about the dangers of his actions.",
                    "http://www.impawards.com/2004/posters/alfie_ver2.jpg",
                    "https://youtu.be/T-whOtC8aak")

hitch = movies.Trailers(
                    "Hitch",
                    "While helping his latest client woo the fine lady of his \
                    dreams, a professional date doctor finds that\
                    his game doesn't quite work on the gossip columnist with \
                    whom he's smitten.",
                    "http://www.impawards.com/2005/posters/hitch_ver2.jpg",
                    "https://youtu.be/dMaq_pfxs-0")

love_jones = movies.Trailers(
                    "Love Jones",
                    "Darius Lovehall is a young black poet in\
                    Chicago who starts dating Nina Moseley, a beautiful and\
                    talented photographer. While trying to figure out if\
                    they've got a love thing or are just kicking it",
                    "http://www.impawards.com/1997/posters/love_jones.jpg",
                    "https://youtu.be/DOYPqcb_jig")

X_Men = movies.Trailers(
                    "X-Men",
                    "They are children of the atom, homo superior, the\
                    next link in the chain of evolution.",
                    "http://www.impawards.com/2000/posters/xmen_ver3.jpg",
                    "https://youtu.be/d-vKUbZYol4")


# array of movies to be shown on fresh_tomatoes movie page
myMovies = [troy, creed, alfie, hitch, love_jones, X_Men]
fresh_tomatoes.open_movies_page(myMovies)
