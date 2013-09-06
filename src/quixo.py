# This program implements the game Quixo.
# It was written as a team project for CSSE 120, Fall 2010.
# Section 1, Team 13
# Team members:
#Kyle Bippus, Demetruis Vassar, Daniel Schepers

# TODO: 3. Implement your solutions here. 
# You can add as many modules as you need, just import them, as necessary. 
# Don't forget to use the template located at 
# http://www.rose-hulman.edu/class/csse/csse120/201110/Homework/formForFunctionsAndModules.html
# in solving this assignment.
#_____________________---------------------------------_____________________
#Import the neccessary items to run the game
from time import sleep
from zellegraphics import *
from createBlockObject import Block
import winsound
#_______________-----------------------------------__________________________
WIDTH = 1024
HEIGHT = 768  
win = GraphWin("Test Quixo Board", WIDTH, HEIGHT)
#Creates a global window
def window(win):
    '''creates the quixo game window'''
    while True:
        startscreen=Image(Point(WIDTH/2,HEIGHT/2),'TitleScreenGameBackground.ppm')
        startscreen.draw(win)
        point=win.getMouse()
        x=point.getX()
        y=point.getY()
        #for instructions
        if x<=640 and x>=387 and y>=430 and y<=460:
            instructionScreen=Image(Point(WIDTH/2,HEIGHT/2),'HowToPlayGameBackground.ppm')
            instructionScreen.draw(win)
            point1=win.getMouse()       
            X=point1.getX()
            Y=point1.getY()
            if X<=982 and X>=826 and Y<56 and Y>22:
                playGame=Image(Point(WIDTH/2,HEIGHT/2),'GameBackground.ppm')
                playGame.draw(win)
                win.setCoords(-1,-1,6,6)
                return win
        #for credits
        if x<=640 and x>=387 and y>=490 and y<=520:
            creditScreen=Image(Point(WIDTH/2,HEIGHT/2),'CreditsGameBackGround.ppm')
            creditScreen.draw(win)
            point1=win.getMouse()
            X=point1.getX()
            Y=point1.getY()
            if X<=995 and X>=735 and Y<56 and Y>22:
                playGame=Image(Point(WIDTH/2,HEIGHT/2),'GameBackground.ppm')
                playGame.draw(win)
                win.setCoords(-1,-1,6,6)
                return win            
        #for quit
        if x<=640 and x>=387 and y>=545 and y<=575:
            win.close()
        #for playGame
        if x<=640 and x>=387 and y>=373 and y<=406:
            playGame=Image(Point(WIDTH/2,HEIGHT/2),'GameBackground.ppm')
            playGame.draw(win)
            win.setCoords(-1,-1,6,6)
            return win

#________________________--------------------------------_________________________
    

def drawSquares(window):
    '''draws the squares to the window.  Puts them in a list.'''
    blockList=[]
    for k in range (0,5):
        for i in range (0,5):
            block=Block(i,k)
            block.draw(window)
            blockList.append(block)
    return blockList            

def getUserInput(win,squares):
    '''Gets the user input. Should rule out illegal clicks to non-perimeter squares'''

    O=2 #an arbitrary number to ensure the loop in the next line runs at least once.
    while O!=1:
        point=win.getMouse()
        X=point.getX()
        Y=point.getY()
        # The following decimals obtained by getting printing getMouse() results
        if X>4.04985337243 and X<5.80156402737 and Y<-0.425032594524 and Y>-0.735332464146:
            win.close()
        while X<0 or X>5 or Y<0 or Y>5 and not (X>4.04985337243 and X<5.80156402737 and Y<-0.425032594524 and Y>-0.735332464146) and not(X>-0.808406647116 and X<0.956989247312 and Y<-0.415906127771 and Y>-0.7444589309):
                text=Text(Point(2.5,5.5),"You did not select a block. Please select again")
                text.draw(win)
                sleep(1)
                point=win.getMouse()
                text.undraw()
                X=point.getX()
                Y=point.getY()
        Xmax=4
        Xmin=1
        yMax=4
        yMin=1
        if X>Xmin and X<Xmax and Y>yMin and Y<yMax:
            text=Text(Point(2.5,5.5),"Illegal move. Please try again")
            text.draw(win)
            sleep (1.5)
            text.undraw()                
        else:
            O=1
            for square in squares:
                selected=square.getMouse(point)
                if selected==1:
                    return square
    
    
