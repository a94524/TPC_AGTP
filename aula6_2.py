import csv
import matplotlib.pyplot as plt

def leObras(filename):
    file=open(filename,encoding="UTF8")
    file.readline()
    csv_file=csv.reader(file,delimiter=";")

    lista=[]
    for obra in csv_file:
        lista.append(tuple(obra))
    return lista

def tamanhoObras(obras):
    return len(obras)

def chaveOrd(a):
    return a[0]


def imprime(obras):
    for nome,desc,ano,_,comp,*_ in obras:
        print(f" | {nome[:20]:20} | {desc[:25]:25} | {ano[:8]:8} | {comp[:15]:15}")

def ordem(tuplo):
    return tuplo[0]

def imprime1(obras):
    lista=[]
    for nome,_,ano,_,_,*_ in obras:
        lista.append((nome,ano))
    lista.sort(key=ordem)
    return lista

def imprime2(obras):
    lista=[]
    for nome,_,ano,_,_,*_ in obras:
        lista.append((nome,ano))
    lista.sort(key=lambda tuplo:tuplo[1]) #ordena por ano
    return lista

def titporAno(obras):
    dici = {}
    for nome,_,ano,*_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else:
            dici[ano]=[nome]
    return dici

def titporPeriodo(obras):
    dici={}
    for nome,_,_,periodo,*_ in obras:
        if periodo in dici.keys():
            dici[periodo]= dici[periodo]+1
        else:
            dici[periodo]=1
    return dici

def titporComp(obras):
    lista=[]
    for _,_,_,_,comp,*_ in obras:
        lista.append(comp)
    lista.sort(key=ordem)
    return lista


def titporAnod(obras):
    dici={}
    for nome,_,ano,_,*_ in obras:
        if ano in dici.keys():
            dici[ano]= dici[ano]+1
        else:
            dici[ano]=1
    return dici

def titporComp1(obras):
    dici={}
    for _,_,_,_,comp,*_ in obras:
        if comp in dici.keys():
            dici[comp]= dici[comp]+1
        else:
            dici[comp]=1
    return dici


def plotDistrib(d):
    a=titporPeriodo(d)
    tuplo=a.items()
    x=[]
    y=[]
    for elem in tuplo:
        x.append(elem[0])
    for elem in tuplo:
        y.append(elem[1])
    plt.bar(x,y,color=['green','black'])
    barWidth=0.25
    plt.show()

    
def calcLista(obras):
    compositor=[]
    for nome,_,_,_,comp,*_  in obras:
        for i in comp:
            if i not in comp:
                comp.append(i)
    return comp

def calcListaTitulos(obras, i):
    titulo=[]
    for nome,_,_,_,comp,*_  in obras:
        a=[nome,_,_,_,comp]
        if i in comp:
            titulo.append(nome)
    return titulo

def indComp(obras):
    indiceCompositores=[]
    listaComp = calcLista(obras)
    for i in listaComp:
        indiceCompositores.append({
            "compositor": listaComp,
            "obra":calcListaTitulos(obras, i)
        })
    return indiceCompositores


            