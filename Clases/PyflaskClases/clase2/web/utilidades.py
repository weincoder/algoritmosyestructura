import pandas as pd 

def leerArchivo (nombreArchivo) :
    diccionario = pd.read_csv(nombreArchivo, encoding='UTF-8', header=0, delimiter = ';').to_dict()
    return diccionario

def validatePassword (diccionario, userIn, passwordIn):
    users = list (diccionario ['user'].values())
    passwords = list (diccionario ['pass'].values())
    salida = ''
    if userIn not in users :
        salida =  'Usuario no registrado'
    else:
        posicion = users.index(userIn)
        originalPsw = str(passwords [posicion])
        #salida = f'El usuario {userIn} esta registrado y esta en la posición {posicion} y su contraseña {passwords[posicion]}'
        if (originalPsw == passwordIn):
            salida = True
        else:
            salida = False

    return salida

