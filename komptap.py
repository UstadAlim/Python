print("Fikrinizde 1-5 araliginda eded tutun", end = ' ')
input("ve  Enter basin")
 
a = input("Bu eded 3 den boyukdur? (he/yox) ")
 
if a == 'he':
	a = input("Bu eded 4 dur? (he/yox) ")
	if a == 'yox':
		print("Bu eded 5 dir")
else:
	a = input("Bu eded 1 dir? (he/yox) ")
	if a == 'yox':
		a = input("Bu eded 2 dir? (he/yox) ")
		if a == 'yox':
			print("Bildim, bu 3 ededidir!")
 
print("Ura men tapdim")