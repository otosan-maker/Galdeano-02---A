from machine import Pin, SPI
from ili9341 import Display,color565
from xglcd_font import XglcdFont
import random

def initGraf(spi):
    global display
    global stdFont
    display = Display(spi, dc=Pin(2), cs=Pin(15), rst=Pin(4),width=320, height=240, rotation=90)
    stdFont =XglcdFont('fonts/Unispace12x24.c', 12, 24)
    initScreen()
    
    
def initScreen():
    global stdFont
    
    for iTerator in range(20):
        display.draw_line(50, 50, random.randint(0, 100),random.randint(0, 100), color565(random.randint(0, 255), 120, 0))
    
    display.draw_text(150, 120, "Init Finished", stdFont,color565(255, 10, 20))



def  pantalla_cal(linea1,valor,cadMode):
    global display
    global stdFont
    display.clear()
    display.draw_text(23, 23, ""+linea1, stdFont,color565(255, 255, 0))
    
    display.draw_text(23, 63, "= "+valor, stdFont,color565(255, 255, 0))
    
    #display.hline(50, 38, 120, 1)
    #display.hline(4, 55, 120, 1)
    display.draw_text(23, 193, "* "+cadMode, stdFont,color565(55, 155, 200))



