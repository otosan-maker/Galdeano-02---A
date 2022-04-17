# This file is executed on every boot (including wake-boot from deepsleep)
from machine import Pin, SPI
from screen import initGraf



#define F1 25
#define F2 26
#define F3 27
#define F4 14
#define F5 12
#define F6 13
#define C1 34
#define C2 35
#define C3 32
#define C4 33
#define C5 22
#define C6 39
#define C7 36

F1 = Pin(25, Pin.OUT)
F2 = Pin(26, Pin.OUT)
F3 = Pin(27, Pin.OUT)
F4 = Pin(14, Pin.OUT)
F5 = Pin(12, Pin.OUT)
F6 = Pin(13, Pin.OUT)

F1.off()
F2.off()
F3.off()
F4.off()
F5.off()
F6.off()

C1 = Pin(34, Pin.IN, Pin.PULL_DOWN)
C2 = Pin(35, Pin.IN, Pin.PULL_DOWN)
C3 = Pin(32, Pin.IN, Pin.PULL_DOWN)
C4 = Pin(33, Pin.IN, Pin.PULL_DOWN)
C5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
C6 = Pin(39, Pin.IN, Pin.PULL_DOWN)
C7 = Pin(36, Pin.IN, Pin.PULL_DOWN)

Columns = [ C1, C2, C3, C4, C5, C6 , C7]
Files = [ F1, F2, F3, F4, F5, F6]

Caracteres = [
    [["a","g","m","1","4","7"," "],
     ["b","h","n","2","5","8","0"],
     ["c","i","o","3","6","9","."],
     ["d","j","p","s","v","shift","mode"],
     ["e","k","q","t","x","cntl","del"],
     ["f","l","r","u","y","z","exe"]],
    [["A","G","M","1","4","7","\""],
     ["B","H","N","2","5","8","0"],
     ["C","I","O","3","6","9",","],
     ["D","J","P","S","V","shift","mode"],
     ["E","K","Q","T","X","cntl","del"],
     ["F","L","R","U","Y","Z","exe"]],
    [["a","g","m","1","4","7",","],
     ["b","h","n","2","5","8","0"],
     ["c","i","o","3","6","9","."],
     ["d","j","p","s","v","shift","mode"],
     ["e","k","q","t","x","cntl","del"],
     ["f","l","r","u","x","z","exe"]] ]


spi = SPI(1, baudrate=3300000, sck=Pin(18), mosi=Pin(23))
initGraf(spi)
