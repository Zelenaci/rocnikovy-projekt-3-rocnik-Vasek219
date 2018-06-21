# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 09:34:19 2018

@author: Vašek
"""

import pyglet as pg
from pyglet import gl
from pyglet.window.key import DOWN, UP, W, S
import random

sirka = 900
vyska = 600

velmic = 18
sirpalka = 10
delpalka = 100
rychlost = 200
rychpalka = rychlost * 1.5

delkapulcary = 20
velfont = 40
odsazenitextu = 30

pozpalek = [vyska // 2, vyska // 2]  # vertikalni pozice palek
pozmic = [0, 0]  # souradnice micku 
rychlostmic = [0, 0]   
stiskklavesy = set()  # sada stisknutych klaves
skore = [0, -1]  # skore hracu



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
    gl.glColor3f(255,255,255)  # barva kresleni - bila
    
#vykreslení míče    
    
    nakresli_obdelnik(
            pozmic[0] - velmic // 2,
            pozmic[1] - velmic // 2,
            pozmic[0] + velmic // 2,
            pozmic[1] + velmic // 2,)
    
#vykreslení pálek    
    
    for x, y in [(0, pozpalek[0]), (sirka, pozpalek[1])]:
        nakresli_obdelnik(
                x - sirpalka,
                y - delpalka // 2,
                x + sirpalka,
                y + delpalka // 2,)
        
#vykreslení pulící čáry        
        
    for y in range(delkapulcary // 2, vyska, delkapulcary * 2):
        nakresli_obdelnik(
                sirka // 2 - 1,
                y,
                sirka // 2 + 1,
                y + delkapulcary)
        
#vykreslení skóre        
        
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
        
        
def nakresli_text(text, x, y, pozice_x):
    napis = pg.text.Label(
            text,
            color=(204, 51, 0,255),
            bold=True,
            font_size=velfont,
            x=x, y=y, anchor_x=pozice_x)
    napis.draw()
    
#klavesy
    
def stisk_klavesy(symbol, modifikatory):
    if symbol == W:
        stiskklavesy.add(('nahoru', 0))
    if symbol == S:
        stiskklavesy.add(('dolu', 0))
    if symbol == UP:
        stiskklavesy.add(('nahoru', 1))
    if symbol == DOWN:
        stiskklavesy.add(('dolu', 1))

def pusteni_klavesy(symbol, modifikatory):
    if symbol == W:
        stiskklavesy.discard(('nahoru', 0))
    if symbol == S:
        stiskklavesy.discard(('dolu', 0))
    if symbol == UP:
        stiskklavesy.discard(('nahoru', 1))
    if symbol == DOWN:
        stiskklavesy.discard(('dolu', 1))
        
#rychlost míče na začátku
        
def reset():
    pozmic[0] = sirka // 2
    pozmic[1] = vyska // 2

    if random.randint(0, 1):
        rychlostmic[0] = rychlost
    else:
        rychlostmic[0] = -rychlost

    rychlostmic[1] = random.uniform(-1, 1) * rychlost
        
def obnov_stav(dt):
    
#pohyb pálek    
    
    for cislo_palky in (0, 1):
        if ('nahoru', cislo_palky) in stiskklavesy:
            pozpalek[cislo_palky] += rychpalka * dt
        if ('dolu', cislo_palky) in stiskklavesy:
            pozpalek[cislo_palky] -= rychpalka * dt

        if pozpalek[cislo_palky] < delpalka / 2:
            pozpalek[cislo_palky] = delpalka / 2
        if pozpalek[cislo_palky] > vyska - delpalka / 2:
            pozpalek[cislo_palky] = vyska - delpalka / 2
            

#pohyb míče
            
    pozmic[0] += rychlostmic[0] * dt
    pozmic[1] += rychlostmic[1] * dt  
    
#odraz míče
    
    if pozmic[1] < velmic // 2:
        rychlostmic[1] = abs(rychlostmic[1])
    if pozmic[1] > vyska - velmic // 2:
        rychlostmic[1] = -abs(rychlostmic[1])
    
    palka_min = pozmic[1] - velmic / 2 - delpalka / 2
    palka_max = pozmic[1] + velmic / 2 + delpalka / 2
    
#odražení vlevo
    
    if pozmic[0] < sirpalka + velmic / 2:
        if palka_min < pozpalek[0] < palka_max:
            #palka odrazi mic
            rychlostmic[0] = abs(rychlostmic[0])
        else:
            #palka je mimo a hrac prohral
            skore[1] += 1
            reset()

#odražení vpravo
    if pozmic[0] > sirka - (sirpalka + velmic / 2):
        if palka_min < pozpalek[1] < palka_max:
            rychlostmic[0] = -abs(rychlostmic[0])
        else:
            skore[0] += 1
            reset()
            
pg.clock.schedule(obnov_stav)
window = pg.window.Window(width=sirka, height=vyska)
window.push_handlers(
    on_draw=vykresli,  # na vykresleni okna pouzij funkci `vykresli`
    on_key_press=stisk_klavesy,
    on_key_release=pusteni_klavesy)

pg.app.run()

