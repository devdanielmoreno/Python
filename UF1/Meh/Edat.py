# Lleis de Morgan
# not ( a and b ) = not a or not b
# not ( a or b )  = not a and not b

nEdat = int(input("Edat (pots passar en edat laboral): "))
if not (nEdat >= 16) or not(nEdat <= 65): # if not (nEdat >= 16 and nEdat <= 65):
   print("No pots passar")
else:
   print("Pots passar")