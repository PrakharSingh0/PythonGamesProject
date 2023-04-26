import random as rd
import time
def game():
    
    diff=input("Choose Your difficulty Easy-Medium-Hard E/M/H:").upper()
    if diff=="E":
        d=10
        attempt=5
    elif diff=='M':
        d=50
        attempt=7
    elif diff=='H':
        d=100
        attempt=10
    else:
        print("invalid Input")
        game()
    
    score=0
    
    num=updateno(d)
    while(attempt>0):
        op=int(input(f"Guess the Number Between 1-{d}:"))
        if op>num:
            print("-----------------------------")
            print("Guess Lower")
            attempt-=1
            score-=2
            print("Attempts:",attempt)
            print("Score:",score)
            print("-----------------------------")
        elif op<num:
            print("-----------------------------")
            print("Guess Higher")
            attempt-=1
            score-=2
            print("Attempts:",attempt)
            print("Score:",score)
            print("-----------------------------")
        else:
            print("-----------------------------")
            print("Correct Guess")
            print("Applause:",applause())
            attempt=5
            score+=10
            num=updateno(d)
            print("Attempts resets:",attempt)
            print("Score:",score)
            print("-----------------------------")
    else:
        print("-----------------------------")
        print("You Loss")
        print("Your Score was:",score)
        print("-----------------------------")
        retry()
    
def retry():
    retry=input("wanna Play Again Y/N:")
    if retry=="y" or retry=="Y":
        game()
    elif retry=="n" or retry=='N':
        print("-----------------------------")
        print("Thanks For Playing See you soon")
        print("Made By Prakhar Singh")
        print("-----------------------------")
        time.sleep(5)
        quit
    else:
        print("invalid input")
        retry()
            
def updateno(upper):
    return rd.randint(1,upper)

def applause():
    ls=["i know you can do it ","your daddy must be proud","you are awesome","Brillient","You are born Intelligent","Keep it Up"]
    return rd.choice(ls)

def start():
    op=input("lets Start the Game Y/N:")
    if op=="y" or op=="Y":
        game()
    elif op=="n" or op=='N':
        quit
    else:
        print("invalid input")
        start()

print("GUESS THE NUMBER".center(100," "))
print(("-"*(40)).center(100," "))
print("For Correct Guess Score : +10 / For Incorrect Guess Score : -2".center(100," "))
print(("-"*(80)).center(100," "))
start()
    