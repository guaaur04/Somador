# calcule e imprima a média aritmética

w, x, y, z = input("Entre quatro numeros para encontrar a media (espacos sem virgulas): ").split()

w, x, y, z = [int(w), int(x), int(y), int(z)]

total = w + x + y + z 

media = total / 4

print("A media de", w, x, y, z, "e", media )