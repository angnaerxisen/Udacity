class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,release_date):
        """ This uesed for show what kind of elements on the websites"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
       
    def show_trailer(self):
        """This explains what it does to show when you open the browser\
        it will open the trailer_youtube_url"""
        webbrowser.open(self.trailer_youtube_url)
