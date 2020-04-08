#pendu
from random import randrange #pour le chiffre au hazard
import unicodedata #to be able to handle accented characters well
import string #to recognize letters

print("bienvenue au jeu du bonhomme pendu")
fichiertexte = '/home/jovyan/work/expressions.txt'
#fichiertexte = 'D:\\Dropbox\\filez\\annabel\\pendu\\animaux.txt'
liste_expressions = [line.rstrip('\n') for line in open(fichiertexte, 'r', encoding='utf8')]
expression_hazard = liste_expressions[randrange(len(liste_expressions))]
#expression_hazard = "tomber dans les bras de Morphée"

nombre_vies = 7
lettres_devinees = set()  #store all guessed letters in a set
stringlist = list(expression_hazard) #to iterate over each letter with a comprehension

def afficher_probleme():
    #replacing letters of a string with hyphens
    displaylist = [letter.replace(letter,"-") if \
                    #only replace letter charachters, not spaces, apostrophes
                   unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').decode() in string.ascii_letters \
                    #and only letters that have not been guesses by the user (forcing lower case for the comparison)
                   and unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').decode().lower() not in lettres_devinees \
                   else letter for letter in stringlist]
    print("\n"+"".join(displaylist))
    if len(set(lettres_devinees) - lettres_uniques) > 0: print("\nlettre erronées: "+" ".join(set(lettres_devinees) - lettres_uniques)+"\n")

#set of unique letters in expression
#combines all forms of accented letters, forcing lower case, and removing the spaces
lettres_uniques = set(unicodedata.normalize('NFKD', expression_hazard).encode('ASCII', 'ignore').decode().lower()) - {' '}

afficher_probleme()
#fewer incorrect letters than number of lives
while len(set(lettres_devinees) - lettres_uniques) < nombre_vies and \
        len(lettres_uniques - lettres_devinees) > 0: #some letters yet to be discovered
    print("il vous reste "+ str(nombre_vies - len(set(lettres_devinees) - lettres_uniques)) + " vies")

    lettre = input("entrez une lettre: ")
    if lettre not in lettres_devinees:
        lettres_devinees.add(lettre.lower())
        afficher_probleme()
    else:
        print("vous avez déjà essayé la lettre "+lettre)

if len(lettres_uniques - lettres_devinees) == 0:
    print("\nbravo, vous avez trouvé la réponse")
else:
    print("\ndésolé, vous avez perdu")
    print("la réponse était:")
    print(expression_hazard)
