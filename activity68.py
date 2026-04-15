from abc import ABC,abstractmethod
class Abstractclass(ABC):
    def print(self,x):
        print("passed value: ", x)
    @abstractmethod
    def task(self):
            print("We are at abstractclass task")
class test_class(Abstractclass):
    def task(self):
        print("we are in subclass")
obj=test_class()
obj.task()
obj.print(100)