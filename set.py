a={1,'hi',(4,5),4+5j}
#print(a)
#print(type(a))

#print(a)
#a.update([1,2,3,4])
#print(a)


#a.add(56)#noo append
print(a)


#set comprehesion
a={i for i in range(0,10,2)}
print(a)
b={i for i in range(0,10,3)}
print(b)
#print(a+b)     can not be done
#print(a-b)
#print(b-a)
#print(a.difference(b))
#print(a.symmetric_difference(b))
#print(b.symmetric_difference(a))

#a.pop()
#print(a)
#a.pop()
#print(a)
#a.pop()
#print(a)

#a.clear()
#print(a)
#union

#print(a|b)
#print(a.union(b))

#print(a&b)
#print(a.intersection(b))


a={1,2,3,4,5,6}
b={1,2,3}
#print(a.issubset(b))
#print(b.issubset(a))
#print(a.issuperset(b))
print(len(a))
print(sum(a))
print(max(a))
print(min(a))
print(enumerate(a))
b=iter(a)
print(a)