import random

print("Sade tesadufilik modulu ")

list = [20,40,80,100,120]
print ("3 tesadufu ededi massivden sechek",random.sample(list,k=3))

list = [20,40,60,90,210]
print ("Diger massivden 7 tesadufi ededi sechek",random.sample(list,k=2))
