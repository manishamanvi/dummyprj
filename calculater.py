def add(a,b):
    print(a-b)
   

#add(a,b)
def sub(a,b):
    print(a-b)
    
# #a=int(input("enter a"))  
# #b=int(input("enter b"))  
# #sub(a,b)print
def mul(a,b):
    print(a*b)
    
# #a=int(input("enter a"))  
# #b=int(input("enter b"))  
# #mul(a,b)
def div(a,b):
    print(a/b)

    

print("1:add")
print("2:sub")
print("3:mul")
print("4:div")
print("5:quit")
# #choice=input("enter (1/2/3/4)")
# #a=int(input("enter a"))  
# #b=int(input("enter b")) 
# #1while true:
ch=int(input("enter choice"))
a=int(input("enter a"))  
b=int(input("enter b")) 
if ch == 1:
	add(a,b)

elif ch == 2:
	sub(a,b)
elif ch == 3:
	mul(a,b)
elif ch == 4:	
    div(a,b)
elif ch == 0:
 	exit()
else:
	print("the choice is invalid")


# # add=a+b
# sub=a-b
# o='sai'
# while(o !="n"):
#     o= input("want to enter new item into dictionary: add/sub ")
#     if o='add'
#    def function_that_prints():
#     print "I printed"

# def function_that_returns():
#     return "I returned"

# f1 = function_that_prints()
# f2 = function_that_returns()
# print "Now let us see what the values of f1 and f2 are"
# print f1
# print f2


# a=[2,3,4,5,6,7,8]
# if a%2!=0:
# 	print(a)

