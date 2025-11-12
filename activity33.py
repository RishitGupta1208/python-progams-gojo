At=int(input("please enter your attendence:"))
md=(input("do you have any medical cause:"))
if  md== 'yes' or 'Yes':
    print("you are allowed to do the exam")
else:
    if At>=75:
        print("you are allowed to do the exam")
    else:
        print("you are not allowed")