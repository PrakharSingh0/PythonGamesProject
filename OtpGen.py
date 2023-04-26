import random as rd
import string

def OTP(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return rd.randint(range_start, range_end)

def start():
    print("-"*(40))
    ch=input("Numeric OR AlphaNumeric OPT N/A:").upper()
    if ch=='N':
        numOTP()
    elif ch=='A':
        alphaNumOTP()
    else:
        print("Invalid Input")

#OTP Gen

def numOTP():
    print("-"*(40))
    n=int(input("enter no of digit of OTP:"))
    print(OTP(n))
    retryn()
    
def alphaNumOTP():
    N=int(input("Enter OTP lenght:"))
    res = ''.join(rd.choices(string.ascii_uppercase +  string.digits, k = N)) 
    print("The random string : " + str(res))
    retrya()
    
# Retry
    
def retrya():
    retry=input("wanna Genrate Again Y/N:")
    if retry=="y" or retry=="Y":
        alphaNumOTP()
    elif retry=="n" or retry=='N':
        print("-----------------------------")
        print("Thanks you for using OTP GEN")
        print("Made By Prakhar Singh")
        print("-----------------------------")
        quit
    else:
        print("invalid input")
        retrya()
        
def retryn():
    retry=input("wanna Genrate Again Y/N:")
    if retry=="y" or retry=="Y":
        numOTP()
    elif retry=="n" or retry=='N':
        print("-----------------------------")
        print("Thanks you for using OTP GEN")
        print("Made By Prakhar Singh")
        print("-----------------------------")
        quit
    else:
        print("invalid input")
        retryn()
        
#main
print("OTP Genrator".center(100," "))
print(("-"*(40)).center(100," "))
start()