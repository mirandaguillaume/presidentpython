# -*- coding: utf-8 -*-
from proto import proto
from pynetez.Session import Session
from pynetez.Client  import Client

class SessionOnClient(Session):

    def do_bonjour(self,nom):
        print "Bienvenue",nom

    def do_demande(self,nom,nb):
        n=input("{0}, quelle carte voulez-vous poser ?".format(nom))
        self.send.pose(n-1,nb)

    def do_err1(self):
        print "Le carte demandée n'est pas dans votre main."

    def do_err2(self):
        print "Vous ne pouvez pas jouer cette carte."

    def do_seeInfo(self, carte):
        print "Derniere carte posée: {0} de {1}".format(carte[0],carte[1]) 

    def do_won_manche(self,place):
        pass
                
    def do_lost_manche(self,place):
        pass

    def do_wait(self, nom):
        print "En attente de ",nom
    
    def on_start(self):
        self.send.logIn(self.choisirNom())

    def do_logIn_Refused(self):
        print "Désolé mais il y a déjà quatre joueurs en jeu"
        self.finish()

    def choisirNom(self):
        nom = raw_input("Entrez votre pseudo : ")
        return nom

    def endClient(self):
        a.on_end()
        self.finish()

    def do_logIn_OK(self):
        print "Connexion réussie"

    def endClient(self):
        self.finish()

    def do_affiche(self,texte):
        print texte

client = Client(proto, SessionOnClient)
client.run_argv()
