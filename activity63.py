class person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print("your name is: ",self.name)
        print("your id number is: ",self.id_number)
class employee(person):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        super().__init__(name,id_number)
obj=employee('Rohan',1453277,56770,'general manager')
obj.display()