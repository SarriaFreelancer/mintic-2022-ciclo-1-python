#operaciones de los conjuntos
# operadores    métodos                 descripción
# | (alt +124)  union                   Unión
# &             intersecction           Intersección
# -             difference              Diferencia
# ^             symmetric_difference    Diferencia simétrica

CultivosZonaA = {'Papa', 'Maíz', 'Trigo'}
CultivosZonaB = {'Plátano', 'Maíz', 'Caña'}
print(CultivosZonaA | CultivosZonaB)
print(CultivosZonaA & CultivosZonaB)
print(CultivosZonaA - CultivosZonaB)
print(CultivosZonaB - CultivosZonaA)
print(CultivosZonaA ^ CultivosZonaB)
print(CultivosZonaA.union(CultivosZonaB))
print(CultivosZonaA.intersection(CultivosZonaB))
print(CultivosZonaA.difference(CultivosZonaB))
print(CultivosZonaB.difference(CultivosZonaA))
print(CultivosZonaA.symmetric_difference(CultivosZonaB))
