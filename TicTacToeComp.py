import random
import time

l=[[1,2,3],[4,5,6],[7,8,9]]  #for finding index

m=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #O,X


#Method 1
def printing():
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

def check(n):
    if(n<1 or n>9): 
        print("\nIncorrect Input")
        print("\nYou Lost!!!")
        time.sleep(3)
        quit() #exit() or quit()
    for i in range(3):
        for j in range(3):
            if(n==l[i][j]):
                if(m[i][j]=='X' or m[i][j]=='O'):
                    print("\nIncorrect Input")
                    print("\nYou Lost!!!")
                    time.sleep(3)
                    quit() #exit() or quit()
                m[i][j]='O'
        

def win():

##    for i in range(3):
##        (m[i][0]=='O' and m[i][1]=='O' and m[i][2]=='O')
    #Horizontal Check
    if((m[0][0]=='O' and m[0][1]=='O' and m[0][2]=='O') or
       (m[1][0]=='O' and m[1][1]=='O' and m[1][2]=='O') or
       (m[2][0]=='O' and m[2][1]=='O' and m[2][2]=='O')):
        time.sleep(3)
        print("\nYou Won!!!")
        exit()

    ##  for i in range(3):
##        (m[0][i]=='O' and m[1][i]=='O' and m[2][i]=='O')
    
    #Vertical Check
    elif((m[0][0]=='O' and m[1][0]=='O' and m[2][0]=='O') or
         (m[0][1]=='O' and m[1][1]=='O' and m[2][1]=='O') or
         (m[0][2]=='O' and m[1][2]=='O' and m[2][2]=='O')):
        time.sleep(3)
        print("\nYou Won!!!")
        exit()

    #Diagonal Check
    elif((m[0][0]=='O' and m[1][1]=='O' and m[2][2]=='O') or
         (m[2][0]=='O' and m[1][1]=='O' and m[0][2]=='O')):
        time.sleep(3)
        print("\nYou Won!!!")
        exit()

