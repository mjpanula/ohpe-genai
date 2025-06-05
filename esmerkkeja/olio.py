
class Person:
    def __init__(self, nimi, ika, kaupunki):
        self.name = nimi
        self.age = ika
        self.city = kaupunki

    def print_data(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")


person = Person("Ransu", 30, "Helsinki")
person.print_data()

