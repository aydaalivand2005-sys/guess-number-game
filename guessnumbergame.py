import random 
def bazi():
    ferstnumber=int(input("Enter the starting number of the interval:\n"))
    lastnumber=int(input("Enter the end number of the interval:\n"))
    chance = 3
    robat_number=random.randint(ferstnumber,lastnumber+1)
    while chance > 0 :
        user_number = int(input(f"guess a number between {ferstnumber} and {lastnumber},you have {chance} chance:\n"))
        if user_number == robat_number:
            print("congratulations!!you win.\n")
            break 
        else:
            if chance > 1:
                print ("Oh,I'm sorry,you lost.try again\n")
                if user_number > robat_number:
                    print("the number is lower than your guess.\n")
                else:
                    print("the number is upper than your guess.\n") 
                chance-=1 
                continue
            else:
                print("Oh,dealing,you lost,and you have no chance.")
                break
def main():
    answer = input("Hi,do you want to play?\n if you want , write yes and if you don't , write no:\n")
    if answer == "yes" :
        bazi()
        playagain=input("do you want play again?\n answer with yes or no:\n")
        if playagain == "yes" :
            bazi()
        elif playagain == "no" :
            print("ok,bye.")   
    elif answer == "no" :
        print ("ok,bye.") 
if __name__=="__main__":
    main()    