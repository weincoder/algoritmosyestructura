import utilidades as helper
import pandas as pd 
data =helper.leerArchivo('usuarios.csv')
print (data)
print (data['user'])
nombre = 'pepito'
psw = '1234'

listaNombres = list (data['user'].values())
listaNombres.append(nombre)
listaPsw =  list (data['pass'].values())
listaPsw.append(psw)

data ['user'] = listaNombres
data ['pass'] = listaPsw
print (data)
dataFrameUser = pd.DataFrame(data)
dataFrameUser.to_csv ('hola.csv', index= False, sep=';')