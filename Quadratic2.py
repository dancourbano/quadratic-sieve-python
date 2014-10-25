import math

from gausiano import rref
#import gaussiana
#def hallarV(vi):
    #for a in vi:
        #for e in a:
def maximo(a,b):
    if a>b:
        return a,b
    else:
        return b,a

def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)


def tam(A):
    B=[]
    for i in A:
        B=i
        #print 'lista',B
    return len(A),len(B)

def evaluarMatriz(A):
    for i in range(len(A)):
        if i!=0:
            return False
    return True

def creandoMatriz(n,i):
    A=[]
    for i in range(n):
        A.append(i)
    return A

def compare(a,b):
    d = [x for x in a if x not in b]
    return d


def buscando(a,B):
    cont=0
    for e in B:
        if a==e:
            cont=cont+1

    return 1 if cont>0 else 0


def factorizando(a,B):
    i=2
    cont=0
    while a>1:
        if a%i==0:

            cont=cont+1
            if a/i==1:
                c=a
                if buscando(c,B)==0:
                    #print 'no factorizado'
                    return False
            a=a/i
        else:
            i=i+1
            cont=0
    #print c

    #print 'factorizado'
    return True


def descomponiendo(a,B):

    cont=0
    A=[]

    val=0
    val2=0
    #print 'soy a',a
    i=B[val]
    #A=llenando(a)
    if a==0:
        return 0
    if a==1:
        return 1
    while True:
        #print 'soy',a

        if a<0:
            #print 'negativo'
            A.append(1)
            val2=val2+1


            a=a*(-1)
        else:
            if val2==0:
                A.append(0)
                val2=val2+1


        if a%i==0:

            cont=cont+1
            a=a/i

        else:
            #print 'push',i


            A.append(cont%2)
            #print 'contador',cont



            cont=0
            if val==len(B)-1:
                break
            val=val+1
            i=B[val]

    return A





def expo2(a):
    cont=0
    while(a%2==0):
        a=a/2
        cont=cont+1
    return cont

def jacobi(a,n):
    if a==0:
        return 0
    if a==1:
        return 1

    e=expo2(a)
    #print 'e',e
    a1=a/(2**int(e))
    s=1
    if e%2==0:
        s=1
    else:
        if (n-1)%8==0 or (n-7)%8==0:
            s=1
        else:
            if (n-3)%8==0 or (n-5)%8==0:
                s=-1

    if (n-3)%4==0 and (a1-3)%4==0:
        s=(-1)*s

    n1=n%a1
    if a1==1:
        return s
    else:
        return s*jacobi(n1,a1)

def hallandoX(V,X):
    pro=1

    for i in range(len(V)):
        if V[i]==1:
            pro=V[i]*X[i]*pro
    return pro

def hallandoY(V,X,n):
    pro=1
    prod=1
    for i in range(len(V)):
        if V[i]==1:
            pro=V[i]*X[i]
            prod=((pro**2)-n)*prod
    return math.sqrt(prod)

def eye(n):
    A=[]

    for i in range(n):
        B=[]
        for j in range(n):
            if i==j:
                B.append(1)
            else:
                B.append(0)
        A.append(B)
    return A


#def aumentada(A,I):
    #a=np.array((A))
    #i=np.array((I))
    #V=np.concatenate((a, i), axis=1)
    #print V
    #fil,col=tam(V)
    #for i in range(fil):
        #V_i=[]
        #for  j in range(col):
            #V_i.append(col)

def unir(M,A):
       c=[]
       for i in range(len(A)):
           c.append(M[i]+A[i])
       return c


def primo(a):
    i=2
    cont=0
    while a>=i:
        if a%i==0:
           cont=cont+1
        i=i+1
    return 1 if cont==1 else 0
def identi(V,col):
    A=[]
    for i in range(len(V)):
        if i>=col:
            A.append((V[i])%2)
    print A
    return A

def sol(M,col1):
    fil,col=tam(M)
    #print 'fil',fil,col
    cont=0
    #print 'col1',col1
    Sol=[]
    for i in range(fil):
        for j in range(col):
            if j<col1:
                if M[i][j]==0:
                    cont=cont+1

            else:
                #print 'contador',cont
                if cont==col1:
                    print 'vector',M[i]
                    Sol.append(identi(M[i],col1))
                cont=0
               # print 'nada'
    return Sol

def main():
    n=input('>')
    M=[]
    T=[]
    contador=0

    for i in range(10):
        if primo(i):
            if jacobi(n,i)==1:
                #print 'primo 1:',i
                M.append(i)

    #prin
    k=len(M)

    m=int(math.sqrt(n))
    for x in range(m-10,m+10):
        valor=(x**2)-n
        if valor!=0:

            if factorizando(abs(valor),M)==True and contador<k+1:
                T.append(x)
                #print 'conta',contador
                contador=contador+1
    print T
    vi=[]

    for x1 in T:
        valor=(x1**2)-n
        vi.append(descomponiendo(valor,M))

    print vi
    I=[]
    V=[]
    fil,col=tam(vi)
    I=eye(fil)
    V=unir(vi,I)
    Vector=rref(V)
    #print Vector
    Vector=sol(Vector,col)
    for A in Vector:
        print A
        x=hallandoX(A,T)
        y=hallandoY(A,T,n)
        if mcd(x-y,n)!=1 and mcd(x+y,n)!=1:
            print 'solucion',mcd(x-y,n),mcd(x+y,n)

    print 'no sale'









while True:

    main()
#print primo(39)
#print factorizando(480,[2,3,5])