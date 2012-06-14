# -*- coding: utf-8 -*-
from proto import proto
from pynetez.Session import Session
from pynetez.Server  import Server
from GameMaster import GameMaster
        
class SessionOnServer(Session):

     def do_logIn(self, nom):
          if (not GameMaster.QuatreJoueurs()):
               GameMaster.newJoueur(self,nom)
               self.send.logIn_OK()
          else:
               self.send.logIn_Refused()
               
     def do_pose(self, carte, nb):
          carte1=Carte(carte[0],carte[1])
          if GameMaster.poserCarte(carte1,nb):
               pass
          
server = Server(proto, SessionOnServer)
server.run_argv()


