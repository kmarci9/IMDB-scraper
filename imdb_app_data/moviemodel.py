
class MovieModel:
    """
    Movie Model containing the essential data
    """
    def __init__(self,rank : int,title : str,rating : float,user_ratings : int,oscar_num : int, imdb_id : str):
        self.rank = rank
        self.title = title
        self.rating = rating
        self.user_ratings = user_ratings
        self.oscar_num = oscar_num
        self.imdb_id = imdb_id
        self.adjusted_rating = rating
