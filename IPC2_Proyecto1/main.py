from tkinter import *
from tkinter import filedialog
from xml.dom.minidom import ElementInfo
import xml.etree.ElementTree as ET
import re
from ListaPatron import ListaPatron
from ListaPisos import ListaPisos
import os
import webbrowser
pisos=None
elem= None
def Inicio():
    opcion = ""
    while True:
        print("========= ROBOT PISOS ARTESANALES =========")
        print("|1. Cargar Archivo                        |")
        print("|2. Mostrar los pisos cargados            |")
        print("|3. Mostrar los patrones cargados         |")
        print("|4. Mostrar graficamente el patron        |")
        print("|5. Seleccionar un nuevo código de patron |")
        print("|6. Salir                                 |")
        print("===========================================")
        print("Ingrese Opcion:")
        opcion = int(input(">. "))
        Menu(opcion)
        print("\n")
        if (opcion >= 1 and opcion <= 6):
            break

def Menu(opcion):
    global archivo
    archivo=""
    if opcion == 1:
        archivo=filedialog.askopenfilename(filetypes=[("Archivos XML", ".xml .XML")])
        print(archivo)
        if archivo!="":
            Lectura(archivo)
            Inicio()
        else:
            print("No se reconocio el archivo")
            Inicio()
    elif opcion == 2:
        if pisos!=None:
            pisos.ordenar()
            print("Pisos cargados ordenados alfabeticamente")
            pisos.imprimirSimpleEnla()
        else:
            print("No se ha cargado el archivo")
            Inicio()
    elif opcion == 3:
        if elem!=None:
            print("Ingrese el nombre del piso en el cual quiere ver los patrones")
            nome =str(input(">. "))
            nome = pisos.getPiso(nome)
            nome.lista_patron.OrdenarPatron()
            print("Patrones cargados ordenados alfabeticamente")
            nome.lista_patron.imprimirSimpleEnlaPa()
        else:
            print("No se ha cargado el archivo")
            Inicio()
    elif opcion == 4:
        if elem!=None:
            print("Ingrese el nombre del piso en el cual quiere ver los patrones")
            nome =str(input(">. "))
            nome = pisos.getPiso(nome)
            nome.lista_patron.OrdenarPatron()
            print("Patrones cargados con este nombre de piso")
            nome.lista_patron.imprimirSimpleEnlaPa()
            print("Ingrese el codigo de patron:")
            pat = input(">. ")
            elem1= nome.lista_patron.getPatron(pat)
            Grafica4(nome,elem1)
            Inicio()
        else:
            print("No se ha cargado el archivo")
            Inicio()
    elif opcion == 5:
        if elem!=None:
            print("Ingrese el nombre del piso en el cual quiere elegir los patrones")
            nome =str(input(">. "))
            nome = pisos.getPiso(nome)
            nome.lista_patron.OrdenarPatron()
            print("Patrones cargados con este nombre de piso")
            nome.lista_patron.imprimirSimpleEnlaPa()
            print("Ingrese el codigo de patron que quiere cambiar:")
            pat = input(">. ")
            elem1= nome.lista_patron.getPatron(pat)
            print("Ingrese el codigo de patron con el que quiere cambiar:")
            pat1 = input(">. ")
            elem11= nome.lista_patron.getPatron(pat1)
            Inicio1()
        else:
            print("No se ha cargado el archivo")
            Inicio()
    elif opcion == 6:
        opcion = 7
        print("\n=== ¡HASTA PRONTO! ====")
    else:
        print("\n====¡OPCION NO EXISTENTE!====")

def Inicio1():
    op = ""
    while True:
        print("========= ROBOT PISOS ARTESANALES =========")
        print("|1. Costo mínimo para realizar el cambio  |")
        print("|2. Instrucciones para hacer el cambio    |")
        print("|3. Mostrar graficamente el nuevo patron  |")
        print("|4. Menu principal                        |")
        print("===========================================")
        print("Ingrese Opcion:")
        op = int(input(">. "))
        Menu1(op)
        print("\n")
        if (op >= 1 and op <= 4):
            break

def Menu1(op):
    if op == 1:
        print("Costo minimo")
    elif op == 2:
        #Buscando(elem1, elem11)
        opc=5
        Menu(opc)
    elif op == 3:
        #Grafica4(nome,elem1)
        opc=5
        Menu(opc)
    elif op == 4:
        op=5
        Inicio()
    else:
        print("\n====¡OPCION NO EXISTENTE!====")
                
        

