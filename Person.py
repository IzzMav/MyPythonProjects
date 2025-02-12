class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self.age = age
    def get_name(self):
        return self._name
    def get_surname(self):
        return self._surname
    def get_age(self):
        return self.age
    def set_name(self, new_name):
        self._name = new_name
    def set_surname(self, new_surname):
        self._surname = new_surname
    def set_age(self, new_age):
        new_age = int(input())
        while new_age == 0:
            print ("Please insert a valid age!")
            new_age = int(input())
        self.age = new_age

p = Person ("","",0)
print("please insert a name, surname and an age to the Person")
p.set_name(input("Name: "))
p.set_surname(input("Surname: "))
print("Age: ")
p.set_age(0)
print("")
print("His/Her name is", p.get_name(), p.get_surname(),"an he's/she's", p.get_age(),"old")
