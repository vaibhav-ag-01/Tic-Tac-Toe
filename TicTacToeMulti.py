import random
import time

l=[[1,2,3],[4,5,6],[7,8,9]]  #for finding index

m=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #O,X

class TicTacToe:
    #Method 1
    def __init__(self,q):
        self.q=q
    
    def printing(self):
        time.sleep(2)
        print("\n\n")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(m[0][0],m[0][1],m[0][2]))
        print("_____|_____|_____")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(m[1][0],m[1][1],m[1][2]))
        print("_____|_____|_____")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(m[2][0],m[2][1],m[2][2]))
        print("     |     |     ")
        print("\n\n")
        time.sleep(2)

    def check(self,n):
        if(n<1 or n>9): 
            print("\nIncorrect Input")
            print("\n{} Lost!!!".format(self.name))
            time.sleep(3)
            quit() #exit() or quit()
        for i in range(3):
            for j in range(3):
                if(n==l[i][j]):
                    if(m[i][j]=='X' or m[i][j]=='O'):
                        print("\nIncorrect Input")
                        print("\n{} Lost!!!".format(self.name))
                        time.sleep(3)
                        quit() #exit() or quit()
                    m[i][j]=self.q
            

    def win(self):
        #Horizontal Check
        if((m[0][0]==self.q and m[0][1]==self.q and m[0][2]==self.q) or
           (m[1][0]==self.q and m[1][1]==self.q and m[1][2]==self.q) or
           (m[2][0]==self.q and m[2][1]==self.q and m[2][2]==self.q)):
            time.sleep(3)
            print("\n{} Won!!!".format(self.name))
            exit()
            
        #Vertical Check
        elif((m[0][0]==self.q and m[1][0]==self.q and m[2][0]==self.q) or
             (m[0][1]==self.q and m[1][1]==self.q and m[2][1]==self.q) or
             (m[0][2]==self.q and m[1][2]==self.q and m[2][2]==self.q)):
            time.sleep(3)
            print("\n{} Won!!!".format(self.name))
            exit()

        #Diagonal Check
        elif((m[0][0]==self.q and m[1][1]==self.q and m[2][2]==self.q) or
             (m[2][0]==self.q and m[1][1]==self.q and m[0][2]==self.q)):
            time.sleep(3)
            print("\n{} Won!!!".format(self.name))
            exit()


    def work(self):
        n=int(input("{} enter the number where you want your input(1-9) : ".format(self.name)))
        self.check(n) #
        self.printing() #
        self.win()

    def naming(self):
        self.name = input("Enter your name : ")
        time.sleep(2)

#MAIN WORKING

print("Hello!\nWelcome to TicTacToe vs Computer")
time.sleep(3)
print("\n\n This is your board,\nRemember the position of numbers")
time.sleep(2)
print("\n\n")
print("     |     |     ")
print("  {}  |  {}  |  {}  ".format(l[0][0],l[0][1],l[0][2]))
print("_____|_____|_____")
print("     |     |     ")
print("  {}  |  {}  |  {}  ".format(l[1][0],l[1][1],l[1][2]))
print("_____|_____|_____")
print("     |     |     ")
print("  {}  |  {}  |  {}  ".format(l[2][0],l[2][1],l[2][2]))
print("     |     |     ")
time.sleep(8)
print("\n\nBy entering the number\nyou will get a circle at that place\n")
time.sleep(3)

p1 = TicTacToe('O')
p2=TicTacToe('X')

p1.naming()
p2.naming()
print("\n\n")
for i in range(4):
    p1.work()
    p2.work()

time.sleep(3)
n=int(input("{} enter the number where you want your input(1-9) : ".format(self.name)))
p1.check(n)
p1.printing()
p1.win()
time.sleep(3)
print("DRAW!!")
