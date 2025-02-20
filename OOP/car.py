class Car:
    def __init__(self, model="unknown", year=0, color="TBA", quantity=0, cng=False):
        self.model = model
        self.year = year
        self.color = color
        self.quantity = quantity
        self.cng = cng

    def set_model(self, model):
        self.model = model
    
    def set_year(self, year):
        self.year = year
    
    def set_color(self, color):
        self.color = color
    
    def set_quantity(self, quantity):
        self.quantity = quantity
    
    def set_cng(self, cng):
        self.cng = cng
    
    def display_info(self):
        print(f"model: {self.model}, year: {self.year}, color: {self.color}, quantity: {self.quantity}, cng: {self.cng}")
