a = [[1,2,3],[3,3,4]]
b = [[5,6,2],[7,8,2]]
b = [[3,2,2],[2,2,1]]
result = [[0,0,0],[0,0,0]]	
for i in range(len(a)):
    for j in range(len(a[0])):
    	result[i][j]=a[i][j]+b[i][j]
for r in result:
    print(r)	
