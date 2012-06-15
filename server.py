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
               
     def do_pose(self, n, nb):
          if n!=-1:
               GameMaster.poserCarte(n,nb)
               
server = Server(proto, SessionOnServer)
server.run_argv()


