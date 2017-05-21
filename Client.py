# -*- coding: utf-8 -*-


import socket
import time
import sys
from IA import *


class Client:
    """Classe définissant un simple client TCP, destiné à se connecter au serveur de jeu.
    
    On y retrouve des fonctions permettant de :
    - envoyer des données sur le socket (connexion_serveur)
    - reçevoir des données sur le socket (connexion_serveur)
    - demander la fermeture du socket"""

    def __init__(self, adresse, port, equipe):
        """Le client n'a qu'un attribut : un socket, que l'on initialise et que l'on connecte.
        On envoie ensuite le nom de l'équipe, qui est le premier message demandé par le serveur."""
        self.connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_serveur.connect((adresse, port))
        self.envoyer(equipe)

    def recevoir(self):
        """Retourne les données envoyées par le serveur."""
        reponse = self.connexion_serveur.recv(1024)

        # Permet de couper le "b'" qui précède la chaîne,
        # ainsi que le "\n" final.
        return repr(reponse)[2: len(reponse) + 1]

    def envoyer(self, chaine):
        """Envoie sur le socket la chaîne de caractères passée en paramètre."""
        self.connexion_serveur.send(bytes(chaine + '\n', 'utf_8'))

    def tout_fermer(self):
        """Ferme le socket."""
        self.connexion_serveur.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage : ' + sys.argv[0] + ' <adresse> <port> <nom_équipe>')
        sys.exit(1)

    mon_client = Client(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    mon_IA = IA()

    reponse_1 = mon_client.recevoir()
    print('Réponse du serveur : ' + reponse_1)

    # Envoyer le premier coup ICI
    mon_client.envoyer('E')

    reponse_1 = mon_client.recevoir()
    print('Réponse du serveur : ' + reponse_1)

    mon_IA.set_size(reponse_1)
    mon_IA.creer_terrain(reponse_1)

    # while True:
    #     print("Réponse du serveur : " + mon_client.recevoir())
    #     mon_client.envoyer('S')
    #     time.sleep(0.2)
