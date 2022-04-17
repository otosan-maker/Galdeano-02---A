from machine import SDCard
from machine import Pin , SPI
import os
try:
    #spi = SPI(1, baudrate=33000000, sck=Pin(18), mosi=Pin(23))
    sd = SDCard(slot=3, miso=Pin(19), mosi=Pin(23), sck=Pin(18), cs=Pin(5),freq=2500000)
    sd.info()
    os.mount(sd, '/sd')
    print("SD card mounted at \"/sdcard\"")
    sys.path.append('/sdcard/pruebas')
except (KeyboardInterrupt, Exception) as e:
    print('SD mount caught exception {} {}'.format(type(e).__name__, e))
    pass