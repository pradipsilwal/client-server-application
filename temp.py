def temp():
	a = [["Dog", 12], ["apple", 4], ["Cat", 15], ["dog", 5], ["ball", 1], ["Apple", 34]]
	print(a)
	for animals in a:
		if (animals[0] == "Cat"):
			a.remove(animals)

	print(a)

temp()