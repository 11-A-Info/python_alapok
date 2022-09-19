elsoValtozo = 12

# string konkatenáció
kiir_1 = "A változó értéke: " + str(elsoValtozo)
print(kiir_1)

# formattált sztring 1.verzió
kiir_1 = "A változó értéke: {}".format(elsoValtozo)
print(kiir_1)

# formattált sztring 2.verzió
kiir_1 = f"A változó értéke: {elsoValtozo}"
print(kiir_1)

# formattált sztring 1.verzió
kiir_1 = "A változó értéke: {0}".format(elsoValtozo)
print(kiir_1)