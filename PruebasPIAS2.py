import json
from PruebasPIAS import Entradas
from PruebasPIAS import InfoEstudiantes
from operator import attrgetter
entrada=[]
info_alumnos = []
print("Por favor complete con sus datos")
while True:
    Nombre = input("Dame tu nombre completo: ")
    Matricula = input("Dame tu matrícula: ")
    Semestre = input("¿En que semestre vas? ")
    continuar = input("¿Quieres continuar? (Si/No) ")
    persona=Entradas(Nombre, Matricula,Semestre)
    persona2 = InfoEstudiantes(Nombre, Matricula, Semestre)
    info_alumnos = info_alumnos + [persona2]
    entrada = entrada + [persona]
    persona = " "
    if continuar == "No":
        break

def Información(y):
    print(y.nombre)
    print(y.matricula)
    print(y.semestre)
    print(y.registro)
    
for persona in entrada:
    print("------------------------------------------")
    Información(persona)
    
entrada.sort(key=attrgetter("matricula"),reverse=False)
def InformacionOrdenada(z):
    print(z.matricula)
    print(z.nombre)
    print(z.semestre)
    print(z.registro)

print("Información ordenada")
for x in entrada:
    print("------------------------------------------")
    InformacionOrdenada(x)
    
json_data = json.dumps(info_alumnos, default=lambda o: o.__dict__, indent=4)
print(json_data)