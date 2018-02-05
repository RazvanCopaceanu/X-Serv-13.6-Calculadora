#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
	sys.exit("python3 calculadora.py funcion operando1 operando2")
_, funcion, operando1, operando2 = sys.argv

if funcion == 'resta':
	print(int(operando1) - int(operando2))
elif funcion == 'suma':
	print(int(operando1) + int(operando2))
elif funcion == 'multiplicacion':
	print(int(operando1) * int(operando2))
elif funcion == 'division':
    try:
		print(int(operando1) / int(operando2))
	except ZeroDivisionError:
		sys.exit("No se puede dividir entre 0")
 
