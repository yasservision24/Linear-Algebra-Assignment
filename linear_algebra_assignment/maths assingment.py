import json
with open("input.txt") as file:
    file1=file.read()
    dic=json.loads(file1)
matrix=[]
X=[]
X1=[]
B=[]
m=dic["rows"]
n=dic["columns"]
for i in range(1,n+1):
    V="x"+str(i)
    X.append(V)
    X1.append(V)
for i in range(m):
    B.append(0)
n+n+1
list=dic["values"]
list1=list.copy()
len1=len(list)
for i in range(m):
    i=[]
    for j in range(n):
        i.append(list[0])
        list.pop(0)
    matrix.append(i)
print("given matrix is:")
for i in range(m):
    print(matrix[i])
print()
L=[]
K=0
for i in range(m):
    LIST=[]  
    for j in range(n):
        LIST.append(list1[K])
        K=K+1
    LIST.append(0)
    L.append(LIST)                 
# program to convert to reduced row echleon form   
cn=0
n=n+1
for i in range(m):
    if cn>=n:
        L=L
        break
    j=i
    if L[j][cn]==0:
        j=j+1
        if j==m:
            j=i
            cn=cn+1
            if n==cn:
                L=L
            break
    L[j],L[i]=L[i],L[j]
    value=L[i][cn]
    value=float(value)
    for a in range(len(L[i])):
        b=L[i][a]/value
        L[i][a]=b  
    for t in range(m):
        if t!=i:
            value1=L[t][cn]
            L[t]=[x-value1*y for x,y in zip(L[t],L[i])]
    cn=cn+1

cn=0
n=n
for i in range(m):
    if cn>=n:
        matrix=matrix
        break
    j=i
    if matrix[j][cn]==0:
        j=j+1
        if j==m:
            j=i
            cn=cn+1
            if n==cn:
                matrix=matrix
            break
    matrix[j],matrix[i]=matrix[i],matrix[j]
    value=matrix[i][cn]
    value=float(value)
    for a in range(len(matrix[i])):
        b=matrix[i][a]/value
        matrix[i][a]=b  
    for t in range(m):
        if t!=i:
            value1=matrix[t][cn]
            matrix[t]=[x-value1*y for x,y in zip(matrix[t],matrix[i])]
    cn=cn+1

print("Matrix in augmented row echleon form")
for i in L :
    for j in range(len(i)):
        if i[j]==0:
            i[j]=float(0)
for i in L:
    print(i)
print()

I1=[] 
for i in L:
    
    T=[index for index,item in enumerate(i) if item!=0]  
    if len(T)==1:
        T1=i[T[0]]
        X1[T[0]]=-T1
        I1.append(T1)
Z5=[]
if m==n-1:
    Z=[]
    
    for i in range(len(L)):
        j=i
        if L[i][j]!=0:
            Z.append(1)
        else:
            Z.append(0)
    if Z.count(1)==n-1:
        print("for the given matrix,zero is the ony sol that is trivial solution, values of x are:")
        for i in X:
            print(i,"=",0)
        

    else:
        z1=[index for index,item in enumerate(Z) if item==0] 
        z2=[index for index,item in enumerate(Z) if item==1]
        Z5=z1.copy()
        Z2=z2.copy()
     

        for i in z1:
            print("free var",X[i])
        for i in z2:
            print("basic var",X[i])
        import numpy as np
        A = np.array(matrix)
        b = np.array(B)
        x = np.linalg.solve(A, b)
        print(x)
else:
    Z2=[]
    g=0
    for i in (L):
        for j in range(g,len(i)-1):
            if i[j]!=0:
                Z2.append(j)
                g=j+1
                break
    z3=[X[i]for i in Z2]
    print("basic varibles are",z3)
    z4=[X[i] for i in range(n-1) if i not in Z2]
    Z5=[i for i in range(n-1) if i not in Z2]
    print("free variables are ",z4)
    j=0
    print()
    for i in range(len(L)):
        print(X[j],"=",end="")
        for k in range(len(X)):
            if matrix[i][k]==0:
                    pass
                   
            else:
                if k!=n-2:
                  print("[",str(matrix[i][k])+" "+str(X[k]),"]",end=" + ")
                else:
                    print("[",str(-matrix[i][k])+" "+str(X[k]),"]",end="")
        print()
        j=j+1
    print()
for i in range(n-1) :
    if str(X[i]).isdigit()==True:
        print(X[i],"=",X1[i])
                           



        
      
    
    
    
        
                 
        
            
            
        
        
        

            
                                
                    
            
    
      