# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 09:34:19 2018

@author: Vašek
"""

import pyglet as pg
from pyglet import gl
from pyglet.window import key

#Velikost okna

sirka = 900
vyska = 600

velmic = 25
sirpalka = 10
delpalka = 100
rychlost = 200
rychpalka = rychlost * 1.5

delkapulcary = 20
velfont = 40
odsazenitextu = 30

 #potřebné proměnné

pozpalek = [vyska // 2, vyska // 2]  # vertikalni pozice palek
pozmic = [0, 0]  # souradnice micku 
rychlostmic = [0, 0]   
stiskklavesy = set()  # sada stisknutych klaves
skore = [0, 0]  # skore hracu


window = pg.window.Window(width = sirka, height = vyska)
#vykreslení hrací plochy

def nakresli_obdelnik(x1, y1, x2, y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    gl.glEnd()  # ukonci kresleni trojuhelniku

#smazáni plochy
...
def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna
    gl.glColor3f(1, 1, 1)  # barva kresleni - bila

window = pg.window.Window(width = sirka, height = vyska)
window.push_handlers(on_draw=vykresli)


#vykreslení míčku
  
def vykresli():
    ...
    nakresli_obdelnik(
            pozmic[0] - velmic // 2,
            pozmic[1] - velmic // 2,
            pozmic[0] + velmic // 2,
            pozmic[1] + velmic // 2,)
      
#vykreslení pálek
    
def vykresli():
    ...
    for x, y in [(0, pozpalek[0]), (sirka, pozpalek[1])]:
        nakresli_obdelnik(
                x - sirpalka,
                y - delpalka // 2,
                x + sirpalka,
                y + delpalka // 2,)
        
#vykreslení pulící čáry
        
def vykresli():
    ...
    for y in range(delkapulcary // 2, vyska, delkapulcary * 2):
        nakresli_obdelnik(
                sirka // 2 - 1,
                y,
                sirka // 2 + 1,
                y + delkapulcary)

#vykreslení skóre
        
def nakresli_text(text, x, y, pozice_x):
    napis = pg.text.Label(
            text,
            font_size=velfont,
            x=x, y=y, anchor_x=pozice_x)
    napis.draw()
    
#nakreslení skóre
    
def vykresli():
    ...
    nakresli_text(
        str(skore[0]),
        x=odsazenitextu,
        y=vyska - odsazenitextu - velfont,
        pozice_x='left')

    nakresli_text(
        str(skore[1]),
        x=sirka - odsazenitextu,
        y=vyska - odsazenitextu - velfont,
        pozice_x='right')
    
#klavesy
    
def stisk_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stiskklavesy.add(('nah', 0))
    if symbol == key.S:
        stiskklavesy.add(('dol', 0))
    if symbol == key.UP:
        stiskklavesy.add(('nah', 1))
    if symbol == key.DOWN:
        stiskklavesy.add(('dol', 1))

def pusteni_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stiskklavesy.discard(('nah', 0))
    if symbol == key.S:
        stiskklavesy.discard(('dol', 0))
    if symbol == key.UP:
        stiskklavesy.discard(('nah', 1))
    if symbol == key.DOWN:
        stiskklavesy.discard(('dol', 1))

window = pg.window.Window(width=sirka, height=vyska)
window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
    on_key_press=stiskklavesy,
    on_key_release=pusteni_klavesy)

pg.app.run()

