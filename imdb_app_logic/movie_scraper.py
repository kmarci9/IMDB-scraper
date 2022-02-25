import imdb
import requests



class MovieScraper:
    
    def __init__(self):
        self.ia = imdb.Cinemagoer()
        self.topmovies = self.__get_top_250_movies()
        self.movielist = []
        self.__setup_movielist()


    def __get_oscar_by_movie_id(self, imdb_id : str) -> int:
        """
        Returns oscar number for a given movie by imdbID
        """
        URL = "https://www.omdbapi.com/?i=tt0167260&apikey=b3d08b0c"

        response = requests.post(URL)

        parsed_dict = response.json()

        awards =  parsed_dict['Awards']
        print (awards)
        oscars  = 0
        if ("Won ") in awards:
            index = awards.index("Won ")
            print (index)
        return oscars

    def __get_top_250_movies(self):
        """
        Gets top 250 movies from IMDB
        """
        top = self.ia.get_top250_movies()
        return top[0:20]

    def __setup_movielist(self):
        for movie in self.topmovies:
            rating = movie.data['rating']
            title = movie.data['title']
            rank = movie.data['top 250 rank']
            ratings = movie.data['votes']
            imdb_id = "tt" + str(movie.movieID)
            oscars = self.__get_oscar_by_movie_id(imdb_id)