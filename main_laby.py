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
from random import randrange
from tkinter import *
from math import ceil, cos, sin, pi
from motifs import *

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
        
    def creerRectangle(self,nature):
        if nature == 'case':
            can.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.couleurCase, width=2)
        elif nature == 'section':
            can.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.couleurCase, width=3, outline = 'red')
        else:
            return 0
            
        
    def placerPion(self):
        if self.pion:
            can.create_oval(self.x1+10, self.y1+10, self.x2-10, self.y2-10, fill = self.couleurPion)
            
    def peutBougerVers(self, dest):
        caseDest = trouverCase(dest)
        if not caseDest:
            return 0
        else:
            return 0 # A terminer
    
def laby():
    ite, i, couleurCase = 0,1,'#f07ab7'
    m_wall = []
    
    nb_section = int(length_laby*heigh_laby/9)
    
    for i in range(0,nb_section):
        motif = motifs[randrange(0,nb_motifs,1)]
        m_wall.append(motif)
    
    for i in range(0,nb_section):
        xs_g = offset_x+3*length_case*(i%int(length_laby/3))
        ys_g = offset_y+3*length_case*(int(i/int(length_laby/3)))
        
        for j in range(0,9):
            x1 = xs_g + (j%3)*length_case
            x2 = x1 + length_case
            y1 = ys_g + int(j/3)*length_case
            y2 = y1 + length_case
            
            if(m_wall[i][j%3][int(j/3)]):
                couleurCase = 'black'
                tout_les_cases.append(Case(x1,y1,x2,y2,couleurCase,'',0))
            else:
                couleurCase = 'white'
                tout_les_cases.append(Case(x1,y1,x2,y2,couleurCase,'',0))
                
            tout_les_cases[-1].creerRectangle('case')
    

    
    Case(0,offset_y,offset_x+length_laby*length_case,offset_y-length_case,'black','',0).creerRectangle('case')
    Case(0,offset_y+heigh_laby*length_case,offset_x+length_laby*length_case,offset_y+(heigh_laby+1)*length_case,'black','',0).creerRectangle('case')
    Case(0,offset_y,length_case,offset_y+(heigh_laby)*length_case,'black','',0).creerRectangle('case')
    
    for i in range(0, heigh_laby):
        for j in range(0,2):
            Case(length_case*(j+1),offset_y+length_case*i,length_case*(j+2),offset_y+length_case*(i+1),'white','',0).creerRectangle('case')
        
    for i in range(0, heigh_laby+2):
        for j in range(0,3):
            Case(offset_x + length_case*(length_laby+j),length_case*i,offset_x + length_case*(length_laby+j+1),length_case*(i+1),'white','',0).creerRectangle('case')    
    
    x1, y1, x2, y2 = offset_x, offset_y, offset_x+length_section*length_case, offset_y+length_section*length_case
    i=1
    
    
    while x1 < length_laby*length_case + offset_x and  y1 < heigh_laby*length_case +offset_y :
    
        tout_les_section.append(Case(x1,y1,x2,y2,'','',0)) 
        
        tout_les_section[-1].creerRectangle('section')

        i,ite,x1,x2 = i+1, ite+1, x1+length_section*length_case, x2+length_section*length_case
        
        if ite == int(length_laby/3):
            y1, y2 = y1 + length_section*length_case, y2 + length_section*length_case
            ite, x1, x2 = 0, offset_x, offset_x+length_section*length_case
            
       
    for case in tout_les_cases:
        case.placerPion()
        
    bouttonLaby.destroy()
    score.pack()
    
#initialisation des variables
length_laby = 30 # Case number, choisir un multiple de 3 svp
heigh_laby = 18
length_case = 45 # pixel number, multiple de 3 svp
length_section = 3 #nb_case
offset_y = length_case
offset_x = 3*length_case
eps = 3
tout_les_cases = []
tout_les_section = []
session = ''

def trouverCase(coord):
    for case in tout_les_cases:
        if case.x1 == coord[0] and case.y1 == coord[1] and case.x2 == coord[2] and case.y2 == coord[3]:
            return case
    return 0

