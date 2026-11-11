def somma(a, b):
	return a + b

def dividi (a,b):
	if b == 0:
		print("Errore: impossibilie dividere per 0.")
		return None
	return a / b

if __name__== "__main__":
	print("  Calcolatore Base ")
	print(f"Somma 5 + 3 = {somma(5, 3)}")
	print(f"Divisione 10 / 2 = {dividi(10, 2)}")