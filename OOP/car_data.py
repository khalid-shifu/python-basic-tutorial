class CarData:

    def __init__(self, model, quantity):
        self.__model = model
        self.__quantity = quantity
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    
    def display_info(self):
        print(f"model: {self.__model}, quantity: {self.__quantity}")

    def __str__(self):
        return f"model: {self.__model}, quantity: {self.__quantity}"

        