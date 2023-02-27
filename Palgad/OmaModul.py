 #1
n = int(input("Mitu inimesi soovite lisada ? "))
for i in range(n):
    name = input("Sisestage nimi: ")
    s= int(input("Sisestage palk: "))
    inimesed.append(name)
    palgad.append(s)
    print(inimesed,palgad)
    
    #2
    name = input("Sisestage inimesi nimi, keda te soovite kustuda: ")
index = inimesed.index(name)
inimesed.pop(index)
palgad.pop(index)
print(inimesed,palgad)
    #5
def Sorteerimine(i:list,p:list):
    v=int(input("palk 1-kahaneb,2-kasvab ?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi 
                    abi=i[j] 
                    i[j]=i[k] 
                    i[k]=abi 
                if p[j]>p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi 
                    abi=i[j] 
                    i[j]=i[k] 
                    i[k]=abi
#6
def Vordsed_palged(i:list,p:list):
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid))
    #[1200,2500,750,750,1200]->[1200,750]
    for palk in dublikatid:
        n?p.count(palk) #1200, n=2; 750, n=2
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):
            k=p.inddex(palk,k+1)
            nimi=i[k]
            print(nimi)