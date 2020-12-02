import random
score1=score2=0
print("")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Welcome to the COIN game///////////////////////////////////////////////////////////////////////////////")
print("........................................................................................................................................................................................................................................................................................")
n1=input("Enter the name of first player---->")
print("")
n2=input("Enter the name of second player---->")
print("")
r=int(input("--How many rounds u want to play?----"))
print("")
i=1
m=0
if r%2!=0:
    print("Rounds are always be even for equality")
      #  break
while i<=r:
    ran1=random.randint(1,2)
    ran2=random.randint(1,2)
    if m%2==0:
        print(n1,"This is your turn....Predict the result")
        if ran1%2==0:
            t=input("Dear,Guess,What will be the result? HEAD or TAIL")
            if t=='head':
                print("")
                print(n1," Your prediction is wrong")
                score1+=00
            else:
                print("")
                print(n1,"your prediction is right")
                score1+=10
        else:
            t=input("Dear,Guess,What will be the result? HEAD or TAIL")
            if t=='head':
                print("")
                print(n1,"Your prediction is right")
                score1+=10
            else:
                print("")
                print(n1,"Your prediction is wrong")
                score1+=00
    else:
        print(n2,"This is your turn....Predict the result")
        if ran2%2==0:
            t=input("Dear,Guess,What will be the result? HEAD or TAIL")
            if t=='head':
                print("")
                print(n2," Your prediction is wrong")
                score2+=00
            else:
                print("")
                print(n2,"your prediction is right")
                score2+=10
        else:
            t=input("Dear,Guess,What will be the result? HEAD or TAIL")
            if t=='head':
                print("")
                print(n2,"Your prediction is right")
                score2+=10
            else:
                print("")
                print(n2,"Your prediction is wrong")
                score2+=00
    m+=1
    i+=1
print("")
print("")
print("================================================")
print(n1,"Your score",score1)
print(n2,"Your Score",score2)
print("================================================")
if score1>score2:
    print("")
    print('CONGRATULATION')#windows+dot key is used for emojis
    print(n1,",You Won the Game")
if score1<score2:
    print("")
    print('CONGRATULATION')#windows+dot key is used for emojis
    print(n2,",You Won the Game")
else:
    print("")#windows+dot key is used for emojis
    print(" Game Tie")

                
    
        
        