def Lectura(archivo):
        tree = ET.parse(archivo)
        raiz = tree.getroot()
        global pisos
        pisos = ListaPisos()
        global nombre, r, c, f, s, codigo, patron
        nombre = ""
        r = ""
        c = ""
        f = ""
        s = ""
        codigo = ""
        patron = ""
        print("===== ¡ARCHIVO LEIDO CORRECTAMENTE! ====")
        for elemento in raiz:
            nombre = elemento.attrib['nombre']
            # Pisos
            for belemento in elemento.iter('R'):
                r = belemento.text
            for belemento in elemento.iter('C'):
                c = belemento.text
            for belemento in elemento.iter('F'):
                f = belemento.text
            for belemento in elemento.iter('S'):
                s = belemento.text

            pisos.insertarSimpleEnla(
                    nombre, r, c,f,s)
            # Patrones
            for subelemento in elemento.iter('patron'):
                global elem,elem1
                elem = pisos.getPiso(nombre)
                codigo=subelemento.attrib['codigo']
                patron=subelemento.text
                patron=patron.replace(" ","")
                patron=patron.replace("\n","")   
                elem.lista_patron.insertarSimpleEnlaPa(codigo, patron)
                # Celdas
                elem1= elem.lista_patron.getPatron(codigo)
                longi = list(patron)
                divi=[longi[j:j + int(c)] for j in range(0,len(longi),int(c))]
                for i in range(int(r)):
                    for o in range(int(c)):
                        color=str(divi[i][o])
                        elem1.lista_celda.insertarCelda(str(i),str(o),color) 

def Grafica4(nome,patron):
        count = 0
        grafico = open("graficapatron.dot", 'w+')
        grafico.write('digraph G {\n')
        grafico.write('node[shape=box fillcolor="pink:yellow" style =filled]\n')
        grafico.write(''' subgraph cluster_p{
            label= "REPORTE CELDA"
            bgcolor = "pink"''')
        grafico.write('nodoP[label="{}" shape="box"];\n'.format(patron.codigo))

        tmp = patron.lista_celda.inicio2
        while tmp is not None:
            if(tmp.color=="W"):
                grafico.write('name{}[label="{}" fillcolor="white" shape="box"];\n'.format(count,  tmp.color))
            else:
                grafico.write('name{}[label="{}" fillcolor="black" shape="box"];\n'.format(count,  tmp.color))
            count += 1
            tmp = tmp.siguiente2
        length = int(nome.Co)
        count3 = 0
        for i in range(length):
            grafico.write('nodoP -> name{};\n'.format(count3))
            count3 += 1
            sum = int(nome.Co)

        for i in range((sum*int(nome.Ro))-length):
            grafico.write('name{} -> name{};\n'.format(i, (i + sum)))
        grafico.write('}\n}\n')
        grafico.close()
        os.system('dot.exe -Tpng graficapatron.dot -o '+patron.codigo+'_reporte.png')
        os.system('dot.exe -Tpdf graficapatron.dot -o '+patron.codigo+'_reporte.pdf')
        os.startfile(patron.codigo+'_reporte.pdf')


def Buscando( pat1, pat2):
    tmp = pat1.lista_celda.inicio2
    tmp1= pat2.lista_celda.inicio2
    print("Buscando cambios que se deben hacer")
    conta=0
    while tmp is not None:
        tante=tmp.anterior2
        tsigue=tmp.siguiente2
        if (tmp.Ro == tmp1.Ro) and (tmp.Co == tmp1.Co): 
            if(tmp.color != tmp1.color):
                print("Cambiar en la posicion: "+ tmp.Ro +","+ tmp.Co +" El patron: "+ tmp.color+ " por: "+ tmp1.color)
                if(conta<2):
                   Intermambio(tante,tsigue,tmp,tmp1)
                   conta +=1
                else:
                    print("Ya no se puede hacer mas intercambios en esta operacion")

                '''
                if(conta<=2):
                    if tante!=None and (tante.color == tmp1.color) and tmp.color:
                        print("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tante.Ro +","+ tante.Co)  
                        tmp.color= tante.color
                    elif tsigue!=None and(tsigue.color == tmp1.color) and tmp.color:
                        print("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tsigue.Ro +","+ tsigue.Co)  
                        tmp.color= tsigue.color
                    else:
                        print("No se puede intercambiar")
                '''
            else:
                print("Patron correcto en la posicion: "+ tmp.Ro +","+ tmp.Co)

        else:
            print("No se puede hacer cambios")
            
        tmp = tmp.siguiente2
        tmp1= tmp1.siguiente2
    pat1.lista_celda.imprimirDobleEnlaPa()
    
def Intermambio(tante,tsigue,tmp,tmp1):
        if tante!=None and (tante.color == tmp1.color) and tmp.color:
            print("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tante.Ro +","+ tante.Co)  
            tmp.color= tante.color
        elif tsigue!=None and(tsigue.color == tmp1.color) and tmp.color:
            print("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tsigue.Ro +","+ tsigue.Co)  
            tmp.color= tsigue.color
        else:
            print("No se puede intercambiar")
            
# Inicio de ejecucion
if __name__ == '__main__':
    Inicio()