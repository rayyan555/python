d = dict()
for x in range(1,10):
    s = set()
    for i in range(1,x+1):
        if x%i == 0:
            s.add(i)
    d[x] = s
print("Factors: ",d)
 
