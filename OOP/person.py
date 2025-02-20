class Person:
	
	def __init__(self, name, age, country):
		self.name = name
		self.age = age
		self.country = country
	
	def set_name(self, name):
		self.name = name
	
	def set_age(self, age):
		self.age = age
	
	def set_country(self, country):
		self.country = country

	def display_info(self):
		print(f"name: {self.name}, age: {self.age}, country: {self.country}")	
	
        
	

