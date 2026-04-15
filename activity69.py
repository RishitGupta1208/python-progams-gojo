from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
     def move(self):
        print(" i can excercise")
class snake(Animal):
     def move(self):
        print(" i can crawl")
class lion(Animal):
     def move(self):
        print(" i can walk and run")
meo=human()
meo.move()
neo=snake()
neo.move()
deo=lion()
deo.move()