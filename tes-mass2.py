import random

qiymet_sozluk = {
  "Akif": 55,
  "Murad": 70,
  "Nadir": 60,
  "Zaur" :50
}
print ("Sozlukden iki neferi tesadufen sechek ",random.sample(qiymet_sozluk.items(), k=2))