from  keypad import get_key
from math import *
from screen import pantalla_cal

linea1=""
valor=""
strQ=""
idMode=0
strMode=["Alpha","Shift","Def"]
strDisplay="Text"
ans=0
print("Entramos al bucle principal")

while 1==1 :
    strQ=get_key(Files,Columns,Caracteres,idMode)
    if strQ != "" :
        #print(strQ)
        if strQ == "del" :
            linea1 = linea1[:-1]
        elif strQ == "eval" :
            try:
                ans = eval(linea1)
                valor = str(ans)
            except:
                valor = "Eval error"
        elif strQ == "exe" :
            try:
                exec(linea1)
            except:
                valor="Exec error"
            valor = "EXECUTED"
        elif strQ == "graph" :
            print("graph")
            if strDisplay=="Text":
                strDisplay="graph"
            else:
                strDisplay="Text"
        elif strQ == "mode" :
            idMode=idMode+1
            if (idMode > len(strMode)-1 ):
                idMode=0
        else :
            linea1 = linea1 + strQ
        
        pantalla_cal(linea1,valor,strMode[idMode])        
        
       
        