def moveBlocks(selection,destination,squareList,turn): 
    '''Selection and destination will be passed into this function using the getInput function
    Eliminates any illegal moves not already ruled out by the getInput function.
    Using the turn parameter, draws the correct notation on the blocks
    moves the selection block to the destination
    '''
    sX=int(selection.getX())
    sY=int(selection.getY())
    dX=int(destination.getX())
    dY=int(destination.getY())
    while True:
        if turn==True:
            selection.drawX(win)
        else:
            selection.drawO(win)
        break
    while True:
        if (dX,dY)!=(sX,0) and (dX,dY)!=(sX,4) and (dX,dY)!=(0,sY) and (dX,dY)!=(4,sY):
            text=Text(Point(2.5,5.5),"You may not choose that block. Please choose your destination block again.")
            text.draw(win)
            sleep(1.5)
            text.undraw()
            newDestination=getUserInput(win,squareList)
            dX=int(newDestination.getX())
            dY=int(newDestination.getY()) 
        elif sX==dX and sY==dY:
            text=Text(Point(2.5,5.5),"Same Block selected. Please choose your destination block again.")
            text.draw(win)
            sleep(1.5)
            text.undraw()
            newDestination=getUserInput(win,squareList)
            dX=int(newDestination.getX())
            dY=int(newDestination.getY())
        elif dX!=sX and dY!=sY:
            text=Text(Point(2.5,5.5),"Invalid Selection. Please choose your destination again.")
            text.draw(win)
            sleep(1.5)
            text.undraw()
            newDestination=getUserInput(win,squareList)
            dX=int(newDestination.getX())
            dY=int(newDestination.getY())
        else:
            break
    if sY==dY: 
        if sX>dX: #Selection is right of destination, on the same line
            selection.move(.5,.5)
            for x in squareList:
                q=x.getX()
                u=x.getY()
                if sY==u and q<sX:
                    x.move(1,0)
            selection.move(dX-sX-.5,-.5)
        if sX<dX: #Selection is left  of destination, on the same line
            selection.move(-.5,.5)
            for x in squareList:
                q=x.getX()
                u=x.getY()
                if sY==u and q>sX:
                    x.move(-1,0)
            selection.move(dX-sX+.5,-.5)
    if sX==dX: 
        if sY>dY: #Selection is left of destination, in the same column
            selection.move(.5,.5)
            for x in squareList:
                q=x.getX()
                u=x.getY()
                if q==sX and u<sY:
                    x.move(0,1)
            selection.move(-.5,dY-sY-.5)
        if sY<dY: #Selection is left of destination, in the same column
            selection.move(.5,-.5)
            for x in squareList:
                q=x.getX()
                u=x.getY()
                if q==sX and u>sY:
                    x.move(0,-1)
            selection.move(-.5,dY-sY+.5)        
                
def consoleDisplay(squareList):
    '''draws a text version of the game to the console'''
    for y in range (4,-1,-1):
        string=""
        for x in range (0,5):
            for k in squareList:
                q=k.whosThere(x,y)
                string=string+str(q)
        print (string)
    print ()

def playerTurn(turn,text):
    '''alternates between playerX turn being true and false.'''
    text.undraw()
    while True:
        playerXturn= not turn
        break
    if playerXturn:
        text=Text(Point(2.5,-.5),"Player X's Turn")
    else:
        text=Text(Point(2.5,-.5),"Player O's Turn")  
    text.draw(win)
    return playerXturn,text

