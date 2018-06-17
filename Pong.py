# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 09:34:19 2018

@author: Vašek
"""

import pyglet as pg
from pyglet import gl

#Velikost okna

sirka = 900
vyska = 600

velmic = 20
sirpalka = 10
delpalka = 100
rychlost = 200
rychpalka = rychlost * 1.5

delkapulcary = 20
velfont = 40
odsazenitextu = 30

 #potřebné proměnné

pozice_palek = [vyska // 2, vyska // 2]  # vertikalni pozice palek
pozice_mice = [0, 0]  # souradnice micku 
rychlost_mice = [0, 0]   
stisknute_klavesy = set()  # sada stisknutych klaves
skore = [0, 0]  # skore hracu

#vykreslení hrací plochy

def nakresli_obdelnik(x1, y1, x2, y2):
    """Nakresli obdelnik na dane souradnice
    
         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
    """
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    gl.glEnd()  # ukonci kresleni trojuhelniku


okno = pg.window.Window(width = sirka, height = vyska)
pg.app.run()