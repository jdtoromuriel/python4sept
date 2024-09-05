# #Tupla

# tuplaNros = (12,15,14,16)
# print(tuplaNros)
# for nro in tuplaNros:
#     print(f"El numero de la tupla es: {nro}")
# # Buscar un numero en la tupla
# nroBuscar = int(input("Ingrese el numero a buscar en la tupla: "))
# i = 0

# #Variable tipo bandera
# # bandera = False
# for num in tuplaNros:   
#     if num == nroBuscar:
#         # bandera = True
#         break
#     i +=1
# # if bandera:
# if i < len(tuplaNros):
#     print(f"El numero {nroBuscar} esta en la posicion {i}")
# else:
#     print(f"El numero {nroBuscar} no se encontró")
    
# set (conjunto de datos)

conj = ("Maria", "Pedro", "Teresa", "Valentina")
print(conj)
for nomre in conj:
    print(nomre)
# Diccionario
dicProducto = {"ref": "A01", "nombre": "Mouse", "Precio": 25000, "estado": False}
for key, value in dicProducto.items():
    print(f"{key}:{value}")
print(dicProducto["nombre"])
# Lista con diccionario 

empleados = [
    {"id": "10", "fullname": "Teresa Valencia", "Salario": 2500000},
    {"id": "11", "fullname": "Fausto Zapata", "Salario": 3500000},
    {"id": "12", "fullname": "Otilia Bonilla", "Salario": 4500000},
]

# Iterar en empleados

for emp in empleados:
    print(f"El nombre completo es: {emp["fullname"]}")
acumSalario = 0
for employee in empleados:
    acumSalario += employee["Salario"]
promSalario = acumSalario / len(empleados)
print(f"El promedio de salarios es: {promSalario}")