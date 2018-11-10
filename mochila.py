import random
import os

def newVector(size, x=0):
    vector = []
    for i in range(0,size):
        vector.append(x)
    return vector

def newMatrix(lins, cols, x=0):
    matrix = []
    for i in range(0,lins):
        matrix.append(newVector(cols, x))
    return matrix

def mochila(nroItens, pesoMax, vec_w, vec_v):
    M = newMatrix(nroItens+1, pesoMax+1)

    for weighs in range(0,pesoMax):
        M[0][weighs] = 0
    for i in range(1, nroItens+1):
        for weighs in range(1, pesoMax+1):
            if (vec_w[i] > weighs):
                M[i][weighs] = M[i-1][weighs]
            else:
                M[i][weighs] = max(M[i-1][weighs], vec_v[i] + M[i-1][weighs-vec_w[i]])
    return M

def rand(min, max):
    return random.randrange(min, max)

def randVect(size, min, max):
    vect = [0]
    for i in range(0,size):
        num = rand(min,max+1) # = 0
        '''while num in vect:
            num = rand(min,max+1)'''
        vect.append(num)
    return vect

os.system('clear')

nroItens = rand(4,10) # 5 # numero de itens 'n'
pesoMax = rand(10,18) # 11 # peso que a mochila aguenta 'W'
weighs = randVect(nroItens+1, 1, int(pesoMax/3)+4) # [0, 1, 2, 5,  6, 7 ] # pesos
values = randVect(nroItens+1, 1, 40) # [0, 1, 6, 18, 22,28] # values

weighs.sort()
values.sort()

print("numero de itens:", nroItens)
print("capacidade da mochila: %d kg" % pesoMax)

print("\nitem valor peso")
for i in range(1, nroItens+1):
    print("%2d %4d %4d" % (i, values[i], weighs[i]))

print("\n")

matriz = mochila(nroItens, pesoMax, weighs, values)
print("matriz de n+1 itens por w+1 pesos\n")
for i in range(0, pesoMax+1):
    print("%-4d" % i, end="")
print("")
print("----"*(pesoMax+1))
for i in matriz:
    for j in i:
        print("%-4d" % j, end="")
    print("\n")
#print("\n")
print("="*40)
print("\nO valor total que a mochila pode levar é -->", matriz[nroItens][pesoMax])
print("\n\n")

#