def findCoordSection(coord):
    num_x = ceil((coord[2]+coord[0])/(3*2*length_case)-1)
    num_y = ceil((coord[3]+coord[1])/(3*2*length_case)-1/3)
 
    xg_s = offset_x + 3*length_case*(num_x-1)
    yg_s = offset_y + 3*length_case*(num_y-1)
    
    xd_s = xg_s + length_case*3
    yd_s = yg_s + length_case*3
    
    return xg_s, yg_s, xd_s, yd_s

def rotate(xc, yc, theta, x_in, y_in): # rotation de centre (xc,yc) d'angle theta (rad) du vecteur (x,y)
    theta = -theta
    x_in = x_in - xc
    y_in = y_in - yc
    x_out = x_in * cos(theta) - y_in * sin(theta)
    y_out = x_in*sin(theta) + y_in*cos(theta)
    x_out = x_out + xc
    y_out = y_out + yc
    return x_out, y_out
    
    
def click_g(event):
    global caseDepart, pionClicker, session
    x, y = event.x, event.y 
    pionClicker = 0
    caseDepart = 0
    clicker = can.find_overlapping(x,y,x,y)
    if len(clicker) > 0 :
        coord = can.coords(clicker[0])
        caseDepart = trouverCase(coord)
        if caseDepart.couleurPion == session:
            pionClicker = 0
        else:
            pionClicker = clicker[1]


      
def click_d(event):
    global caseDepart, pionClicker, session
    x, y = event.x, event.y 
    pionClicker = 0
    caseDepart = 0
    clicker = can.find_overlapping(x,y,x,y)
    if len(clicker) > 0 :
        coord = can.coords(clicker[0])
        xg_s, yg_s, xd_s, yd_s = findCoordSection(coord)
        section_matrix = can.find_overlapping(xg_s+eps, yg_s+eps, xd_s-eps, yd_s-eps)
        xc = (xg_s + xd_s)/2
        yc = (yg_s + yd_s)/2
        if(y > offset_y and y < offset_y + heigh_laby * length_case and x > offset_x and x< offset_x + length_laby*length_case ):
            for i in range(len(section_matrix)):
                coord = can.coords(section_matrix[i])
                xg, yg = rotate(xc, yc, pi/2, coord[0], coord[1])
                xd, yd = rotate(xc, yc, pi/2, coord[2], coord[3])
                deplacement = [[xg, yg,xd,yd]] #A terminer, comprendre
                can.coords(section_matrix[i], deplacement[0])
                caseDepart = trouverCase(coord)
       
       
        #if caseDepart.couleurPion == session:
        #    pionClicker = 0
        #else:
        #    pionClicker = clicker[1]
        
def bouger(event):
    global caseDepart, pionClicker
    x, y = event.x, event.y
    if caseDepart and pionClicker:
        coord = can.coords(pionClicker)
        deplacement = [[x-10, y-10,x+10,y+10]]
        can.coords(pionClicker, deplacement[0])

def arret(event):
    global caseDepart, pionClicker, scoreV, scoreJ, session
    x,y = event.x, event.y
    
    '''collision = find_overlapping(x-10,y-10,x+10,y+10)
    coord = can.coords(collision[0])
    
    if not caseDepart.peutBougerVers(coord):
        can.coords(pionClicker, caseDepart,getCoordCase()) A terminer''' 

fen = Tk()
fen.title('labyrinthe')
length_window = (length_laby+6)*length_case + 40
heigh_window = (heigh_laby+2)*length_case + 40
fen.geometry(f'{length_window}x{heigh_window}+200+250')
fen.configure(bg = 'white')
can = Canvas(fen, width = (length_laby+6)*length_case+10, heigh = (heigh_laby+2)*length_case+10, bg = 'white') #pink
    
font = 'arial 13 bold'
    
bouttonLaby = Button(fen, text = 'Commencer', font = font, command=laby, fg ='white', bg ='#f00ab7')
score = Label(fen, text = 'V : 0 vs J : 0', font = font, fg ='white', bg ='#f00ab7')
    
can.pack()
bouttonLaby.pack()
    
can.bind('<ButtonPress-1>', click_g) # bouton gauche de la souris => click_g
can.bind('<ButtonPress-3>', click_d) # bouton droit de la souris => click_d
can.bind('<B1-Motion>', bouger)
can.bind('<ButtonRelease-1>', arret)
can.configure(cursor = 'hand2')
    
fen.resizable(False,False)
fen.mainloop()