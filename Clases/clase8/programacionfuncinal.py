def line_design ():
    print ('#'*60)
line_design ()
line = lambda : print ('#'*60)
print ('ahora usando lambdas')
line()

print('caso2')
def line_design_e (cantidad):
    print ('#'*cantidad)
line_design_e(10)
line = lambda cantidad : print ('#'*cantidad)
print ('con lambdas')
line(10)

sumar = lambda valor1=0, valor2=0 : valor1+valor2
restar = lambda valor1=0, valor2=0 : valor1-valor2
multiplicar = lambda valor1=0, valor2=0 : valor1*valor2
dividir = lambda valor1=0, valor2=0 : valor1/valor2
print (sumar(1,2))
print (restar(1,2))
print (multiplicar(42,48))
print (dividir(1,2))
calculadora = lambda operacion, valor1=0, valor2 =0 : print(operacion (valor1, valor2))
calculadora(dividir, 83,87)

#Map 
listaNotas = [3,1.8,2.7,3.4,4]
for i in range (len (listaNotas)):
    listaNotas[i] +=1 
print (listaNotas)
listaNotas = [3,1,2,3,4]
sumar1 = lambda valor: valor+1
adicionar = list(map(sumar1, listaNotas)) 
print (adicionar)
for i in range (len (listaNotas)):
    listaNotas[i] =listaNotas[i] **2

print (listaNotas)
listaNotas = [3,1,2,3,4]
exponte = lambda elemento : elemento**2
listaCuadrados = list(map(exponte,listaNotas))
print(listaCuadrados)

#filter
listaNumeros = [1,2,3,45,23,4,8,9,20]
listaPares = []
for numero in listaNumeros: 
    if numero % 2 == 0 :
        listaPares.append(numero)
print (listaPares)
par = lambda elemento : elemento %2 == 0
pares = list (filter(par,listaNumeros))
print (pares)