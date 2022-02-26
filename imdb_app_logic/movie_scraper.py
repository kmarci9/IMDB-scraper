from subprocess import list2cmdline
import imdb
import requests

from imdb_app_data.moviemodel import MovieModel



class MovieScraper:
    
    def __init__(self):
        self.ia = imdb.Cinemagoer()
        self.topmovies = self.__get_top_250_movies()

    def __get_oscar_by_movie_id(self, imdb_id : str) -> int:
        """
        Returns oscar number using OMDB API for a given movie by imdbID
        """
        URL = "https://www.omdbapi.com/?i=" + imdb_id +"&apikey=b3d08b0c"
        response = requests.post(URL)
        parsed_dict = response.json()
        awards =  parsed_dict['Awards']
        print ( imdb_id +" " + awards)
        oscars  = 0
        if ("Won ") in awards:
            split_list = awards.split(' ')
            index = int(awards.split(' ').index('Won') + 1)
            oscars = int(split_list[index])
        return oscars

    def __get_top_250_movies(self):
        """
        Gets top 250 movies from IMDB
        """
        top = self.ia.get_top250_movies()
        return top[0:20]

    def get_movie_list(self) -> list:
        """
        fills up movielist with movieModel
        """
        movielist = []
        for movie in self.topmovies:
            rating = movie.data['rating']
            title = movie.data['title']
            rank = movie.data['top 250 rank']
            ratings = movie.data['votes']
            imdb_id = "tt" + str(movie.movieID)
            oscars = self.__get_oscar_by_movie_id(imdb_id)
            model = MovieModel(rank,title,rating,ratings,oscars,imdb_id)
            movielist.append(model)
        return movielist