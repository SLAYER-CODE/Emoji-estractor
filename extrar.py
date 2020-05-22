#!\usr\bin\bash
import os
import sys
from tqdm import tqdm,trange

#mi_archivo=open(sys.argv[1],"wr")
def write(archivo,dato):
    print("Los inconos estan en :"+archivo)
    folder = open(archivo,"a")
    folder.write(dato)
    folder.close()

def empaquetar(arch,method,dato):
    if(method=="residuos.txt"):
        write(arch+"/"+method,dato)
    else:
        if(os.path.isdir(arch)):
            write(arch+"/"+method,dato)
        else:
            os.system("mkdir "+str(arch))
def name(nombre):
    rem=nombre.split(".")
    part = len(rem)
    if(part==1):
        if(os.path.isfile(nombre)):
            return nombre+"_icon"
        else:
            return nombre
    else:
        nombre = rem[0]
        return name(nombre)
def comprobar(methodo,nombre):
    if(os.path.isfile(nombre+"/"+methodo) or os.path.isfile(methodo)):
        print("SOBRESCRIBIR?"+methodo+"[Y/N]")
        res = str(input(">>"))
        if(res.upper() == "N"):
            return False
        elif(res.upper() == "Y"):
            return True
        else:
            comprobar(methodo,nombre)
    else:
        return True
def primero(text,nombre):
    salto = 0
    nombre = name(str(nombre))
    if(comprobar("primero",nombre)):
        barra1=tqdm(text)
        for i in barra1:
            barra1.set_description("Progres %s" % i)
            if r"\u" in repr(i):
                if (not(i=='\ue601' or i== '\ue6cd')):
                    empaquetar(nombre,"primero",i)
                    salto += 1
                    if(salto == 30):
                        empaquetar(nombre,"primero","\n")
                else:
                    empaquetar(nombre,"residuos.txt",i)
    else:
        pass

def segundo(text,nombre):
    if(comprobar(nombre,nombre)):
        array="1234567890qwertyuiopasdfghjklñzxcvbnm"
        dato=len(array)
        print("LOS SIGUIENTES CARACTERES SE OMITIRAN:")
        print(array)
        for a in text:
            if(a not in array):
                array+=a
        final=array[dato:]
        nombre=name(nombre)
        write(nombre,final)
    else:
        print("bye")
        exit()

    
def main(argv=sys.argv):
    try:
        if(len(argv)==1):
            print("Especifique su archivo ")
            print(f"python {__name__} archivo.txt")
            exit()
            
        print("Tu archivo es :"+argv[1])
        if(input("[Y/N]: >> ").upper() == 'Y'):
            archivo=open(str(argv[1]),"r")
            if(argv[2]=='-d'):
                print("Funcion de Not REPET")
                texto=archivo.read()
                segundo(texto,"No-Repet")
            else:
                texto=archivo.read()
                primero(texto,argv[1])
                archivo.close()
        else:
            exit()
    except KeyboardInterrupt:
        print('Se recolecto lo suficiente')
    except IOError as e:
        print('EL ARCHIVO NO EXISTE')

    exit()
if(__name__ == "__main__"):
    print("SACANDO INFO")
    sys.exit(main())
else:
    pass
