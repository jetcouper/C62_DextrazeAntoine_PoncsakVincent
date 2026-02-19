from sys import argv

from entrainement import Entrainement

def main():
    chemin = argv[1]
    encodage = argv[2]
    #fenetre = argv[3]
    fenetre = 5
    entrainementText = Entrainement(chemin,encodage,fenetre)


    return 0


if __name__ == '__main__':
    quit(main())