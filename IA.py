# -*- coding: utf-8 -*-


import time

# TODO: améliorer l'algorithme, trouver une manière de marquer le chemin à prendre
class IA:
    """Classe définissant notre intelligence artificielle."""

    def __init__(self):
        """Constructeur de notre intelligence artificielle.
        On initialise :
        - les dimensions du tableau, la position de l'IA, et la position du but, à -1
        - le terrain de jeu"""
        self.nb_lignes = self.nb_colonnes = self.posX = self.posY = self.butX = self.butY = self._num_equipe = -1
        self.terrain = []
        self.chemin_a_prendre = []
        self.cases_marquees = []

        # A ENLEVER PLUS TARD
        self.butX = 13
        self.butY = 8

    def _get_num_equipe(self):
        return self._num_equipe

    def _set_num_equipe(self, num_equipe):
        self._num_equipe = num_equipe

    def set_position(self, reponse_du_serveur):
        """Définit la position du joueur, en extrayant celle-ci de la réponse du serveur"""
        coordonnees_joueurs = reponse_du_serveur[reponse_du_serveur.rindex('/') + 3:]
        coordonnees_joueurs = coordonnees_joueurs.split(',')
        self.posX = int(coordonnees_joueurs[self._get_num_equipe()])
        self.posY = int(coordonnees_joueurs[self._get_num_equipe() + 1])

    def set_taille(self, reponse_du_serveur):
        """Définit la taille du terrain, en extrayant celle-ci de la réponse du serveur."""
        taille = reponse_du_serveur[0: reponse_du_serveur.index('/')]
        self.nb_colonnes = int(taille.split('x')[0])
        self.nb_lignes = int(taille.split('x')[1])

    def creer_terrain(self, reponse_du_serveur):
        """Créé la liste qui contient le terrain de jeu.
        Le terrain est une liste de liste, donc par exemple :
            self.terrain[2][4]
            
        permet d'accéder à la cinquième case de la troisième ligne."""
        self.terrain = []

        # On découpe la réponse du serveur en enlevant le début (informations sur les dimensions du terrain),
        # et la fin (informations sur les joueurs, et leur position).
        chaine_terrain = reponse_du_serveur[reponse_du_serveur.index('/') + 1 : reponse_du_serveur.rindex('/')]

        # le split('-') renvoie liste où chaque élément est une case du terrain
        chaine_terrain = chaine_terrain.split('-')

        # on parcourt donc cette liste, et on remplit notre terrain avec les éléments de cette liste
        i = 0
        while i < len(chaine_terrain):
            for j in range(0, self.nb_lignes):
                self.terrain.append([])
                for k in range(0, self.nb_colonnes):
                    self.terrain[j].append(chaine_terrain[i])
                    i += 1

    def trouver_chemin_a_prendre(self, posX, posY):
        # On marque la case sur laquelle on est
        self.cases_marquees.append((posX, posY))

        if posX == self.butX and posY == self.posY:
            return 'C'

        chemins_possibles = []

        # On vérifie toujours :
        # - si l'on ne sort pas du terrain
        # - si l'on est pas déjà passé par là
        # - si l'on ne va pas sur une dune

        # On vérifie si l'on peut aller au nord
        if posY - 1 >= 0 and (posX, posY - 1) not in self.cases_marquees and self.terrain[posX][posY - 1] != 'D':
            chemins_possibles.append((posX, posY - 1))

        # On vérifie si l'on peut aller à l'ouest
        if posX - 1 >= 0 and (posX - 1, posY) not in self.cases_marquees and self.terrain[posX - 1][posY] != 'D':
            chemins_possibles.append((posX - 1, posY))

        # On vérifie si l'on peut aller au sud
        if posY + 1 >= 0 and (posX, posY + 1) not in self.cases_marquees and self.terrain[posX][posY + 1] != 'D':
            chemins_possibles.append((posX, posY + 1))

        # On vérifie si l'on peut aller à l'est
        if posX + 1 >= 0 and (posX + 1, posY) not in self.cases_marquees and self.terrain[posX + 1][posY] != 'D':
            chemins_possibles.append((posX + 1, posY))

        print(chemins_possibles)

        time.sleep(1)

        for direction in chemins_possibles:
            print('direction = ' + repr(direction))
            self.trouver_chemin_a_prendre(direction[0], direction[1])

    num_equipe = property(_get_num_equipe, _set_num_equipe)