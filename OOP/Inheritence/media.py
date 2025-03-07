class Media:

    def __init__(self, id, title, year):
        self.id = id
        self.title = title
        self.year = year
    

    def display(self):
        return f"id: {self.id}, title: {self.title}, year: {self.year}"