def endGame(squareList,turn,text2):
    '''Checks first rows, then columns, then one diagonal at a time to see if there are 5 
    player blocks in a row. Checks to see if both players win and if so the player who made
    the last move loses
    '''
    playerXwins=False
    playerOwins=False
    for y in range (0,5):
        winByRow=[]
        winByColumn=[]
        winByDiagonal=[]
        winByOther=[]
        for x in range (0,5):
            for k in squareList:
                q=k.whosThere(x,y)
                if q!="":
                    winByRow.append(q)
                p=k.whosThere(y,x)
                if p!="":
                    winByColumn.append(p)
                u=k.whosThere(x,x)
                if u!="":
                    winByDiagonal.append(u)
                z=k.whosThere(x,4-x)
                if z!="":
                    winByOther.append(z)
        players=["X","O"]
        for k in players:
            if (winByRow[0]==winByRow[1] and winByRow[1]==winByRow[2] and winByRow[2]==winByRow[3] and winByRow[3]==winByRow[4] and winByRow [3]==k) or (winByColumn[0]==winByColumn[1] and winByColumn[1]==winByColumn[2] and winByColumn[2]==winByColumn[3] and winByColumn[3]==winByColumn[4] and winByColumn[3]==k) or (winByOther[0]==winByOther[1] and winByOther[1]==winByOther[2] and winByOther[2]==winByOther[3] and winByOther[3]==winByOther[4] and winByOther[3]==k) or(winByDiagonal[0]==winByDiagonal[1] and winByDiagonal[1]==winByDiagonal[2] and winByDiagonal[2]==winByDiagonal[3] and winByDiagonal[3]==winByDiagonal[4] and winByDiagonal[3]==k):
                if k=="X":
                    playerXwins=True
                else:
                    playerOwins=True
        if playerXwins and playerOwins and not turn:
            text2.undraw()
            winsound.PlaySound('Victory.wav', winsound.SND_FILENAME)
            text=Text(Point(2.5,5.5),"Player X wins!!")
            text.draw(win)
            print ("Player X wins!")
            return "winner"
        elif playerXwins:
            text2.undraw()
            winsound.PlaySound('Victory.wav', winsound.SND_FILENAME)
            text=Text(Point(2.5,5.5),"Player X Wins!")        
            text.draw(win)
            print("player X wins!")
            return "winner"    
        elif playerOwins:
            text2.undraw()
            winsound.PlaySound('Victory.wav', winsound.SND_FILENAME)
            text=Text(Point(2.5,5.5),"Player O wins!!")
            text.draw(win)
            print("Player O wins!!")
            return "winner"
#________________----------------________________________________-----------------------____________________________ 
def play():
    window(win)
    squares=drawSquares(win)
    turn=True
    turnLabel=Text(Point(2.5,-.5),"Player X's Turn.")
    turnLabel.draw(win)
    end=endGame(squares,turn,turnLabel)
    while end!="winner":
        selection=getUserInput(win,squares)
        X=int(selection.getX())
        Y=int(selection.getY())
        while (selection.whosThere(X,Y)=="X" and turn==False) or (selection.whosThere(X,Y)=="O" and turn==True):
            text=Text(Point(2.5,5.5),"You may not select the other player's block. Please select again")
            text.draw(win)
            sleep(1)
            selection=getUserInput(win,squares)
            text.undraw()
            X=selection.getX()
            Y=selection.getY()
        destination=getUserInput(win,squares)     
        moveBlocks(selection,destination,squares,turn)
        turn,turnLabel=playerTurn(turn,turnLabel)
        consoleDisplay(squares)
        end=endGame(squares,turn,turnLabel) 
    win.getMouse()
    win.close()
#_____________________________----------------------------------------------
def main():
    play()

    
#----------------------------------------------------------------------
# If this module is running at the top level
# (as opposed to being imported by another module),
# then run the body of this expression, which simply calls main.
#----------------------------------------------------------------------
if __name__ == '__main__':
    main()    