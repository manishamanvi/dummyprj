# Measure some strings:
#words = ['cat', 'window', 'defenestrate']
#for w in words:
#	print(w, len(w))
#for w in words[ : ]:  # Loop over a slice copy of the entire list.
 #   if len(w) > 6:
  #      words.insert(0, w)
#print(w)
#print(words)

   #range function
#for i in range(4):
#	print(i)

#a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
#     print(i, a[i])

#a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
 #  print(i, a[i])
#print(tuple(range(5)))
#for n in range(2, 10):
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')