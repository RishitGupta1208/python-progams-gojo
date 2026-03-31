theboard={"7":" ","8":" ","9":" ",
          "4":" ","5":" ","6":" ",
          "1":" ","2":" ","3":" "}
boardkey=[]
for key in theboard:
    boardkey.append(key)
def printboard():
    print(theboard["7"] + '|' + theboard["8"] + '|' + theboard["9"])
    print(theboard["4"] + '|' +theboard["5"] + '|' + theboard["6"])
    print(theboard["1"]+ '|' + theboard["2"]+'|'+theboard["9"])
def game():
    turn='X'
    count=0
    for i in range(10):
        printboard(theboard)
        print("its you turn," + turn +".move to which place")
    move=input()
    if theboard[move]== ' ':
        theboard[move]=turn
        count+=1
    else:
        print("the place is aldready filled.\nmove to which place")
    