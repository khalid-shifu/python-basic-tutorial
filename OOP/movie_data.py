class MovieData:

    def __init__ (self, id, title, year, genre, rating):
        self.__id = id
        self.__title = title
        self.__year = year 
        self.__genre = genre
        self.__rating = rating

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title

    @property 
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year
    
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def fenre(self, genre):
        self.__genre = genre
    
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    def __str__(self):
        return f"id: {self.__id}, title: {self.__title}, year: {self.__year}, genre: {self.__genre}, rating: {self.__rating}"
    
    


