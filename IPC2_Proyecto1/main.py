from tkinter import *
from tkinter import filedialog
from lxml import etree as t

def Inicio():
    print("BIENVENIDO USUARIO")
    print("cargue su archivo porfavor..")
    global archivo
    archivo=filedialog.askopenfilename(filetypes=[("Archivos XML", ".xml .XML")])
    print("\n Archivo procesado exitosamente")
    if archivo!=None:
        Menu()
    else:
        print("No se reconocio el archivo")

def Menu():
    print("llego")


# Inicio de ejecucion
if __name__ == '__main__':
    Inicio()