import fresh_tomatoes
import movies

troy = movies.Trailers(
                    "Troy",
                    "An adaptation of Homer's great epic, the film follows the assault on Troy by the united Greek forces and chronicles the fates of the men involved.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk5MzU1MDMwMF5BMl5BanBnXkFtZTcwNjczODMzMw@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=IKQhUzxlml8")
print(troy.storyline)
creed = movies.Trailers(
                    "Creed",
                    "The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.",
                    "http://www.impawards.com/2015/posters/creed.jpg",
                    "https://youtu.be/Uv554B7YHk4")

#print(avatar.storyline)

alfie = movies.Trailers(
                    "Alfie",
                    "A cockney womanizer learns the hard way about the dangers of his actions.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNTBjOWQwZDEtZWRlYi00YzY0LTg3NDQtYzRiYjk2YjMyMzEyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                    "https://youtu.be/T-whOtC8aak")

hitch = movies.Trailers(
                    "Hitch",
                    "While helping his latest client woo the fine lady of his dreams, a professional date doctor finds that his game doesn't quite work on the gossip columnist with \
                    whom he's smitten.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzYyNzM2NzM2NF5BMl5BanBnXkFtZTcwNjg5NTQzMw@@._V1_SY1000_CR0,0,659,1000_AL_.jpg",
                    "https://youtu.be/dMaq_pfxs-0")

love_jones = movies.Trailers(
                    "Love Jones",
                    "Darius Lovehall is a young black poet in Chicago who starts dating Nina Moseley, a beautiful and talented photographer. While trying to figure out if they've got a \
                    love thing or are just kicking it",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2NjYxMDczNV5BMl5BanBnXkFtZTcwODAwODAyMQ@@._V1_.jpg",
                    "https://youtu.be/DOYPqcb_jig")

love_and_basketball = movies.Trailers(
                    "Love and Basketball",
                    "Monica (Sanaa Lathan) and Quincy (Omar Epps) are two childhood friends who both aspire to be professional basketball players.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU4NjY4NTI5MF5BMl5BanBnXkFtZTYwNjQ4OTc3._V1_.jpg",
                    "https://youtu.be/Ur83i6_BjbE")



myMovies = [troy, creed, alfie, hitch, love_jones, love_and_basketball]
fresh_tomatoes.open_movies_page(myMovies)
