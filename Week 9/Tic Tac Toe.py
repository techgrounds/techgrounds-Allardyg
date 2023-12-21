space1 = "1"
space2 = "2"
space3 = "3"
space4 = "4"
space5 = "5"
space6 = "6"
space7 = "7"
space8 = "8"
space9 = "9"
#
#Initializing all possible spaces

space1taken = False
space2taken = False
space3taken = False
space4taken = False
space5taken = False
space6taken = False
space7taken = False
space8taken = False
space9taken = False
#
#Initializing whether or not the spaces are taken

win = False
draw = False

winner = "NoWinneryet"
CurrentPlayer = "Player2"
ValidInput = False
#
#Initializing other variables like win or draw, who's turn it is, and whether or not the input is valid.

while win == False and draw == False:

    ValidInput = False

    if CurrentPlayer == "Player2":
      CurrentPlayer = "Player1"

    else:
        CurrentPlayer = "Player2"

    print (space1+"|"+space2+"|"+space3)
    print (space4+"|"+space5+"|"+space6)
    print (space7+"|"+space8+"|"+space9)

    print("\nIt's "+CurrentPlayer+"'s turn.")
    print ("\nWhere would you like to place your piece?")
#
# Switches who's turn it is, and draws the board

    while ValidInput == False:
        PlayerInput = input()
        #
        # Start of the loop that keeps repeating until the current player made a valid move, in the case of a wrong input the program will keep asking for new input.

        if CurrentPlayer == "Player1":
            
            if PlayerInput == "1" or PlayerInput == "2" or PlayerInput == "3" or PlayerInput == "4" or PlayerInput == "5" or PlayerInput == "6" or PlayerInput == "7" or PlayerInput == "8" or PlayerInput == "9":
                if PlayerInput == "1" and space1taken == False:
                    space1 = "X"
                    space1taken = True
                    ValidInput = True
                elif PlayerInput == "2" and space2taken == False:
                    space2 = "X"
                    space2taken = True
                    ValidInput = True
                elif PlayerInput == "3" and space3taken == False:
                    space3 = "X"  
                    space3taken = True          
                    ValidInput = True 
                elif PlayerInput == "4" and space4taken == False:
                    space4 = "X"
                    space4taken = True
                    ValidInput = True
                elif PlayerInput == "5" and space5taken == False:
                    space5 = "X"
                    space5taken = True
                    ValidInput = True
                elif PlayerInput == "6" and space6taken == False:
                    space6 = "X"
                    space6taken = True
                    ValidInput = True
                elif PlayerInput == "7" and space7taken == False:
                    space7 = "X"
                    space7taken = True
                    ValidInput = True
                elif PlayerInput == "8" and space8taken == False:
                    space8 = "X"
                    space8taken = True
                    ValidInput = True
                elif PlayerInput == "9" and space9taken == False:
                    space9 = "X"
                    space9taken = True
                    ValidInput = True
                #
                # Checks to see if the input is valid for player 1, if it is, it updates the board.

                else:
                    if ValidInput == False:
                        print ("Sorry, "+CurrentPlayer+". But this spot has already been taken, please try a different one")
                #
                # Checks if player 1 entered 1-9, but on a taken spot
 
            else:
                print ("Invalid input, please enter a number between 1 and 9")
                print ("\nWhere would you like to place your piece?")
            #
            # If player 1 didn't enter a correct symbol, it prints this error message.

            if ValidInput == True:
                print(CurrentPlayer+" placed their piece on spot #"+PlayerInput+"\n")
            #
            # Prints text to show that a move has been made succesfully

        if CurrentPlayer == "Player2":
            if PlayerInput == "1" or PlayerInput == "2" or PlayerInput == "3" or PlayerInput == "4" or PlayerInput == "5" or PlayerInput == "6" or PlayerInput == "7" or PlayerInput == "8" or PlayerInput == "9":
                if PlayerInput == "1" and space1taken == False:
                    space1 = "O"
                    space1taken = True
                    ValidInput = True
                elif PlayerInput == "2" and space2taken == False:
                    space2 = "O"
                    space2taken = True
                    ValidInput = True
                elif PlayerInput == "3" and space3taken == False:
                    space3 = "O"
                    space3taken = True          
                    ValidInput = True 
                elif PlayerInput == "4" and space4taken == False:
                    space4 = "O"
                    space4taken = True
                    ValidInput = True
                elif PlayerInput == "5" and space5taken == False:
                    space5 = "O"
                    space5taken = True
                    ValidInput = True
                elif PlayerInput == "6" and space6taken == False:
                    space6 = "O"
                    space6taken = True
                    ValidInput = True
                elif PlayerInput == "7" and space7taken == False:
                    space7 = "O"
                    space7taken = True
                    ValidInput = True
                elif PlayerInput == "8" and space8taken == False:
                    space8 = "O"
                    space8taken = True
                    ValidInput = True
                elif PlayerInput == "9" and space9taken == False:
                    space9 = "O"
                    space9taken = True
                    ValidInput = True
                #
                # Checks to see if the input is valid for player 2, if it is, it updates the board.                   
                else:
                    if ValidInput == False:
                        print ("Sorry, "+CurrentPlayer+". But this spot has already been taken, please try a different one")
                #
                # Checks if player 2 entered 1-9, but on a taken spot                        
            else:
                print ("Invalid input, please enter a number between 1 and 9")
                print ("\nWhere would you like to place your piece?")
            #
            # If player 1 didn't enter a correct symbol, it prints this error message.

            if ValidInput == True:
                print(CurrentPlayer+" placed their piece on spot #"+PlayerInput+"\n")
            #
            # Prints text to show that a move has been made succesfully

    if space1 == "X" and space2 == "X" and space3 == "X":
        winner = "Player1"
        win = True
    if space4 == "X" and space5 == "X" and space6 == "X":
        winner = "Player1"
        win = True
    if space7 == "X" and space8 == "X" and space9 == "X":
        winner = "Player1"
        win = True
    if space1 == "X" and space4 == "X" and space7 == "X":
        winner = "Player1"
        win = True
    if space2 == "X" and space5 == "X" and space8 == "X":
        winner = "Player1"
        win = True
    if space3 == "X" and space6 == "X" and space9 == "X":
        winner = "Player1"
        win = True
    if space1 == "X" and space5 == "X" and space9 == "X":
        winner = "Player1"
        win = True
    if space3 == "X" and space5 == "X" and space7 == "X":
        winner = "Player1"
        win = True

