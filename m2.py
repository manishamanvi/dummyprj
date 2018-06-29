a=[]
a1=[]
a2=[]
a3=[]
a1.append(1)
a1.append(2)
a1.append(3)
a.append(a1)
a2.append(3)
a2.append(3)
a2.append(4)
a.append(a2)
a3.append(2)
a3.append(2)
a3.append(2)
a.append(a3)

#a = [[1,2,3],[3,3,4],[2,2,2]]
b = [[5,6,2],[7,8,2],[2,2,2]]
c = [[3,2,2],[2,2,1],[2,2,2]]
result = [[0,0,0],[0,0,0],[0,0,0]]	
for i in range(len(a)):
    for j in range(len(b)):
    	result[i][j]=a[i][j]+b[i][j]+c[i][j]
for r in result:
    print(r)	
