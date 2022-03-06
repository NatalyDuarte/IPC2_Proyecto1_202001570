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
            print("Nombre---R---C---F---S")
            pisos.imprimirSimpleEnla()
            Inicio()
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
            print("Nombre----patron")
            nome.lista_patron.imprimirSimpleEnlaPa()
            Inicio()
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
            global auxi
            global auxi1
            auxi="No"
            auxi1="No"
            Inicio1(pat,nome,elem1,elem11,auxi,auxi1)
        else:
            print("No se ha cargado el archivo")
            Inicio()
    elif opcion == 6:
        opcion = 7
        print("\n=== ¡HASTA PRONTO! ====")
    else:
        print("\n====¡OPCION NO EXISTENTE!====")

def Inicio1(pat,nome,elem1,elem11,auxi,auxi1):
    op = ""
    while True:
        print("=============== ROBOT PISOS ARTESANALES ==============")
        print("|1. Costo mínimo para realizar el cambio             |")
        print("|2. Instrucciones para hacer el cambio por consola   |")
        print("|3. Instrucciones para hacer el cambio por archivo   |")
        print("|4. Mostrar graficamente el nuevo patron             |")
        print("|5. Menu principal                                   |")
        print("======================================================")
        print("Para que cada funcion cumpla su objetivo debe seleccionar cada opcion segun su número correspondiente")
        print("Ingrese Opcion:")
        op = int(input(">. "))
        Menu1(pat,op,nome,elem1,elem11,auxi,auxi1)
        print("\n")
        if (op >= 1 and op <= 5):
            break

def Menu1(pat,op,nome,elem1,elem11,auxi,auxi1):
    if op == 1:
        Costominimo(nome,elem1, elem11)
        Inicio1(pat,nome,elem1,elem11,auxi,auxi1)
    elif op == 2:
        Buscando(pat,nome,elem1, elem11,auxi,auxi1)
        Inicio1(pat,nome,elem1,elem11,auxi,auxi1)
    elif op == 3:
        Genrartxt(pat)
        print("Generado exitosamente")
        Inicio1(pat,nome,elem1,elem11,auxi,auxi1)
    elif op == 4:
        Grafica4(nome,elem1)
        Inicio1(pat,nome,elem1,elem11,auxi,auxi1)
    elif op == 5:
        op=6
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

def Costominimo(nome, pat1, pat2):
    tmp = pat1.lista_celda.inicio2
    tmp1= pat2.lista_celda.inicio2
    contaFi=0
    contaSi=0
    conta=0
    conti=0
    while tmp is not None:
        tante=tmp.anterior2
        tsigue=tmp.siguiente2
        if (tmp.Ro == tmp1.Ro) and (tmp.Co == tmp1.Co): 
            if(tmp.color != tmp1.color):
                if(float(nome.Si)<=float(nome.Fi)):
                    Inter(tante,tsigue,tmp,tmp1,auxi,auxi1)
                    contaSi +=1
                else:
                    Vol(tante,tsigue,tmp,tmp1)
                    contaFi +=1
            else:
                conti=0
        else:
            conti=0
        tmp = tmp.siguiente2
        tmp1= tmp1.siguiente2
    conta=float(float(nome.Fi)*contaFi)+float(float(nome.Si)*contaSi)
    print("El costo minimo es de: Q."+ str(conta))

def Inter(tante,tsigue,tmp,tmp1,auxi,auxi1):
    global auxiliar
    global auxiliar1 
    auxiliar=""
    auxiliar1=""
    if tante!=None and (tante.color == tmp1.color) and tmp.color  and (tante.color!=auxi):
            auxiliar=tmp.color
            tmp.color= tante.color
            tante.color= auxiliar
            auxi=auxiliar     
    elif tsigue!=None and(tsigue.color == tmp1.color) and tmp.color and (tsigue.color!=auxi1):
            auxiliar1=tmp.color
            tmp.color= tsigue.color
            tsigue.color=auxiliar1
            auxi1=auxiliar1          
    else:
       Vol(tante,tsigue,tmp,tmp1)

