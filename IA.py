# -*- coding: utf-8 -*-


class IA:
    """Classe définissant notre intelligence artificielle."""

    def __init__(self):
        """Constructeur de notre intelligence artificielle.
        On initialise :
        - la dimension du tableau à zéro (qui sera amenée à être modifiée par set_size)
        - le terrain de jeu"""
        self.nb_lignes = 0
        self.nb_colonnes = 0

    def set_size(self, reponse_du_serveur):
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