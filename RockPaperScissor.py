import random as rd
import time 

#game mode selection
def game():
    print("-"*40)
    gm=input("Play Agains Computer or player C/P:")
    
    if gm=="c" or gm=="C":
        comp()
    elif gm=="p" or gm=='P':
        player()
    else:
        print("invalid input")
        game()  
        
# Computer as Op
def comp():
    print("-"*40)
    attempt=5
    score=0
    while(attempt>0):
        userchoice=input("Enter your Option R/P/S:").upper()
        compchoice=compSelect()
        
        # HERE GAME BEGIN
        print("-"*40)
        if userchoice == compchoice:
            print(f"Both players and computer choose {userchoice}. It's a tie!")
            status(attempt,score)
        elif userchoice == "R":
            if compchoice == "S":
                print("Rock smashes scissors! You win!")
                attempt=5
                score+=10
                status(attempt,score)
            else:
                print("Paper covers rock! You lose.")
                attempt-=1
                score-=2
                status(attempt,score)
        elif userchoice == "P":
            if compchoice == "R":
                print("Paper covers rock! You win!")
                attempt=5
                score+=10
                status(attempt,score)
            else:
                print("Scissors cuts paper! You lose.")
                attempt-=1
                score-=2
                status(attempt,score)
        elif userchoice == "S":
            if compchoice == "P":
                print("Scissors cuts paper! You win!")
                attempt=5
                score+=10
                status(attempt,score)
            else:
                print("Rock smashes scissors! You lose.")
                attempt-=1
                score-=2
                status(attempt,score)
        else:
            print("Invalid Input please Enter Your Choice From R/P/S")
                     
        print("-"*20)
    
    else:
        print("it look like your born to loss")
        print("Your Score WAS:",score)
        retryc()
        
# Retry     
def retryc():
    retry=input("wanna Play Again Y/N:")
    if retry=="y" or retry=="Y":
        comp()
    elif retry=="n" or retry=='N':
        print("-----------------------------")
        print("Thanks For Playing See you soon")
        print("Made By Prakhar Singh")
        print("-----------------------------")
        time.sleep(5)
        quit
    else:
        print("invalid input")
        retryc()



def compSelect():
    ls=['R','P','S']
    return rd.choice(ls)        

#print scoreboard
def status(a,s):
    print("your Score:",s)
    print("Your Attempt left:",a)


# player as Op
def player():
    turn=int(input("Enter No of Round You wanna Play:"))
    
    p1score=0
    p2score=0
    
    for _ in range(turn):
    
        p1=input("Player 1:Enter your Option R/P/S:").upper()
        p2=input("Player 2:Enter your Option R/P/S:").upper()
        
        print("-"*20)
        # HERE GAME BEGIN

        if p1 == p2:
                print(f"Both players and computer choose {p1}. It's a tie!")
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
        elif p1 == "R":
            if p2 == "S":
                print("Rock smashes scissors! Player 1 win!")
                p1score+=10
                p2score-=2
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
            else:
                print("Paper covers rock! Player 2 win!")
                p1score-=2
                p2score+=10
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
        elif p1 == "P":
            if p2 == "R":
                print("Paper covers rock! Player 1 win!")
                p1score+=10
                p2score-=2
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
            else:
                print("Scissors cuts paper! Player 2 win!")
                p1score-=2
                p2score+=10
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
                
                
        elif p1 == "S":
            if p2 == "P":
                print("Scissors cuts paper! Player 1 win!")
                p1score+=10
                p2score-=2
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
                
            else:
                print("Rock smashes scissors! Player 2 win!")
                p1score-=2
                p2score+=10
                print("Player 1 Score:",p1score)
                print("Player 2 Score:",p2score)
        else:
            print("Invalid Input please Enter Your Choice From R/P/S")
                
    print("-"*20)
    
    # Final Victory
    if p1score>p2score:
        print("Player 1 Won the Game")
    elif p1score==p2score:
        print("Draw")
    else:
        print("Player 2 Won the Game")
        
#start The game 
def start():
    op=input("lets Start the Game Y/N:")
    if op=="y" or op=="Y":
        game()
    elif op=="n" or op=='N':
        quit
    else:
        print("invalid input")
        start()
#main
print("Rock paper Scissor".center(100," "))
print(("-"*(40)).center(100," "))
print("For Win Score : +10 / For Loss Score : -2".center(100," "))
print(("-"*(80)).center(100," "))
start()