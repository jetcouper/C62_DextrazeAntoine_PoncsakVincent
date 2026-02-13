from sys import argv
import re
import entrainement

def main():
    chemin = argv[1]
    encodage = argv[2]
    #methode = argv[3]

    f = open(chemin, encoding=encodage)
    texte = f.read()
    texte = re.findall(r'\w+' , texte)

    f.close()
    return 0


if __name__ == '__main__':
    quit(main())