# Checks the 8 possible win conditions to see if player2 has won yet    

    if space1 == "O" and space2 == "O" and space3 == "O":
        winner = "Player2"
        win = True
    if space4 == "O" and space5 == "O" and space6 == "O":
        winner = "Player2"
        win = True
    if space7 == "O" and space8 == "O" and space9 == "O":
        winner = "Player2"
        win = True
    if space1 == "O" and space4 == "O" and space7 == "O":
        winner = "Player2"
        win = True
    if space2 == "O" and space5 == "O" and space8 == "O":
        winner = "Player2"
        win = True
    if space3 == "O" and space6 == "O" and space9 == "O":
        winner = "Player2"
        win = True
    if space1 == "O" and space5 == "O" and space9 == "O":
        winner = "Player2"
        win = True
    if space3 == "O" and space5 == "O" and space7 == "O":
        winner = "Player2"
        win = True
#
# Checks the 8 possible win conditions to see if player2 has won yet        
    
    if win == True:
        print ("there is a winner!! The game ends now."+" Congratulations to: "+winner)
        print (space1+"|"+space2+"|"+space3)
        print (space4+"|"+space5+"|"+space6)
        print (space7+"|"+space8+"|"+space9)
#
# Declares the winner        

    if win == False and space1taken == True and space2taken == True and space3taken == True and space4taken == True and space5taken == True and space6taken == True and space7taken == True and space8taken == True and space9taken == True:
        draw = True
#
# Checks if there's no winner, and if all possible spaces are occupied yet. If so, it declares a draw so that the players won't be asked for input anymore.

    if draw == True:
        print (space1+"|"+space2+"|"+space3)
        print (space4+"|"+space5+"|"+space6)
        print (space7+"|"+space8+"|"+space9)        
        print ("It's a draw, please restart the program to try again.")
#
# Shows the end result of a draw.

print ("\nGame ended")        
#
#Message to show the game is over.
