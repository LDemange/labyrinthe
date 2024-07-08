# -*- coding: Utf-8 -*
################################################################################
#                                                                              #
#                                  PACO                                        #
#                                                                              #
#                           Jeu de type Pac Man                                #
#                         avec éditeur de niveaux                              #
#                     non limité en largeur et hauteur                         #
#                                                                              #
#                       langage : Python 2.7                                   # 
#                       API     : Pygame 1.9                                   #
#                       date    : 14/03/2016                                   #
#                       version : 1.4                                          #
#                       auteur  : guillaume michon                             #
#                                                                              # 
################################################################################
#import pygame as pg
#from pygame.locals import *
from tkinter import *

class Case:
    def __init__(self,x1, y1, x2, y2, couleurCase, couleurPion, pion):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.couleurCase = couleurCase
        self.couleurPion = couleurPion
        self.pion = pion
    
    def __eq__(self, other):
        return (self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2)
    
    def getCoordCase(self):
        return [self.x1, self.y1, self.x2, self.y2]
    
    def getCoordPion(self):
        return [self.x1+10, self.y1+10, self.x2-10, self.y2-10]
    
    def set(self, val):
        set.pion = val
        
    def setCouleurPion(self, val):
        self.couleurPion = val
        
    def creerCase(self):
        can.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.couleurCase)
        
    def placerPion(self):
        if self.pion:
            can.create_oval(self.x1+10, self.y1+10, self.x2-10, self.y2-10, fill = self.couleurPion)
    """
    Purpose: 
    """
    
def laby():
    global x1, y1, x2, y2
    ite, i, couleurCase = 0,1,'#f07ab7'
    
    while x1<200 and y1<200 :
        if i <=12 :
            couleurPion = '#9feb87'
            tout_les_cases.append(Case(x1,y1,x2,y2,couleurCase,couleurPion,1))
        
        elif i > 13 :
            couleurPion = '#ffde01'
            tout_les_cases.append(Case(x1,y1,x2,y2,couleurCase,couleurPion,1))
        
        else :
            tout_les_cases.append(Case(x1,y1,x2,y2,couleurCase,'',0)) 
        
        tout_les_cases[-1].creerCase()
        
        i,ite,x1,x2 = i+1, ite+1, x1+40, x2+40
        
        if ite == 5:
            y1, y2 = y1 + 40, y2 + 40
            ite, x1, x2 = 0, 5, 45
            
        if i%2 == 0:
            couleurCase = 'white'
            
        else:
            couleurCase = '#f07ab7'
        
    for case in tout_les_cases:
        case.placerPion()
        
    bouttonLaby.destroy()
    score.pack()
    
#initialisation des variables
x1, y1, x2, y2  = 5, 5, 45, 45
tout_les_cases = []

fen = Tk()
fen.title('labyrinthe')
fen.geometry('260x245+450+250')
fen.configure(bg = 'white')
can = Canvas(fen, width = 206, heigh = 206, bg = 'pink')
    
font = 'arial 13 bold'
    
bouttonLaby = Button(fen, text = 'Commencer', font = font, command=laby, fg ='white', bg ='#f00ab7')
score = Label(fen, text = 'V : 0 vs J : 0', font = font, fg ='white', bg ='#f00ab7')
    
can.pack()
bouttonLaby.pack()
    
''' can.bind('ButtonPress-1', click)
can.bind('B1-motion', bouger)
can.bind('ButtonRelease-1', arret)
can.configure(cursor = 'hand2')'''
    
fen.resizable(False,False)
fen.mainloop()