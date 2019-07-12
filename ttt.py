#!/usr/bin/python
'''
1. display instruction of game
2. who is first player
3. create layout of game
4. display layout of game
5. while nobody is won and it is not tie
        if it is your turn
                get your move
                update layout
        else
                calculate best layout
                update layout
        
        display layout
        switch turn
        congratulation
def displayInstr() #instruction of the game
def askYN() #collect the information from user
def getNumber(ques,low,high)
def confirmPieces()
def newBoard()
def displayBoard(board)
def validMoves(board)
def nextTurn(turn)
def humanMove(board,human)
def computerMoves(board,computer,human)
def winner(board)
def congratesWinner(thewinner,computer,human)
def main()


*********python Hints***********
Lists are enclosed in brackets ( [ ] ), and
their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and
cannot be updated.
'''
X="X"
O="O"
EMPTY=" "
TIE="TIE"
NUMOFSEQ=9

def displayInstr():
        '''contain the instruction'''
        print( ''' WELCOME TO THE WORLD OF TIC TAC TOE THE GAME BETWEEN INTELLIGENT COMPUTER AND SMART HUMAN.THIS IS GREATEST INTELLECTUAL CHALLENGE 
                0  | 1 | 2
                ----------
                3  | 4 | 5
                ----------
                6  | 7 | 8
        YOU CAN SELECT CELL BY PROVIDING A NUMBER FROM 0-8 ''')

def askYN(qus):
        '''ask question to user do you want to play or not'''   
        response=None
        while response not in ("y","n"):
                response = input((qus).lower())
        return response


def getNumber(qus,low,high):
        '''
        we should demand a number between low and high repeatedly
        unless use enters a valid number 
        '''
        response=None
        while response not in range(low,high):
                response = int(input(qus))
                print(response)
        return response

def confirmPieces():
        '''determine human or computer goes first if user is going to play first then we will allot X to human and O to computer otherwise vice versa '''
        getfirst=askYN("DO YOU WANT TO  PLAY FIRST (Y|N) ? ")
        if getfirst=="y":
                human=X
                computer=O
        else:
                human=O
                computer=X

        return computer,human

def newBoard():
        '''deciding data structure for a game'''
        board=[]
        for cell in range(NUMOFSEQ):
                board.append(cell)
        return board    

def displayBoard(board):
        '''display the newly created board'''
        print ("\n\t",board[0],"|",board[1],"|",board[2])
        print ("\t","----------")
        print ("\t",board[3],"|",board[4],"|",board[5])
        print ("\t","----------")
        print ("\t",board[6],"|",board[7],"|",board[8])

def validMoves(board):
        '''
        deciding valid moves
                        type() return variable type for findind valid move we are comparing the type of each cells
                        if type of cell is integer then its empty hence valid else it is filled with x 
        '''
        validlist=[]
        for i in range(NUMOFSEQ):
                if type(board[i]) == type(1):
                        validlist.append(i)
        return validlist

def humanMove(board,human):
        '''method for human move'''
        legalmoves=validMoves(board)
        move=None
        while move not in legalmoves:
                move=getNumber("Enter The No. Between 0-8 : ",0,NUMOFSEQ)       
                if move not in legalmoves: 
                        print ("Invalid Move! try again.")
        return move

def nextTurn(turn):
        if turn==X:
                return O
        else:
                return X

def winner(board):
        '''
        -=-=--=-=-=-= wining condition -=-=-=-=-=-=-
        winways decide winning moves that are 3 vertical possibilities
        3 horizontal possibilities and remaining 2 diagonals.
        now each tuple i.e.((2,5,8) is expanded in t hence for (2,5,8) t[0]=2
                t[1]=5 t[2]=8)
        furthur we check that all cells contains same symbole (either 'x' or 'o') 
        also we cross check that it is not of integer type, if condition is satisfied
        the winer is returned by his symbol('o' or 'x') which is contain in board[t[i]]

        -- tie condition --
        first we check winner if there is no winner and all cells are filled with symbol (0,x) then there is TIE
        here we are checkinf that all cells type are same and its not int hence all cells are filled with symbol bt no
        winner

        use of tuples cant be changed
        '''
        winways=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for t in winways:
                if(board[t[0]]==board[t[1]]==board[t[2]] != type(1)):
                        win=board[t[0]]
                        return win
        if (type(board[0])==type(board[1])==type(board[2])==type(board[3])==type(board[4])==type(board[5])==type(board[6])==type(board[7])==type(board[8]) != type(1)):
                return TIE
        else:
                return None
        
def computerMove(board,computer,human):
        board=board[ : ]
        for move in validMoves(board):
                board[move]=computer
                if winner(board) == computer:
                        return int(move)
                        #print move
        #board[move]=computer
        for move in validMoves(board):
                board[move]=human
                if winner(board)==human:
                        return int(move)
        #board[move]=computer
        bestmoves=(4,0,2,6,8,1,3,5,7)
        for move in bestmoves:
                if move in validMoves(board):
                        return int(move)
        
def congratesWinner(thewinner,computer,human):
        if thewinner==human:
                print ("Congratulation %s is winner"%human)
        elif thewinner==computer:
                print ("Sorry  %s is winner"%computer)
        else:
                print ("Its a tie !")

        

def main():
        
        #print askYN("DO YOU WANT TO CONTINUE PRESS YES OR NO : ")
        #print getNumber("ENTER A NUMBER BETWEEN 0-8 : ",0,NUMOFSEQ)
        #print "COMPUTER IS DECIDED TO PLAY WITH %s AND HUMAN WITH %s "%(computer,human)
        turn=X
        displayInstr()
        computer,human=confirmPieces()
        board=newBoard()
        displayBoard(board)
        print("Valid moves: ")
        print (validMoves(board))
        while winner(board)==None:
                if turn==human:
                        hm=humanMove(board,human)
                        '''
                        these is the important line which will update the board 
                        human move returns move selected by human
                        '''
                        board[hm]=human
                        ###############
                else:
                        cm=computerMove(board,computer,human)
                        board[cm]=computer
        
                displayBoard(board)
                print (validMoves(board))
                turn=nextTurn(turn)
        congratesWinner(winner(board),computer,human)
        
main()
