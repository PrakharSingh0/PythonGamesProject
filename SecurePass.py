import random as rd
import array 

def start():
    a=input("Genrate Password Y/N :").upper()
    if a=='Y':
        gen()
    elif a=='N':
        quit
    else:
        print("invalid input")
        start()
        
        
def gen():
    
    maxlen=12
    
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowerA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    upperA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

    comlist=digit+lowerA+upperA+symbol
    
    rand_D=rd.choice(digit)
    rand_L=rd.choice(lowerA)
    rand_U=rd.choice(upperA)
    rand_S=rd.choice(symbol)
    
    temp_pass=rand_D+rand_L+rand_U+rand_S
    
    for i in range(maxlen-4):
        temp_pass+=rd.choice(comlist)
        
        temp_pass_list=array.array('u',temp_pass)
        rd.shuffle(temp_pass_list)
        
    password=''
    for x in temp_pass_list:
        password+=x
    
    print("-"*40)
    
    print("Your Genrated password is :",password)

    start()
    


print("Strong Password Genrator".center(100," "))
print(("-"*(40)).center(100," "))
start()
    