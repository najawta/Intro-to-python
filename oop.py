# oop
# classes
class Person:
    # constructor
    def __init__(self, name, dob, color, weight, height):
        self.name=name
        self.dob=dob
        self.color=color
        self.weight=weight
        self.height=height
    def display(self):
        print(f"Name is{self.name} and DOB is {self.dob}")

    def get_bmi(self):
        result=self.weight/self.height**2
        return round(result,2)


p1=Person("Fatma Issa","05-03-2003", "Black",58,1.89)
p2= Person("Aisha Moha","02-10-2023","White",189,2.35 )

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")