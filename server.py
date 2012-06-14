# -*- coding: utf-8 -*-
from proto import proto
from pynetez.Session import Session
from pynetez.Server  import Server
from GameMaster import GameMaster
        
class SessionOnServer(Session):

     def do_logIn(self, nom):
         cpt=0
         if (cpt!=4):
             GameMaster.newJoueur(cpt, nom)
             cpt+=1
             self.send.logIn_OK()
             self.send.bonjour(nom)
         else:
             self.send.logIn_Refused()
             
     def do_pose(self, carte):
          carte1=Carte(carte[0],carte[1])
          GameMaster.poserCarte(carte1)

server = Server(proto, SessionOnServer)
server.run_argv()


