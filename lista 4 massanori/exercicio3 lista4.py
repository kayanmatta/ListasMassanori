import random 
l1 = list()
l2 = list()
l3 = list()
for contador in range (1,21):
    x= random.randint (1,100)
    if contador > 10:
        l2.append (x)
    else:
        l1.append (x)

for contador in range (0,10):
    l3.append (l1[contador])
    l3.append (l2[contador])

print (l1)
print (l2)
print (l3)