def compmove():
    ##WINNING
    #Horizontal 1
    if((m[0][0]=='X' and m[0][1]=='X' and m[0][2]==' ')):
        m[0][2]='X'
    elif((m[0][0]=='X' and m[0][1]==' ' and m[0][2]=='X')):
        m[0][1]='X'
    elif((m[0][0]==' ' and m[0][1]=='X' and m[0][2]=='X')):
        m[0][0]='X'

    #Horizontal 2
    elif((m[1][0]=='X' and m[1][1]=='X' and m[1][2]==' ')):
        m[1][2]='X'
    elif((m[1][0]=='X' and m[1][1]==' ' and m[1][2]=='X')):
        m[1][1]='X'
    elif((m[1][0]==' ' and m[1][1]=='X' and m[1][2]=='X')):
        m[1][0]='X'

    #Horizontal 3
    elif((m[2][0]=='X' and m[2][1]=='X' and m[2][2]==' ')):
        m[2][2]='X'
    elif((m[2][0]=='X' and m[2][1]==' ' and m[2][2]=='X')):
        m[2][1]='X'

    elif((m[2][0]==' ' and m[2][1]=='X' and m[2][2]=='X')):
        m[2][0]='X'

    #Vertical 1
    elif((m[0][0]=='X' and m[1][0]=='X' and m[2][0]==' ')):
        m[2][0]='X'
    elif((m[0][0]=='X' and m[1][0]==' ' and m[2][0]=='X')):
        m[1][0]='X'
    elif((m[0][0]==' ' and m[1][0]=='X' and m[2][0]=='X')):
        m[0][0]='X'

    #Vertical 2
    elif((m[0][1]=='X' and m[1][1]=='X' and m[2][1]==' ')):
        m[2][1]='X'
    elif((m[0][1]=='X' and m[1][1]==' ' and m[2][1]=='X')):
        m[1][1]='X'
    elif((m[0][1]==' ' and m[1][1]=='X' and m[2][1]=='X')):
        m[0][1]='X'

    #Vertical 3
    elif((m[0][2]=='X' and m[1][2]=='X' and m[2][2]==' ')):
        m[2][2]='X'
    elif((m[0][2]=='X' and m[1][2]==' ' and m[2][2]=='X')):
        m[1][2]='X'
    elif((m[0][2]==' ' and m[1][2]=='X' and m[2][2]=='X')):
        m[0][2]='X'

    #Diagonal 1
    elif((m[0][0]=='X' and m[1][1]=='X' and m[2][2]==' ')):
        m[2][2]='X'
    elif((m[0][0]=='X' and m[1][1]==' ' and m[2][2]=='X')):
        m[1][1]='X'
    elif((m[0][0]==' ' and m[1][1]=='X' and m[2][2]=='X')):
        m[0][0]='X'

    #Diagonal 2
    elif((m[2][0]=='X' and m[1][1]=='X' and m[0][2]==' ')):
        m[0][2]='X'
    elif((m[2][0]=='X' and m[1][1]==' ' and m[0][2]=='X')):
        m[1][1]='X'
    elif((m[2][0]==' ' and m[1][1]=='X' and m[0][2]=='X')):
        m[2][0]='X'
    
    ##STOPPING PLAYER FROM WINNING
    #Horizontal 1
    elif((m[0][0]=='O' and m[0][1]=='O' and m[0][2]==' ')):
        m[0][2]='X'
    elif((m[0][0]=='O' and m[0][1]==' ' and m[0][2]=='O')):
        m[0][1]='X'
    elif((m[0][0]==' ' and m[0][1]=='O' and m[0][2]=='O')):
        m[0][0]='X'

    #Horizontal 2
    elif((m[1][0]=='O' and m[1][1]=='O' and m[1][2]==' ')):
        m[1][2]='X'
    elif((m[1][0]=='O' and m[1][1]==' ' and m[1][2]=='O')):
        m[1][1]='X'
    elif((m[1][0]==' ' and m[1][1]=='O' and m[1][2]=='O')):
        m[1][0]='X'

    #Horizontal 3
    elif((m[2][0]=='O' and m[2][1]=='O' and m[2][2]==' ')):
        m[2][2]='X'
    elif((m[2][0]=='O' and m[2][1]==' ' and m[2][2]=='O')):
        m[2][1]='X'

    elif((m[2][0]==' ' and m[2][1]=='O' and m[2][2]=='O')):
        m[2][0]='X'

    #Vertical 1
    elif((m[0][0]=='O' and m[1][0]=='O' and m[2][0]==' ')):
        m[2][0]='X'
    elif((m[0][0]=='O' and m[1][0]==' ' and m[2][0]=='O')):
        m[1][0]='X'
    elif((m[0][0]==' ' and m[1][0]=='O' and m[2][0]=='O')):
        m[0][0]='X'

    #Vertical 2
    elif((m[0][1]=='O' and m[1][1]=='O' and m[2][1]==' ')):
        m[2][1]='X'
    elif((m[0][1]=='O' and m[1][1]==' ' and m[2][1]=='O')):
        m[1][1]='X'
    elif((m[0][1]==' ' and m[1][1]=='O' and m[2][1]=='O')):
        m[0][1]='X'

    #Vertical 3
    elif((m[0][2]=='O' and m[1][2]=='O' and m[2][2]==' ')):
        m[2][2]='X'
    elif((m[0][2]=='O' and m[1][2]==' ' and m[2][2]=='O')):
        m[1][2]='X'
    elif((m[0][2]==' ' and m[1][2]=='O' and m[2][2]=='O')):
        m[0][2]='X'

    #Diagonal 1
    elif((m[0][0]=='O' and m[1][1]=='O' and m[2][2]==' ')):
        m[2][2]='X'
    elif((m[0][0]=='O' and m[1][1]==' ' and m[2][2]=='O')):
        m[1][1]='X'
    elif((m[0][0]==' ' and m[1][1]=='O' and m[2][2]=='O')):
        m[0][0]='X'

    #Diagonal 2
    elif((m[2][0]=='O' and m[1][1]=='O' and m[0][2]==' ')):
        m[0][2]='X'
    elif((m[2][0]=='O' and m[1][1]==' ' and m[0][2]=='O')):
        m[1][1]='X'
    elif((m[2][0]==' ' and m[1][1]=='O' and m[0][2]=='O')):
        m[2][0]='X'

    elif(m[1][1]==' '):
        m[1][1]='X'
        
    else:
    #Random
        for i in range(10):
            a=random.randint(0,2) #row index
            b=random.randint(0,2) #column index
            if(m[a][b]=='X' or m[a][b]=='O'):
                continue
            else:
                m[a][b]='X'
            break

def loss():
    #Horizontal Check
    if((m[0][0]=='X' and m[0][1]=='X' and m[0][2]=='X') or
       (m[1][0]=='X' and m[1][1]=='X' and m[1][2]=='X') or
       (m[2][0]=='X' and m[2][1]=='X' and m[2][2]=='X')):
        time.sleep(3)
        print("\nYou Lost!!!")
        exit()
        
    #Vertical Check
    elif((m[0][0]=='X' and m[1][0]=='X' and m[2][0]=='X') or
         (m[0][1]=='X' and m[1][1]=='X' and m[2][1]=='X') or
         (m[0][2]=='X' and m[1][2]=='X' and m[2][2]=='X')):
        time.sleep(3)
        print("\nYou Lost!!!")
        exit()

    #Diagonal Check
    elif((m[0][0]=='X' and m[1][1]=='X' and m[2][2]=='X') or
         (m[2][0]=='X' and m[1][1]=='X' and m[0][2]=='X')):
        time.sleep(3)
        print("\nYou Lost!!!")
        exit()


def work():
    n=int(input("Enter the number where you want your circle(1-9) : "))
    check(n) #
    printing() #
    win()

    #Compmove
    print("The Computer chose this :")
    compmove()
    printing()
    loss()


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

for i in range(4):
    work()

time.sleep(3)
n=int(input("Enter the number where you want your circle(1-9) : "))
check(n)
printing()
win()
time.sleep(3)
print("DRAW!!")
