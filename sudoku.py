"""  
Inteligencia Artificial
Grupo 5A
Andrea Hernandez                    
Fecha: 08/10/2022                        
                        """


s=int()
s=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0]]

i = 0
j = 0
 
print('introduce los valores del cuadrante 1')
for i in range(3):
    for j in range(3):
      s[i][j]=input()
      s[i][j] = int(s[i][j])
            
print('Tus datos estan ordenados de la siguiente manera')
print(s[0][0],s[0][1],s[0][2])
print(s[1][0],s[1][1],s[1][2])
print(s[2][0],s[2][1],s[2][2])    
 #-----------------------------------------------------------------------   

print('introduce los valores del cuadrante 2')
    
for i  in range(3):
    for j in range(3): 
        j+=3
        s[i][j]=input()
        s[i][j] = int(s[i][j])
     
print('Tus datos estan ordenados de la siguiente manera')
print(s[0][3],s[0][4],s[0][5])
print(s[1][3],s[1][4],s[1][5])
print(s[2][3],s[2][4],s[2][5])
 #-----------------------------------------------------------------------      

print('introduce los valores del cuadrante 3')
for i  in range(3):
    for j in range(3): 
        j+=6
        s[i][j]=input()
        s[i][j] = int(s[i][j])
     
print('Tus datos estan ordenados de la siguiente manera')
print(s[0][6],s[0][7],s[0][8])
print(s[1][6],s[1][7],s[1][8])
print(s[2][6],s[2][7],s[2][8])
 #-----------------------------------------------------------------------      
#Cuadrante del 4 al 6

print('introduce los valores del cuadrante 4')
for i in range(3):
        i+=3
        for j in range(3):
            
            s[i][j]=input()
            s[i][j] = int(s[i][j])
            
print('Tus datos estan ordenados de la siguiente manera')
print(s[3][0],s[3][1],s[3][2])
print(s[4][0],s[4][1],s[4][2])
print(s[5][0],s[5][1],s[5][2])    
 #-----------------------------------------------------------------------      
print('introduce los valores del cuadrante 5')
    
for i  in range(3):
        i+=3
        for j in range(3): 
            j+=3
            s[i][j]=input()
            s[i][j] = int(s[i][j])
     
print('Tus datos estan ordenados de la siguiente manera')
print(s[3][3],s[3][4],s[3][5])
print(s[4][3],s[4][4],s[4][5])
print(s[5][3],s[5][4],s[5][5])
 #-----------------------------------------------------------------------          
print('introduce los valores del cuadrante 6')
for i  in range(3):
        i+=3
        for j in range(3): 
            j+=6
            s[i][j]=input()
            s[i][j] = int(s[i][j])
     
print('Tus datos estan ordenados de la siguiente manera')
print(s[3][6],s[3][7],s[3][8])
print(s[4][6],s[4][7],s[4][8])
print(s[5][6],s[5][7],s[5][8])
 #-----------------------------------------------------------------------      
#cuadrante del 7 al 9

print('introduce los valores del cuadrante 7')
for i in range(3):
        i+=6
        for j in range(3):
            
            s[i][j]=input()
            s[i][j] = int(s[i][j])
            
print('Tus datos estan ordenados de la siguiente manera')
print(s[6][0],s[6][1],s[6][2])
print(s[7][0],s[7][1],s[7][2])
print(s[8][0],s[8][1],s[8][2])    

#-----------------------------------------------------------------------  
print('introduce los valores del cuadrante 8')
for i  in range(3):
        i+=6
        for j in range(3): 
            j+=3
            s[i][j]=input()
            s[i][j] = int(s[i][j])
     
print('Tus datos estan ordenados de la siguiente manera')
print(s[6][3],s[6][4],s[6][5])
print(s[7][3],s[7][4],s[7][5])
print(s[8][3],s[8][4],s[8][5])
    
 #-----------------------------------------------------------------------      
print('introduce los valores del cuadrante 9')
for i  in range(3):
        i+=6
        for j in range(3): 
            j+=6
            s[i][j]=input()
            s[i][j] = int(s[i][j])
     
print('Tus datos estan ordenados de la siguiente manera')
print(s[6][6],s[6][7],s[6][8])
print(s[7][6],s[7][7],s[7][8])
print(s[8][6],s[8][7],s[8][8])
 #-----------------------------------------------------------------------



print('Inicio del Juego \n')
for line in s:
    print ('  '.join(map(str, line)))
print ('--------------------------------------------')


def imp(s):
    for line in s:
        print ('  '.join(map(str, line)))
        
#esta cordenada nos ayuda a ubicarnos dentro de la matriz
def cordmat(val):
    if val <= 2:
        return 0
    elif val <= 5:
        return 1
    else:
        return 2

#esta funcion ayuda a saber en que posicion dentro de un cuadrante es en la que estamos
def cordenadaCuad(x, y, s):
    colCua = cordmat(x)
    filCua = cordmat(y)
    
    cuadrante = []
    for fila in s[filCua *3: filCua *3 + 3]:
        for col in fila[colCua *3: colCua *3 + 3]:
            cuadrante.append(col)
            
    return cuadrante

# esta funcion revisa filas, columnas y cuadrantes, para verificar que no se repita ningun valor
def es_posible(x, y, v, s):
    # Revisar la fila
    if v in s[y]:
        return False
    # revisar la columna
    col = [fila[x] for fila in s]
    if v in col:
        return False
    # Revisar cuadrates 
    cua = cordenadaCuad(x, y, s)
    if v in cua:
        return False
    
    return True


def solS(s):
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0:
                for valor in range(1,10):# ciclo para agregar un valor 
                    if es_posible(x, y, valor, s):# en caso de no repetirse
                        s[y][x] = valor #se asigna un valor 
                        solS(s) # se le vuelve a llamar a la funcion para resolver el nuevo estado
                        s[y][x] = 0 #si el valor no era el bueno, se regresa a su estado anterior
                return
    imp(s) #si se le da una tabulacion se ven todos los pasos, peeero tarda muchoooo :c, a veces no sale todo
    
    return


print('Solucion \n')           
solS(s)