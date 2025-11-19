ui=int(input(" please enter to check: "))
sum=0
temp=ui
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp //=10
if ui==sum:
    print(" the number is an armstrong number ")
else:
    print(" the number is not an armstrong number ")