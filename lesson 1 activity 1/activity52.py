numbers1=[1,9,7]
numbers2=[2,4,2]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))
def square(n):
    return n*n
numdx=list(map(square,numbers1))
print(numdx)