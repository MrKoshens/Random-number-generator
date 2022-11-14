import math
from matplotlib import pyplot as plt

p =float(input("Enter a number: "))
q = float(input("Enter another number: "))
u = float(19283)
v = float(82634)
m = float(pow(2,32))

#maths

x = []
for i in range(1, 10000):
    p = ((v*math.pi*p) + 1) % m
    x.append(p)
q=0
y = []
for j in range(1,10000):
    q=q+1
    y.append(q)


#graph

plt.scatter(x, y, label= "dots", color= "green", 
            marker= ".", s=1)
  
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My rng plot!')
plt.legend()
plt.show()
