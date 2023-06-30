# create a file that has the name,age and gender
class people:
    def __init__(self, name, age, gender):
        self.personname = name
        self.personage = age
        self.persongender = gender

    def display(self):
        print(self.personname, self.personage, self.persongender)


person1 = people("Bilha", "20", "F")
person1.display()
person2 = people("Tom", "50", "M")
person2.display()
person3 = people("Cate", "30", "F")
person3.display()
