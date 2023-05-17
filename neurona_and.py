import random
#iniciamos los datos de tabla de verdad
datas=[[1,1,1], [1,0,0], [0,1,0], [0,0,0]]
#pesos aleatrorios
weights=[random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)]

learning = True
out_enter = 0
iteration = 0
tasaLearn = 0
iterations = 0

while(learning==True):
    iteration+=1
    learning=False
    for cont in range(0,4):
        realOut= (datas[cont][0]*weights[0]+datas[cont][1]*weights[1]+1*weights[2])
        if realOut > 0:
            out_enter = 1
        else:
            out_enter

        error = int(datas[cont][2] - out_enter)


        if (error!=0):
            weights[0]+=tasaLearn * error * datas[cont][0]
            weights[1]+=tasaLearn * error * datas[cont][1]
            weights[2]+=tasaLearn * error *1
            learning = True


    if learning ==  False:
        break

print("iterations = ", iteration)
print("Peso 1", weights[0]) 
print("Peso 2", weights[1])
print("Peso 3", weights[3])

for cont in range(0,1):
    if realOut >0:
        out_enter = 1
    else:
        print("entradas: ",datas[cont][0], datas[cont][1], datas[cont][2] "perceptron = ", out_enter)

