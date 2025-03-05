from person import Person
from car import Car
from print import Print
from car_data import CarData
from person_data import PersonData
from movie_data import MovieData
from anime_data import AnimeData

def main():
    p1 = Person("john", 25, "Korea")
    p1.display_info()

    car1 = Car("Toyota", 2019, "Red", 10, True)
    car1.display_info()

    car2 = Car()
    car2.display_info()

    car3 = Car("Suzuki", quantity=5, cng=False)
    car3.display_info()

    printer = Print("Hello World")
    printer.display_message()

    car_data = CarData("Toyota", 12)
    print(car_data)

    car_data.model = "Suzuki"
    car_data.quantity = 15
    print(car_data)

    person1 = PersonData("john", 25, 48000, True)
    print(person1)

    person2 = PersonData("jane")
    print(person2)


    movie1 = MovieData("M01220", "The Dark Knight", 2008, "Action", 9.0)
    print(movie1)

    anime1 = AnimeData("A01001", "Naruto", "Fiction", 8.5, 220)
    print(anime1)

# client code
if __name__ == "__main__":
    main()



# notes
# 1. instead of getter, setter use @property and @<property_name>.setter
# 2. instead of using display_info() method, use __str__ method
# 3. if we do not have __eq__ car1 == car2 checks object reference, if we have __eq__ then car1 == car2 checks values 
# 4. __repr__ is used to represent object in string format
# 5. __str__ is used to represent object in string format
# 6. difference between str and repr is that str is used for end user and repr is used for developer