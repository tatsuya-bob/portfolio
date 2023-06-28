#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:10:15 2023

@author: kanoutatsuya
"""

import pygame as pg
from pygame.locals import *
from pygame import mixer 
import sys
import time
import random as rd


img6 = pg.image.load("slot6_s.png")
img7 = pg.image.load("slot6_s.png")
img8 = pg.image.load("slot6_s.png")
img9 = pg.image.load("JG_body.png")
img10 = pg.image.load("JG_body2.png")




def main():
    pg.init()
    (w, h) = (500, 500)
    screen = pg.display.set_mode((w, h))
    pg.display.set_caption("Test")
    clock = pg.time.Clock()
    y1,y2,y3=300,300,300
    body=img9.get_rect()
    body2=img10.get_rect()
    reel_R=img6.get_rect()
    reel_C=img7.get_rect()
    reel_L=img8.get_rect()
    
   
    
    body.center=(w/2,h/2)
    body2.center=(w/2,h/2)
    reel_R.center=(180,y1)
    reel_C.center=(250,y2)
    reel_L.center=(320,y3)
    button1 = pg.Rect(130, 285, 30, 30)
    button2 = pg.Rect(195, 285, 30, 30)
    button3 = pg.Rect(240, 285, 30, 30)
    button4 = pg.Rect(280, 285, 30, 30)
    
    lottery = False
    result = rd.randint(1, 10)
    
    a = False
    b = False
    c = False
    #cherry

    gmax=2
    gcnt=0
    mflg =0
    

    while (1):
        
        pg.draw.rect(screen, (255, 0, 0), button1)
        pg.draw.rect(screen, (0, 255, 0), button2)
        pg.draw.rect(screen, (255, 0, 0), button3)
        pg.draw.rect(screen, (0, 255, 0), button4)
        screen.blit(img6,reel_R)
        screen.blit(img6,reel_C)
        screen.blit(img6,reel_L)
        
        
        
        if gcnt>gmax :
            screen.blit(img10,body2)
            body.center=(w/2,h/2)
            
            if mflg == 0:
                
                pg.mixer.music.load("peka.mp3")
                pg.mixer.music.play(1)
                time.sleep(0.5)
                pg.mixer.music.stop()
                mflg=1
           
           
        else :
            screen.blit(img9,body)
            body.center=(w/2,h/2)
        
        reel_R.center=(180,y1)
        reel_C.center=(250,y2)
        reel_L.center=(320,y3)
       
       
       
        
        
        if lottery == True:
            result=rd.randint(1, 10)
            print(result)
            lottery=False
        
        
        if a == True:
            y1 += 1
        if b == True:
            y2 += 1
        if c == True:
            y3 += 1
        
        if y1 > 350:
            y1 = 0
        if y2 > 350: 
            y2 = 0
        if y3 > 350:
            y3 = 0
        
        pg.display.update()
        clock.tick(500)
        
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    lottery=True
                    a = True
                    b = True
                    c = True
                    gcnt = gcnt + 1
                    
                    pg.mixer.music.load("start.mp3")
                    pg.mixer.music.play(1)
                    time.sleep(1.5)
                    pg.mixer.music.stop()
                    
                if button2.collidepoint(event.pos):
                    
                    z1 = y1 % 50
                    z=50-z1
                    if z!=50:
                        y1=y1+z
                    a = False
                    if gcnt>gmax:
                        y1=50
                    
                    pg.mixer.music.load("stop.mp3")
                    pg.mixer.music.play(1)
                    time.sleep(0.5)
                    pg.mixer.music.stop()
                    
                    
                if button3.collidepoint(event.pos):
                    
                    z2 = y2 % 50
                    z=50-z2
                    if z!=50:
                        y2=y2+z
                    b = False
                    if gcnt>gmax:
                        y2=50
                    
                    pg.mixer.music.load("stop.mp3")
                    pg.mixer.music.play(1)
                    time.sleep(0.5)
                    pg.mixer.music.stop()
                    
                    
                if button4.collidepoint(event.pos):
                    
                    z3 = y3 % 50
                    z=50-z3
                    if z!=50:
                        y3=y3+z
                    
                    if gcnt<gmax:
                        if y3==50:
                            y3=100
                    if gcnt>gmax:
                        y3=50
                        
                    
                    c = False
                    
                    pg.mixer.music.load("stop.mp3")
                 
                    pg.mixer.music.play(1)
                  
                    time.sleep(0.5)
                  
                    pg.mixer.music.stop()
                 
                    if y1==50 & y2==50 & y3==50:
                        
                        pg.mixer.music.load("BigBonus.mp3")
                        
                        pg.mixer.music.play(1)
                       
                   
                    
                    
    


if __name__ == "__main__":
    main()