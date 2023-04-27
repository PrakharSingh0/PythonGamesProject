import random as rd
from collections import Counter

def wordguess():
    word_list=['cat','dog','bat','hat','top','pop','bob','you','she','lap','fat','ace','lol','hug','mug','ram','rom','dam','ham','eat']
    word=rd.choice(word_list)
    return word
guessed=[]

def start():
    p=input("Start the game Y/N :").upper()
    if p=='Y':
        print("-"*50)
        game()
    elif p=='N':
        quit
    else:
        print("invalid input")
        start()

def game():
    word=wordguess()
    print("word : ",end="")
    for i in word: 
        print('_', end=' ')
    print()    
    letterGuessed = ''
    chances = 6
    correct = 0
    flag = 0
    guessedword=[]
    
    while chances!=0 and flag==0:
    
        chances-=1
        guess=input("Guess the the letters : ")
        guessedword.append(guess)
        
        if guess in word:
            k=word.count(guess)
            chances+=1
            guessedword.remove(guess)
            print(stage(chances))
            for _ in range(k):
                letterGuessed += guess
        else:
                print(stage(chances))
            
        print("remaining chance are:",chances)
        print("Wrong Guessed Words are : ",*guessedword)
        print("-"*50)
        print("word : ",end="")
        for char in word:
            if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                print(char,end=" ")
                correct+=1
            elif Counter(letterGuessed)==Counter(word):
                
                print(word)
                flag = 1
                print('Congratulations, You won!')
                print("Man have been rescued")
                print(
             """
              \ o /
                |      thanks buddy 
               / \\
             """)
                break
            else:
                print("_",end=" ")
        print()
    
    a=input("want to save another mans life Y/N : ").upper()
    if a=='Y':
        print("-"*50)
        game()
    elif a=='N':
        print("Bye Have nice Day")
        print("Created By Prakhar Singh")
        quit
    else:
        print("invalid input")
        start()

    
def stage(chance):
    max_attempt=6
    stage=[ """
               +---+
                   |
                   |
                   |
                  ===
           """,
           """
               +---+
               o   |
                   |
                   |
                  ===
           """,
            """
               +---+
               o   |
               |   |
                   |
                  ===
           """,
            """
               +---+
               o   |
              /|   |
                   |
                  ===
           """, """
               +---+
               o   |
              /|\  |
                   |
                  ===
           """, """
               +---+
               o   |
              /|\  |
              /    |
                  ===
           """, """
               +---+
               o   |
              /|\  |
              / \  |
                  ===
            ops Man have died You are unable to save him
           """]
    
    return stage[max_attempt-chance]

print("HangMan The Game".center(100," "))
print(("-"*(40)).center(100," "))
print("Can you save a Innocent man from Hanging".center(100," "))
print("Save the man by Guessing correct words".center(100," "))
print(("-"*(80)).center(100," "))
start()
    