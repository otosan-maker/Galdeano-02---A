from machine import Pin
import time


strLastKey="Inicio"

def get_key(Files,Columns,Caracteres,idMode):
    strValue=""
    global strLastKey
    for idFil,file in enumerate( Files):
        file.on()
        for idCol,col in enumerate(Columns):
            if col.value() == 1:
                strValue=Caracteres[idMode][idFil][idCol]
        file.off()
    if strValue == strLastKey:
        return ""
    else:
        strLastKey=strValue
        return strValue