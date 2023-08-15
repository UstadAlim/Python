import random
import math

random.seed()
k=random.random()
print(k)


random.seed(20)
m=math.floor(random.random()*10)
print(m)

for i in range(20):
    p=math.floor(random.random()*20+1)
    print(p)

print('------- Musbet araliq ------------')
random.seed()
f=random.randint(0,50)
print(f)

print('--------Menfi araliq --------')
random.seed()
f1=random.randint(-50,2)
print(f1)