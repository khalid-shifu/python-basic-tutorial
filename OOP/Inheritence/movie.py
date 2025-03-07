from media import Media

class Movie(Media):
    def __init__(self, id, title, year, director, theater_id):
        super().__init__(id, title, year)
        self.director = director
        self.theater_id = theater_id


    def display(self):
        return super().display() + f", director: {self.director}, theater_id: {self.theater_id}"
    