def Vol(tante,tsigue,tmp,tmp1):
    if(tmp.color=="W"):
        tmp.color="B"
    elif(tmp.color=="B"):
        tmp.color="W"
    else:
        Inter(tante,tsigue,tmp,tmp1,auxi,auxi1)

def Buscando(pat,nome, pat1, pat2,auxi,auxi1):
    tmp = pat1.lista_celda.inicio2
    tmp1= pat2.lista_celda.inicio2
    global archivo
    archivo=open(str(pat)+".txt","w")
    print("Buscando cambios que se deben hacer")
    archivo.write("Buscando cambios que se deben hacer\n")
    conta=0
    while tmp is not None:
        tante=tmp.anterior2
        tsigue=tmp.siguiente2
        if (tmp.Ro == tmp1.Ro) and (tmp.Co == tmp1.Co): 
            if(tmp.color != tmp1.color):
                print("Cambiar en la posicion: "+ tmp.Ro +","+ tmp.Co +" El patron: "+ tmp.color+ " por: "+ tmp1.color)
                archivo.write("Cambiar en la posicion: "+ tmp.Ro +","+ tmp.Co +" El patron: "+ tmp.color+ " por: "+ tmp1.color+"\n")
                if(float(nome.Si)<float(nome.Fi)):
                    Intermambio(tante,tsigue,tmp,tmp1,auxi,auxi1)
                    conta +=1
                else:
                    Voltear(tante,tsigue,tmp,tmp1)
                    conta +=1
            else:
                print("Patron correcto en la posicion: "+ tmp.Ro +","+ tmp.Co)
                archivo.write("Patron correcto en la posicion: "+ tmp.Ro +","+ tmp.Co+"\n")
        else:
            print("No se puede hacer cambios")
            archivo.write("No se puede hacer cambios\n")
            
        tmp = tmp.siguiente2
        tmp1= tmp1.siguiente2
    pat1.lista_celda.imprimirDobleEnlaPa()
    
def Intermambio(tante,tsigue,tmp,tmp1,auxi,auxi1):
    global auxiliar
    global auxiliar1 
    auxiliar=""
    auxiliar1=""
    if tante!=None and (tante.color == tmp1.color) and tmp.color  and (tante.color!=auxi):
            print("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tante.Ro +","+ tante.Co)  
            archivo.write("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tante.Ro +","+ tante.Co+"\n")
            auxiliar=tmp.color
            tmp.color= tante.color
            tante.color= auxiliar
            auxi=auxiliar     
    elif tsigue!=None and(tsigue.color == tmp1.color) and tmp.color and (tsigue.color!=auxi1):
            print("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tsigue.Ro +","+ tsigue.Co)  
            archivo.write("Intercambio piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" por el piso: "+ tsigue.Ro +","+ tsigue.Co+"\n")
            auxiliar1=tmp.color
            tmp.color= tsigue.color
            tsigue.color=auxiliar1
            auxi1=auxiliar1          
    else:
       Voltear(tante,tsigue,tmp,tmp1)

def Voltear(tante,tsigue,tmp,tmp1):
    if(tmp.color=="W"):
        print("Volteo del piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" al color: B")  
        archivo.write("Volteo del piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" al color: B\n")
        tmp.color="B"
    elif(tmp.color=="B"):
        print("Volteo del piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" al color: W")  
        archivo.write("Volteo del piso en la posicion: "+ tmp.Ro +","+ tmp.Co +" al color: W\n")
        tmp.color="W"
    else:
        Intermambio(tante,tsigue,tmp,tmp1,auxi,auxi1)

def Genrartxt(pat1):
    archivo.close()
    webbrowser.open_new_tab(pat1+".txt")
            
# Inicio de ejecucion
if __name__ == '__main__':
    Inicio()