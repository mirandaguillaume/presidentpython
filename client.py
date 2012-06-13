# -*- coding: utf-8 -*-
from proto import proto
from pynetez.Session import Session
from pynetez.Client  import Client

class SessionOnClient(Session):

    def do_go(self):
        n = int(raw_input("Quelle carte voulez-vous jouer (0 pour se coucher) ? "))
        self.send.posed(self.main.liste[n].no,self.main.liste[n].couleur)

    def do_err1(self):
        print "Le carte demandée n'est pas dans votre main."

    def do_err2(self):
        print "Vous ne pouvez pas jouer cette carte."


    def do_inGame(self, carte):
        print "Derniere carte posée: {0} de {1}".format(carte[0],carte[1])  

    def do_won(self):
        print "You won!"
        self.finish()

    def do_lost(self):
        print "You lost!"
        self.finish()

    def do_abort(self):
        print "Game aborted!"
        self.finish()

    def do_pending(self):
        print "Waiting for an opponent"

    def do_connected(self):
        print "Connected to an opponent"

    def do_wait(self):
        print "Wait for your opponent's move"