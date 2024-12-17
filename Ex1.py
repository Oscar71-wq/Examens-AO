def llegir_llista_enters():
    l = [] 
    a = "a"
    while a!=".":
        a = input("dime un nombre: ")
        if a!=".":
            l.append(int(a))
    return l





def llegir_llista():
    l = [] 
    a = "a"
    while a!=".":
        a = input("dime un nombre: ")
        if a!=".":
            l.append(int(a))
    return l

def llista_senars(l):
    s = []
    for num in l: 
        if num % 2 == 1: 
            s.append(num) 
    return s






def llegir_llista():
    l = [] 
    a = "a"
    while a!=".":
        a = input("dime un nombre: ")
        if a!=".":
            l.append(int(a))
    return l

def llista_senars(l): 
    s = [] 
    for num in l: 
        if num % 2 == 1: 
            s.append(num) 
    return s 

def suma_parells(l): 
    suma = 0 
    for num in l: 
        if num % 2 == 0: 
            suma += num 
    return suma




def llegir_llista():
    l = [] 
    a = "a"
    while a!=".":
        a = input("dime un nombre: ")
        if a!=".":
            l.append(int(a))
    return l

def numero():
    num = input("Introdueix el número que vols cercar a la llista: ") 
    return int(num)


def cercar_numero_llista(llista, numero):
    for i in range(len(llista)):
         if llista[i] == numero: 
            return i 
    return -1




    def llegir_llista_enters():
    l = [] 
    a = ""
    while a!=".":
        a = input("dime un nombre: ")
        if a!=".":
            l.append(a)
    return l



import random 

def crear_llista_numeros_aleatoris(): 
    llista = [random.randint(1, 100) for _ in range(5)] 
    return llista
