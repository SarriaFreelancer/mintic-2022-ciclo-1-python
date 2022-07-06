import numpy as np
import pandas as pd

inventario2 = {'hola': [562,78,45],
            'como': [45,462, 21],
            'por que': [58,55, 232],
            'siempre': [372,62, 34]}
prueba2 = pd.DataFrame(inventario2, columns=['llave','Valor1','Valor2','Valor3'], index=['Primero','Segundo','Tercero', 'Cuarto'])
print(inventario2)
print(prueba2, '\n')
print(prueba2.columns)
 
inventario = {
    'Impresoras': ['Canon', 'Hp', 'Epson'],
    'Cantidad': [10,8,15]
}
print(inventario, '\n')
prueba = pd.DataFrame(inventario, index=['P1','P2','P3'])
print(prueba, '\n')
print(prueba.iloc[1])
print(prueba.loc['P1'])
