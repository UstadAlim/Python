massivim=[23,5,6,7,9,67,34,12,90,45,43]
t=0


x=int(input('Axtarilan ededi daxil edin: '))

for p in massivim:
    if x==p:
        t+=1
if t>0:
    print('Eded massivde var')
else:
    print('Eded massivde yoxdur')
