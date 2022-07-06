# Un diccionario es una estructura de datos se utilizan para almacena 
# datos o valores en pares llamados clave-valor o llave-valor 
# clave: valor, ejemplo->> 'nombre':'Marina', 'ciudad': 'Barranquilla'
# Son mutables y no permiten llaves duplicadas

datosPersonales = {
    'nombre': 'Carlos',
    'edad': 40,
    'id': 32658741,
    'telefono': 3015874896,
    'direccion': 'Calle 75 89 25',
    'Permiso_AR': True,
    'hijos': {'hijo1': 'María', 'hijo2': 'Sofía'},
    123: 'prueba',
    456: 0
}

dic = {
    'a': 1, 
    'b': 2, 
    'c': 3, 
    'd': 4
}

print(datosPersonales['telefono'])
print(datosPersonales)
datosPersonales['direccion']= "Carrera 45 33 10"
print(datosPersonales)
print(type(datosPersonales), type(datosPersonales['Permiso_AR']), type(datosPersonales['edad']))
print(type(datosPersonales['hijos']['hijo1']))
print(datosPersonales['hijos']['hijo1'])
print(datosPersonales['hijos']['hijo2'])

print(dic)
lista = list(dic.items())
print(lista)
nuevodic = dict(lista)
print(nuevodic)
for termino, valor in nuevodic.items():
    #print(termino, valor)
    print(('{}:{}').format(termino, valor))
