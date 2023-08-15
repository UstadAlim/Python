import random

random.seed()

say=0

for i in range(1,11):
    z1=int(random.random()*6+1)
    z2=int(random.random()*6+1)
    if z1==3 and z2==3:
        print("3 qosha dushdu ve dovr bitdi")
        break
    elif z1==z2:
            say+=1
    print("{0}  {1}:{2} ".format(i,z1,z2))

print("10 atishda {0} sayda qosha dushdu".format(say))