#Petite application de jeu de roulette

#On importe randrange qui permet de generer un nombre aléatoire
from random import randrange

#On definit l'argent de départ
Argent = 2500


print("Bienvenue au Zcasino! \nIci vous pouvez jouer au jeu de la roulette. \n   Vous commencez cette partie avec", Argent, "$")
Name = input("Quel est votre nom ?")

#Tant que Argent n'est pas à 0 l'action s'èxécute
while Argent > 0:
    somme_mise = input("Choisissez votre mise :")

    somme_mise = int(somme_mise)
    while somme_mise > Argent:
        print("Vous n'avez pas assez d'argent.")
        mise2 = input("Choisissez votre mise:")
        mise2 = int(mise2)
        somme_mise = mise2

    print("\n", Name, " mise", somme_mise, "$")

    Argent = Argent - somme_mise
    print("Il vous reste", Argent, "$")

    Choix = input("\n Choisissez un numero entre 0 et 49.")
    Choix = int(Choix)
    while Choix > 49 or Choix < 0:
        print("Vous n'avais pas choisi un chiffre valide")
        Choix2 = input("Choisissez un numero entre 0 et 49.")
        Choix = Choix2
        Choix = int(Choix)
        #On laisse le joueur choisir le montant de sa mise et le numero sur le quelle il mise

    Resultat = randrange(50)
    Resultat = int(Resultat)
    print(Resultat)
    #On donne le résultat

    if Choix == Resultat:
        print("Vous avez gagner! \n Vous gagner le double de votre mise.")
        Argent = Argent + somme_mise * 2
        Argent = int(Argent)
        print("Vous avez maintentant", Argent, "$")

    else:
        print("Ce n'etait pas le bon numero.")
        print("Il vous reste", Argent, "$")
        #On compare

print("Vous n'avez plus d'argent.")
