'''''
Author: Jonas Toussaint
Assignment: Asignment 7
Purpose: Create a python tic-tac-toe game program using loops 
and functions
'''
#import
import os 
import time
import random

#Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " " , " ", " ", " ", " ", " ", " ", " "]
x = 0
y = 0
o = 0
ca =0
ans = True 

#Print the header
def print_header():
    print('''
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    1 | 2 | 3 | 4
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      5 | 6 | 7 | 8
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     9 | 10| 11| 12
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\    13| 14| 15| 16
                                                            
 To play Tic-Tac-Toe, you need to get three in a row...
 Your choices are defined, they must be from 1 to 16...

''')

#Define the print_board functions
def print_board():
    print("   |   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" | "+board[4])
    print("   |   |   |   ")
    print("---|---|---|---")
    print("   |   |   |   ")
    print(" "+board[5]+" | "+board[6]+" | "+board[7]+" | "+board[8])
    print("   |   |   |   ")
    print("---|---|---|---")
    print("   |   |   |   ")
    print(" "+board[9]+" | "+board[10]+" | "+board[11]+" | "+board[12])
    print("   |   |   |   ")
    print("---|---|---|---")
    print("   |   |   |   ")
    print(" "+board[13]+" | "+board[14]+" | "+board[15]+" | "+board[16])
    print("   |   |   |   ")
    
#Define a function to make sure the user inputs a number
def inputValidation(message):
    while True:
        try:          
            userInput = int(input(message))
            
        except ValueError:
            print("Not a integer! Try Again.")
            continue
        else:            
            return userInput      
       
def continueAgain():
    global ca
    global x
    global y
    global o
 
    if x == 3:
        print("X wins!")
        return False   
       
    elif y == 3:
        print("Y wins!")
        return False   
     
    elif o == 3:
        print("O wins!")
        return False  
    
    elif ca== 4:
         print("    Tie     ")
         return False   
    
    while True:  
        option = input("Do you want to continue again? Y/N ")
  
        if(option == "Y" or option == "y"):
            ca +=1
            clearTable()
            return True
                
        elif option == "N" or option == "n":
            os.system("clear")
            print_header()
            print("     Good Bye!     ")
            return False      
            
def clearTable():
    global board
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " " , " ", " ", " ", " ", " ", " ", " "]
    os.system("clear")
    print_header()
    print_board()
   
