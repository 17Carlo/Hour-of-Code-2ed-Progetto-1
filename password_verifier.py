import re

while True:
    pw = input("Dimmi la password da testare: ")
    valida = True
    
    
    
    

    # La password deve essere lunga almeno 8 caratteri
    
    if len(pw) < 8:
        print("La password deve essere lunga almeno 8 caratteri")
        valida = False
    
    # La password deve contenere almeno un carattere maiuscolo
    if not re.search("[A-Z]+", pw):
        print("La password deve contenere almeno un carattere maiuscolo")
        valida = False
    
    # La password deve contenere almeno un carattere minuscolo
    if not re.search("[a-z]+", pw):
        print("La password deve contenere almeno un carattere minuscolo")
        valida = False
    
    # La password deve contenere almeno un numero
    if not re.search("[0-9]+", pw):
        print("La password deve contenere almeno un numero")
        valida = False
    
    # La password deve contenere almeno un carattere speciale: .,_-
    if not re.search("[\,._-]+", pw):
        print("La password deve contenere almeno un carattere speciale: .,_-")
        valida = False
    
    if valida:
        print("La password è: ")
        break
    else:
        continue
    
print("Chiudo il programma.")