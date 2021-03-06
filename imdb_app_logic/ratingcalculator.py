from imdb_app_logic.movie_scraper import MovieScraper
import math
class RatingCalculator:

    def __init__(self) -> None:
        scraper = MovieScraper()
        self.movielist = scraper.get_movie_list()
        self.maxreviews = 0
        self.__getmaxreviews(self.movielist)
        self.calculate_oscar_rating(self.movielist)
        self.review_penalizer(self.movielist)


    def calculate_oscar_rating(self,movielist : list):
        """
        writes adjusted rating based on number of oscars
        """
        for movie in movielist:
            if (movie.oscar_num == 1 or movie.oscar_num == 2):
                movie.adjusted_rating = movie.adjusted_rating + 0.3
            elif (movie.oscar_num >= 3 and movie.oscar_num <= 5):
                movie.adjusted_rating = movie.adjusted_rating + 0.5
            elif (movie.oscar_num >= 6 and movie.oscar_num <= 10):
                movie.adjusted_rating = movie.adjusted_rating + 1
            elif movie.oscar_num > 10:
                movie.adjusted_rating = movie.adjusted_rating + 1.5

    def __getmaxreviews(self,movielist : list):
        """
        Gets maximum reviews
        """
        for movie in movielist:
            #print (movie.user_ratings)
            if self.maxreviews < movie.user_ratings:
                self.maxreviews = movie.user_ratings

    def review_penalizer(self, movielist: list):
        """
        Penalizes movies with low reviews
        """
        for movie in movielist:
            difference = math.floor((self.maxreviews - movie.user_ratings)/100000)
            if difference > 0:
                val_to_sub = difference * 0.1
                movie.adjusted_rating -= val_to_sub
