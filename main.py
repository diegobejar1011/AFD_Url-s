from automata import Automata
from validator_txt import ValidatorTxt
from leer_afd_txt import leer_automata_de_txt


data = leer_automata_de_txt('automata.txt')
print(data)

# Crear instancia de ValidatorTxt con los datos leídos
validator = ValidatorTxt(data)

# Llamar al método validar_existencia_alfabeto() desde la instancia creada
if validator.validar_existencia_alfabeto():
    automata = Automata(data)
    while True:
        cadena = input()
        if automata.validar_cadena(cadena):
            print("Cadena válida")
        else:
            print("Cadena inválida")
        automata.restaurar_automata()
