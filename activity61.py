class employee():
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructor called")
def createobj():
    print("Making object...")
    obj=employee()
    print("function end")
    return obj
print("calling createobj function")
obj=createobj()
print("program end")