import fresh_tomatoes
import media

# Dead pool the story line ,poster and treailer find on IMDB ,cool websites

dead_pool = media.Movie(
    "Dead Pool",
    "A fast-talking mercenary with a morbid sense of humor is subjected to\
         a rogue experiment that leaves him with accelerated healing powers and \
         a quest for revenge.",
    # naqa
   "http://bit.ly/2m5Kw07",
   "https://www.youtube.com/watch?v=17CUxUduw-g"
)

# Shawshank redepemtion
Shawshank_redepemtion = media.Movie(
    "Shawshank redepemtion",
    "Two imprisoned men bond over a number of years,\
             finding solace and eventual redemption\
              through acts of common decency.",
    # naqa
    "http://bit.ly/2e2Yn28",
    "https://www.youtube.com/watch?v=6hB3S9bIaco"
)

# batman VS superman

Batman_VS_Superman = media.Movie(
    "Batman VS Superman",
    "Two DC superhero fight on the City",
    # naqa
    "http://bit.ly/2hvTqP9",
    "https://www.youtube.com/watch?v=0WWzgGyAH6Y"
)

# killsing Bills Vol 2
Killing_Bills_Vol_2 = media.Movie(
    "Killing Bills Vol 2",
    "A Woman's revenge her boss",
    # napa
    "http://bit.ly/2lnggKh",
    "https://www.youtube.com/watch?v=WTt8cCIvGYI"
)

# Zootopia
Zootopia = media.Movie("Zootopia",
                       "In a city of anthropomorphic animals,\
                 a rookie bunny cop and a cynical con artist \
                 fox must work together to uncover a conspiracy.",
                       # naqa
                       "http://bit.ly/2m5Nphr",
                       "https://www.youtube.com/watch?v=yCOPJi0Urq4"
                       )

# Account
The_Accountant = media.Movie("The Accountant",
                             "As a math savant uncooks the books for a new client, \
                             the Treasury Department closes in on his activities \
                            and the body count starts to rise.",
                             # napa
                             "http://bit.ly/2mr9QPd",
                             "http://www.imdb.com/video/imdb/vi2433726233?playlistId=tt2140479&ref_=tt_ov_vi"
                             )


movies = [dead_pool, Shawshank_redepemtion, Batman_VS_Superman,
          Killing_Bills_Vol_2, Zootopia, The_Accountant]
fresh_tomatoes.open_movies_page(movies)

print(media, movie, valid_ratings)
