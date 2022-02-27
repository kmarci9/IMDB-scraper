import unittest
from imdb_app_data.moviemodel import MovieModel

from imdb_app_logic.movie_scraper import MovieScraper
from imdb_app_logic.ratingcalculator import RatingCalculator

class Test(unittest.TestCase):
    
    def test_scraper(self):
        scraper = MovieScraper()
        scraper.get_movie_list()
        #self.assertIsNotNone(scraper.topmovies)
        self.assertTrue(len(scraper.topmovies) == 20)

    def test_oscar_calculator(self):
        test_movie = MovieModel(1,"TEST",5,20000,2,"TEST")
        test_list = [test_movie]
        rc = RatingCalculator()
        rc.calculate_oscar_rating(test_list)
        self.assertTrue(test_list[0].adjusted_rating == 5.3)

    def test_review_penalizer(self):
        test_movie = MovieModel(1,"TEST",5,200000,2,"TEST")
        test_list = [test_movie]
        rc = RatingCalculator()
        rc.maxreviews = 500000
        rc.review_penalizer(test_list)
        self.assertTrue(test_list[0].adjusted_rating == 4.7)

if __name__ == "__main__":
     unittest.main()

# python -m unittest unit_tests.py