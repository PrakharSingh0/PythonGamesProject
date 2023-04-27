import random as rd
import keyboard as kw  # pip install keyboard to run it 
def game():
    print("To through a Dice Press SPACE and to exit Press ESC ")
    ls=[]
    while True:
        kw.read_key()
        
        if kw.is_pressed("esc"):
            print("Exiting the game")
            break
        elif kw.is_pressed("space"):
            print("-"*30)
            dice=rd.randint(1,6)
            print("you rolled :",dice)
            ls.append(dice)
            print("your rolled dice faces are:",ls)
        

print("Game of Dice".center(100," "))
print(("-"*(40)).center(100," "))
game()
    