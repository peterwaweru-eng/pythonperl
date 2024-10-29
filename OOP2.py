#Create a class called person with name, age ,and gender
# as the attribute  a constructor a method and an object


class Person:
    #constructor method

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

        #method
    def display(self):
        print(f"i am {self.name},of age{self.age} and i am a {self.gender}")

  #instance
Myobj=Person("waweru",26,"male")
Myobj.display()