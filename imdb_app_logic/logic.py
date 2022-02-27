

import json
from imdb_app_logic.movie_scraper import MovieScraper
from imdb_app_logic.ratingcalculator import RatingCalculator
from imdb_app_logic.csvwriter import csvWriter


class Logic:

    def __init__(self) -> None:
        """
        Creates logic instance, which executes all necessary calculations
        """
        self.rc = RatingCalculator()


    def WriteToCSV(self):
        """
        Writes movies into movies.csv
        """
        csvWriter.write_to_csv(self.rc.movielist)
    
    



    






