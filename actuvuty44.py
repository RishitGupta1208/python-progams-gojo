ui=int(input(" please enter number 1: "))
ui2=int(input(" please enter number2: "))
temp2=ui
temp3=ui2
while (ui2!=0):
    temp=ui2
    ui2=ui%ui2
    ui=temp
hcf=ui
print("\nHCF of", temp2, "and", temp3,"is",hcf)