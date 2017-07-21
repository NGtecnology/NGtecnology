import math
from math import sqrt

def estendido(k):
    print "                  ALG. EUCLIDIANO ESTENDIDO\n\n\n"
    for i in range(50):
        n1 = input("Dividendo: ")
        n2 = input("Divisor: ")
        resto = n1%n2
        n3=1
        n4=0
        n5=0
        n6=1
        while resto!=0:
            print "\n------->Quociente = ", n1/n2
            res=n1/n2
            resto=n1%n2
            print "------->resto = ", resto
            x=n3-n4*res
            y=n5-n6*res
            print "------->Valor de x = ", x
            print "------->Valor de y = ", y
            n3=n4
            n4=x
            n5=n6
            n6=y
            n1=n2
            n2=resto
        print "\n************************** MDC = ",n1,"****************************\n"
    print "\n************************** FIM PROGRAMA *************************"

def diofantina(n1,n2,c):
    print "                  Diofantina\n\n\n"
    n1 = input("Digite o primeiro termo: ")
    k=n1 #guardar valor de n1
    n2 = input("Digite o segundo termo: ")
    l=n2 #guardar valor n2
    c= input("Digite o terceiro termo: ")
    resto = n1%n2
    n3=1
    n4=0
    n5=0
    n6=1
    while resto!=0:
        res=n1/n2
        resto=n1%n2
        x=n3-n4*res
        y=n5-n6*res
        n3=n4
        n4=x
        n5=n6
        n6=y
        n1=n2
        n2=resto
        mdc=n1
        print (n3)
        print (n4)
        print "--------x--------"
        print (x)
        print (y)
        print "----------------"
    if c%mdc!=0:
        print " NAO HA SOLUCAO! (0,0)\n"
    else:
        mult=c/n1
        print (mult)
        print "----------------"
        p=x*mult
        print (p)
        o=y*mult
        print (o)
        print "----------------"
        print (p,o)
        print "----------------"
        print (k)
        print (l)

def crivo(lim):
        print "                  Crivo de Eratostenes\n\n\n"
        listprimo = []
        listprimo.append(2)
        listprimo.append(3)
        listprimo.append(5)
        listprimo.append(7)
        listprimo.append(11)
        n = 2
        for n in range (lim):
            if n%2!=0 and n%3!=0 and n%5!= 0 and n%7!=0 and n%11!=0:
                listprimo.append(n)
                n=n+1
            else:
                n=n+1
        listprimo.remove(1)
        return listprimo

def fat(num):
        print "                  Ingenuo de Fatoracao\n\n\n"
        listdivisores = []
        div = 2
        while num!=1:
            if div==2 and num%div==0:
                listdivisores.append(div)
                num=num/div
                num=num
            elif div==3 and num%div==0:
                listdivisores.append(div)
                num=num/div
                num=num
            elif div==5 and num%div==0:
                listdivisores.append(div)
                num=num/div
                num=num
            elif div==7 and num%div==0:
                listdivisores.append(div)
                num=num/div
                num=num
            elif div==11 and num%div==0:
                listdivisores.append(div)
                num=num/div
                num=num                
            elif div%2!=0 and div%3!=0 and div%5!= 0 and div%7!=0 and div%11!=0 and num%div==0:
                listdivisores.append(div)
                num=num/div
                num=num
            else:
                div=div+1 
        return listdivisores

def fermat(n):
        print "                  Fermat\n\n\n"
        a=math.ceil(sqrt(n))
        b=(a**2)-n
        raiz_b=sqrt(b)
        int_b=int(raiz_b)
        if n%2==0:
            print "invalido"
        else:
            while int_b!=b:
                b=(a**2)-n
                raiz_b=sqrt(b)
                int_b=(int(raiz_b)**2)
                print a
                print b
                print "int b", int_b,
                print "raiz b", raiz_b
                a=a+1                
        return (a-1)-sqrt(b), (a-1)+sqrt(b)

def somamod(a,b,mod):
        print "                  soma modular\n\n"
        termo1=a%mod
        termo2=b%mod
        result=(termo1+termo2)%mod
        return "resultado da soma:",result

def difmod(a,b,mod):
        print "                  diferenca modular\n\n"
        termo1=a%mod
        termo2=b%mod
        if termo1>termo2:
            result=(termo1-termo2)%mod
        else:
            result=(termo2-termo1)%mod            
        return "resultado da diferenca:",result

def multmod(a,b,mod):
        print "                  multiplicacao modular\n\n"
        termo1=a%mod
        termo2=b%mod
        result=(termo1*termo2)%mod
        return "resultado da multiplicacao:",result

def potmod(a,b,mod):
        print "                  potenciacao modular\n\n"
        result=(a**b)%mod
        return "resultado da potencia:",result
    
def invmod(a,mod):
        print "                  potenciacao modular\n\n"
        i=0
        for i in range(mod):
            result1=(a*i)%mod
            if result1==1:
                print "inverso igual a: ", i
            else:
                i=i+1
