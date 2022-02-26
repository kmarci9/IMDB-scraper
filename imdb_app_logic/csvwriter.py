import csv

class csvWriter:

    @staticmethod
    def write_to_csv(movie_list: list) -> None:
        """
        Writes out movie_list to movies.csv
        """
        header = ["Rank","Title","Rating","Adjusted Rating","Votes","Oscars","imdb_id"]
        with open('movies.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f,delimiter =';')
            writer.writerow(header)
            for movie in movie_list:
                writer.writerow([movie.rank, movie.title,movie.rating,round(movie.adjusted_rating,2),movie.user_ratings,movie.oscar_num,movie.imdb_id])
