def main():
    import random
    print("Tic Tac Toe\nYou are X and the computer is O.\nEnter Q to QUIT.")
    
    print()
    #Create Gameboard
    print("GAMEBOARD:")
    tictactoe = [[],[],[]]
    for i in range(3):
        tictactoe[i] = [" "," "," "]
        print(tictactoe[i])
    print()

    count = 0
    #Ask for row number
    row = input("Enter row of your move:")
    
    while row.upper()!= "Q":
        #Calling def validate() to validate input
        while validate(row) == False:
            row = input("Enter row of your move:")
        column = input("Enter column of your move:")
        while validate(column) == False:
            column = input("Enter column of your move:")
            
        #if input is validated, continue with game  
        if validate(row) == True and validate(column) == True:
            
            #if user move is not empty, send error message
            if tictactoe[int(row)-1][int(column)-1] != " ":
                print("ERROR: That spot is taken. Re-enter move.")
                
            #if user move is empty, add user move to board
            elif tictactoe[int(row)-1][int(column)-1] == " ":
                tictactoe[int(row)-1][int(column)-1] = "X"
                count += 1

                #print boardgame
                print("Your Move:")
                for i in range(3):
                    print(tictactoe[i])
                print()
                if isWinner(tictactoe) == True:
                    break

                #getting random row and column for computer move        
                i = random.randint(0,2)
                j = random.randint(0,2)
                #while random computer move not an empty space, get new move
                while tictactoe[i][j] != " ":
                    i = random.randint(0,2)
                    j = random.randint(0,2)
                #if empty, add computer move       
                if tictactoe[i][j] == " ":
                    tictactoe[i][j] = "O"
                    count += 1
                    print("Computer Move:")
                #print boardgame    
                for i in range(3):
                    print(tictactoe[i])
                #check to see if there is winner
                # This line here can be simplified into if isWinner(tictactoe):
                if isWinner(tictactoe) == True or count == 9:
                    break
        #loop to ask for new move            
        row = input("Enter row of your move:")



def validate(userInp):
    #if row or column not a number, send error message
    if userInp.isdigit() == False:
        print("ERROR: Must enter numbers only.")
        return False
    #if row or column not 1-3, send error message
    elif int(userInp) < 1 or int(userInp) > 3:
        print("ERROR: There are only 3 rows and 3 columns. Reenter.")
        return False            
    else:
        return True
    
    
def isWinner(tictactoe):
    for i in range(3):
        #vertical wins
        if tictactoe[0][i] == tictactoe[1][i] == tictactoe[2][i]:
            #X wins
            if tictactoe[0][i] == "X":
                print("Yay! You Win!")
                return True
            #O wins
            elif tictactoe[0][i] == "O":
                print("Aww...You Lose:(")
                return True
        #horizontal wins
        elif tictactoe[i][0] == tictactoe[i][1] == tictactoe[i][2]:
            if tictactoe[i][0] == "X":
                print("Yay! You Win!")
                return True
            elif tictactoe[i][0] == "O":
                print("Aww...You Lose:(")
                return True
    #diagonal wins
    if tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2]:
        if tictactoe[0][0] == "X":
            print("Yay! You Win!")
            return True
        elif tictactoe[0][0] == "O":
            print("Aww...You Lose:(")
            return True
    elif tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0]:
        if tictactoe[0][2] == "X":
            print("Yay! You Win!")
            return True
        elif tictactoe[0][2] == "O":
            print("Aww...You Lose:(")
            return True
    
main()


