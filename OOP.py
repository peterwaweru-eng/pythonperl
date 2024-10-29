class Fruits:
    #constructor method
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color

        #method
    def dispay(self):
        print(f"i love eating {self.name}, it cost {self.price},and it is {self.color} in colour")

#instance

myobj=Fruits("banana",20,"yellow")
myobj.dispay()

myobj2=Fruits("mangoes",40,"green")
myobj2.dispay()