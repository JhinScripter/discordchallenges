texto = input("Texto: ")
rot = int(input("ROT: "))

print("Esquerda: " + texto[rot:] + texto[:rot])
print("Direita: " + texto[rot+1] + texto[0:rot+1])