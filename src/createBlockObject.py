'''
Created on Oct 12, 2010

@authors: Dan Schepers, Kyle Bippus and Demetruis Vassar
'''
from zellegraphics import *
from math import *
from time import sleep

class Block:
    
    '''a block will be an object that will have a center point, a display (x,o, ) and will be mobile'''

    def __init__(self, initX, initY ,sizeX=1,sizeY=1, color='white',color1='black', isX=False,isO=False,isBlank=True, selected = True):
        
        ''' Point(initX,initY) will be the lower left hand corner of each block.
        initX,initY=the point of the lower left hand corner of the block
        sizeX,sizeY=1 because the lower left hand corner will be connected to a point up one coordinate, 
            right one coordinate. Can be set to a value because we want all blocks to be the same size
        size= one side of the square
        color- blocks themselves will be white
        color1-X's or O's will be black
        isX-will change to True if player X chooses the block
        '''

        self.initX=initX
        self.initY=initY
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.isX=False
        self.isO=False
        self.isBlank=True
        self.color1=color1
        self.color=color
        self.selected = selected
        if isX==True:
            self.X=Image(Point(initX+.5,initY+.5),'PlayerXTileFinal.ppm')
        if isO==True:
            self.O=Image(Point(initX+.5,initY+.5),'PlayerOTileFinal.ppm')
        if isBlank==True:
            self.blank=Image(Point(initX+.5,initY+.5),'NeutralTileFinal.ppm')            
                  
        #______----------____________------------------_______
        
        
    def draw(self,win):
            '''draws the block object in the given window.'''
            self.blank=Image(Point(self.initX+.5,self.initY+.5),'NeutralTileFinal.ppm')  
            self.blank.draw(win)
            
    def drawX(self,win):
            '''Turns the blank block into an x block'''
            if not self.isX and not self.isO:
                self.isX=True
                self.isBlank=False
                self.X=Image(Point(self.initX+.5,self.initY+.5),'PlayerXTileFinal.ppm')
                self.X.draw(win)
    def drawO(self,win):
        '''Turns the blank block into an o block'''
        if not self.isX and not self.isO:
            self.isO=True
            self.isBlank=False
            self.O=Image(Point(self.initX+.5,self.initY+.5),'PlayerOTileFinal.ppm')
            self.O.draw(win)
    def getMouse(self,point):
        '''Checks to see whether the click in the window falls within the perimeter of the block'''
        '''Returns 1 if it does,nothing if it doesn't'''
        X=point.getX()
        Y=point.getY()
        if self.initX<X<self.initX+self.sizeX and self.initY<Y<self.initY+self.sizeY:
            return 1
                
    def move(self,dx,dy):
        '''Moves block from current location dx, dy amount. Mutates initX and initY to reflect this move'''
        for i in range (10):            
            if self.isBlank:
                self.blank.move(dx/10,dy/10)
            elif self.isO:
                self.O.move(dx/10,dy/10)
            elif self.isX:
                self.X.move(dx/10,dy/10)
            sleep(.01)
        self.initX+=dx
        self.initY+=dy
   
    def getX(self):
        '''Gets the x value of the lower left hand corner of the block'''
        return self.initX
    
    def getY(self):
        '''gets the y value of the lower left hand corner of the block'''
        return self.initY
     
    def whosThere(self,x,y):
        '''given the parameters x and y, checks to see if x,y refers to the lower left hand corner of the block'''
        '''if they do, returns X if the block has an X on it, an O if it has an O on it, and a - if block is blank'''
        '''returns nothing if x,y doesn't refer to the left hand corner'''
        if x==self.initX and y==self.initY:
            if self.isX:
                return "X"
            if self.isO:
                return "O"
            else:
                return "-"
        else:
            return ""