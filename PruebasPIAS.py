#Registro de entrada en biblioteca
import datetime #Para guardar la hora exacta del registro
#Definición de clase para guardar la información
class Entradas:
    def __init__(PIA, nombre, matricula, semestre, registro=datetime.datetime.now(), UIValido=False):
        PIA.nombre = nombre
        PIA.matricula = matricula
        PIA.semestre = semestre
        PIA.registro = registro
        PIA.UIValido=UIValido
class InfoEstudiantes:
    def __init__(PIA, nombre, matricula, semestre, UIValido=False):
        PIA.nombre = nombre
        PIA.matricula = matricula
        PIA.semestre = semestre
        PIA.UIValido = UIValido