def TicTacToe():
    
    global board
    global x
    global y
    global o
     
    while True:
        os.system("clear")
        print_header()
        print_board()
        choice = inputValidation("Please choose an empty space for X. ")
        
        while board[choice] != " ":            
            print("Sorry, That space is not empty")
            time.sleep(1)
            choice = inputValidation("Please choose an empty space for X. ") 
        board[choice] = "X"  
                
        #Check for X win 
        if (board[1] == "X" and board[2] == "X" and board[3] == "X" and board[4] == "X" or #1st row
            board[5] == "X" and board[6] == "X" and board[7] == "X" and board[8] == "X" or #2nd row
            board[9] == "X" and board[10] == "X" and board[11] == "X" and board[12] == "X" or #3rd row
            board[13] == "X" and board[14] == "X" and board[15] == "X" and board[16] == "X" or #4th row
            board[1] == "X" and board[5] == "X" and board[9] == "X" and board[13] == "X" or #1st col
            board[2] == "X" and board[6] == "X" and board[10] == "X" and board[14] == "X" or #2nd col
            board[3] == "X" and board[7] == "X" and board[11] == "X" and board[15] == "X" or #3rd col
            board[1] == "X" and board[6] == "X" and board[11] == "X"and board[16] == "X" or #1st diag
            board[4] == "X" and board[7] == "X" and board[10] == "X"and board[13] == "X"):  #2nd diag
            os.system("clear")
            print_header()
            print_board()
            print("X Wins! Congratulations")
            x = x + 1
            print("Score X: ", x)
            break
        
        os.system("clear")
        print_header()
        print_board()
        
        #Check for tie (is board is full)
        isFull = True
        if " " in board:
            isFull = False
            
        #If the board is full. Do something
        if isFull == True:
            print("Tie!")
            break
            
        choice = inputValidation("Please choose an empty space for Y. ")
        #choice = int(choice)
        
        #Check for tie (is board is full)
        isFull = True
        for index in range(1, 16):
            if(board[index] == " "):
                isFull = False
                break
            
        #If the board is full. Do something
        if isFull == True:
            print("Tie!")
            break
        
        os.system("clear")
        print_header()
        print_board()
        
        #Get player Y input
        while board[choice] != " ":            
            print("Sorry, That space is not empty")
            time.sleep(1)
            choice = inputValidation("Please choose an empty space for Y. ") 
        board[choice] = "Y"  
        
        #Check for Y win 
        if (board[1] == "Y" and board[2] == "Y" and board[3] == "Y" and board[4] == "Y" or #1st row
            board[5] == "Y" and board[6] == "Y" and board[7] == "Y" and board[8] == "Y" or #2nd row
            board[9] == "Y" and board[10] == "Y" and board[11] == "Y" and board[12] == "Y" or #3rd row
            board[13] == "Y" and board[14] == "Y" and board[15] == "Y" and board[16] == "Y" or #4th row
            board[1] == "Y" and board[5] == "Y" and board[9] == "Y" and board[13] == "Y" or #1st col
            board[2] == "Y" and board[6] == "Y" and board[10] == "Y" and board[14] == "Y" or #2nd col
            board[3] == "Y" and board[7] == "Y" and board[11] == "Y" and board[15] == "Y" or #3rd col
            board[1] == "Y" and board[6] == "Y" and board[11] == "Y"and board[16] == "Y" or #1st diag
            board[4] == "Y" and board[7] == "Y" and board[10] == "Y"and board[13] == "Y"):  #2nd diag
            os.system("clear")
            print_header()
            print_board()
            print("Y Wins! Congratulations")
            y +=1
            break
        
        #Check for tie (is board is full)
        isFull = True
        if " " in board:
            isFull = False
            
        #If the board is full. Do something
        if isFull == True:
            print("Tie!")
            break
            
        os.system("clear")
        print_header()
        print_board()
        choice = inputValidation("Please choose an empty space for O. ")
        #choice = int(choice)  
        #Check for tie (is board is full)
        isFull = True
        for index in range(1, 16):
            if(board[index] == " "):
                isFull = False
                break
            
        #If the board is full. Do something
        if isFull == True:
            print("Tie!")
            break
        
        os.system("clear")
        print_header()
        print_board()
        #Get player O input
        while board[choice] != " ":            
            print("Sorry, That space is not empty")
            time.sleep(1)
            choice = inputValidation("Please choose an empty space for O. ") 
        board[choice] = "O"  
        
        #Check for O win 
        if (board[1] == "O" and board[2] == "O" and board[3] == "O" and board[4] == "O" or #1st row
            board[5] == "O" and board[6] == "O" and board[7] == "O" and board[8] == "O" or #2nd row
            board[9] == "O" and board[10] == "O" and board[11] == "O" and board[12] == "O" or #3rd row
            board[13] == "O" and board[14] == "O" and board[15] == "O" and board[16] == "O" or #4th row
            board[1] == "O" and board[5] == "O" and board[9] == "O" and board[13] == "O" or #1st col
            board[2] == "O" and board[6] == "O" and board[10] == "O" and board[14] == "O" or #2nd col
            board[3] == "O" and board[7] == "O" and board[11] == "O" and board[15] == "O" or #3rd col
            board[1] == "O" and board[6] == "O" and board[11] == "O"and board[16] == "O" or #1st diag
            board[4] == "O" and board[7] == "O" and board[10] == "O"and board[13] == "O"):  #2nd diag
            os.system("clear")
            print_header()
            print_board()
            print("O Wins! Congratulations")
            o = o + 1
            break
        
        #Check for tie (is board is full)
        isFull = True
        if " " in board:
            isFull = False
            
        #If the board is full. Do something
        if isFull == True:
            print("Tie!")
            break
        
#Main Program        
while ans == True:
    TicTacToe()
    ans = continueAgain()