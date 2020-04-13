#pendu
from random import randrange, choice #pour le chiffre au hazard
import unicodedata #to be able to handle accented characters well
import string #to recognize letters

def jouons():
    
    banque_mots = {}
    
    def charger_fichier(nom_ficher, category):
        liste_mots = [line.rstrip('\n') for line in open(nom_ficher, 'r', encoding='utf8')]
        dictio = dict.fromkeys(liste_mots, category)
        banque_mots.update(dictio)
    
  
    rejouer = "o"
    while rejouer == "o":
        print("bienvenue au jeu du bonhomme pendu")
        
        charger_fichier('animaux.txt', 'noms d\'animaux')
        charger_fichier('expressions.txt','expressions françaises')
        charger_fichier('nourriture.txt','la nourriture')

        expression_hazard, category = choice(list(banque_mots.items()))
        print("\n*** votre catégorie: %s ***\n" % category)
        
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
            if len(set(lettres_devinees) - lettres_uniques) > 0:
                print("\nlettres erronées: %s\n" % (" ".join(set(lettres_devinees) - lettres_uniques)))
            #debug
            #print("\nlettres devinées: %s\n" % (" ".join(lettres_devinees)))

        #set of unique letters in expression
        #combines all forms of accented letters, forcing lower case, and removing the spaces
        lettres_uniques = set(unicodedata.normalize('NFKD', expression_hazard).encode('ASCII', 'ignore').decode().lower()) - {' '}

        afficher_probleme()
        #fewer incorrect letters than number of lives
        while len(set(lettres_devinees) - lettres_uniques) < nombre_vies and \
                len(lettres_uniques - lettres_devinees) > 0: #some letters yet to be discovered

            print("il vous reste %s vies" % (nombre_vies - len(set(lettres_devinees) - lettres_uniques)))

            lettre = input("entrez une lettre: ")
            lettrenormale = unicodedata.normalize('NFKD', lettre).encode('ASCII', 'ignore').decode().lower()
            if len(lettrenormale) > 1:
                print("vous ne devez entrer qu'une seule lettre") 
            elif lettrenormale in lettres_devinees:
                print("vous avez déjà essayé la lettre "+lettre)
            elif lettrenormale not in string.ascii_letters:
                print("vous devez entrer un lettre valide")      
            else:
                lettres_devinees.add(lettrenormale)
                afficher_probleme()

        if len(lettres_uniques - lettres_devinees) == 0:
            print("\n*** bravo, vous avez trouvé la réponse! ***")
        else:
            print("\n*** désolé, vous avez perdu ***")
            print("la réponse était: %s" % expression_hazard)

        rejouer = input("voulez-vous rejouer? (o/n)")
