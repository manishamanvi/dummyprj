def add(a,b):
    return a+b
    
#a=int(input("enter a"))  
#b=int(input("enter b"))

#add(a,b)
def sub(a,b):
    return a-b 
    
#a=int(input("enter a"))  
#b=int(input("enter b"))  
#sub(a,b)print
def mul(a,b):
    return a*b
    
#a=int(input("enter a"))  
#b=int(input("enter b"))  
#mul(a,b)
def div(a,b):
    return a/b
    
#a=int(input("enter a"))  
#b=int(input("enter b"))  
#div(a,b)
print("1:add")
print("2:sub")
print("3:mul")
print("4:div")
print("5:quit")

#ch=int(input("enter choice"))

#print("1:add")
#print("2:sub")
#print("3:mul")
#print("4:div")
#print("5:quit")
#choice=input("enter (1/2/3/4)")
#a=int(input("enter a"))  
#b=int(input("enter b")) 
while true:
	ch=int(input("enter choice"))
a=int(input("enter a"))  
b=int(input("enter b")) 
if ch == 1:
	print(add(a,b))
elif ch == 2:
	print(sub(a,b))
elif ch == 3:
	print(mul(a,b))
elif ch == 4:	
	print(div(a,b))
elif ch == 0:
	exit()
else:
	print("the choice is invalid")