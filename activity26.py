maths=int(input("please enter your marks in maths:"))
english=int(input("please enter your marks in english"))
ss=int(input("please enter your marks in S.S"))
science=int(input("please enter your marks in science"))
marks=maths+english+ss+science
total=marks/4
if total>=90 and total is total<=100:
    print("you got the grade A1")
elif total>=80 and total is total<=90:
    print("you got the grade A2")
elif total>=65 and total is total<=80:
    print("you got the grade B1")
elif total>=50 and total is total<=65:
    print("you got the grade B2")
elif total>=25 and total is total<=50:
    print("you got the grade C1")
else:
    print("you failed you need to this grade")
    print("call your parents")