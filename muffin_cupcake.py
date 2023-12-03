muffin = int(input("muffins: "))
cupcake = int(input("cupcakes: "))
buying = ""
while buying != "0":
	buying = input("buying: ")
	if buying == "muffins":
		if muffin > 0:
			muffin -= 1
		else:
			print("Out of stock")
	elif buying == "cupcakes":
		if cupcake > 0:
			cupcake -= 1
		else:
			print("Out of stock")
print ("muffins: ",muffin,"cupcakes: ",cupcake)