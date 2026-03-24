import array as arr
num=arr.array('i',[1,3,5,3,9,7,3])
print(num)
print("the occurence of 3 in the array"+str(num.count(3)))
num.reverse()
print("the reversed array="+str(num))