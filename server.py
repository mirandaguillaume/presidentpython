# -*- coding: utf-8 -*-
from proto import proto
from pynetez.Session import Session
from pynetez.Server  import Server
from threading import Lock
from pynetez.Agent import Agent
import os

from pynetez.Protocol import Protocol

masterproto = Protocol()
masterproto.define("play", None, None) # agent, n

class GameMaster(Agent):

    def __init__(self, players, nbJoueurs):
        super(GameMaster, self).__init__(masterproto)
        self.nbJoueurs=nbJoueurs
        self.players=players
        self.paquet()
        self.cpt=0
        self.nbManches=0
        self.DerniereCarte=range(2)
        self.DerniereCarte[0]=1
        self.DerniereCarte[1]="H"
        self.begin.connect(self.connected)

    def connected(self):
    	for i in range(self.nbJoueurs):
        	self.players[i].send.connected()
        	self.players[0].send.go()
        for i in range(self.nbJoueurs-1):
        	self.players[i].send.wait()

    def finish(self):
        super(GameMaster, self).finish()
        for i in range(self.nbJoueurs):
        	self.players[i].finish()

    def do_play(self, player,n): # Fonction qui gere la reponse du joueur et agit en consequence
        nb=self.cpt%self.nbJoueurs
        if player is not self.players[nb]:
            # out of turn: abort game
            for i in range(self.nbJoueurs):
                self.players[i].abort()
                self.finish()

        if self.players[nb].main.taille()<n:
            self.players[nb].send.err1()
            self.players[nb].send.go()
        elif n!=0:
            if self.players[nb].main.liste[n-1].no==self.DerniereCarte.no:
    	        self.DerniereCarte=self.players[nb].main.liste[n-1]
   	        elif self.main.liste[n-1]>self.DerniereCarte:
                self.DerniereCarte=self.players[nb].main.liste[n-1]
            else :
                self.players[nb].send.err2()
            	self.players[nb].send.go()  
            else :
                self.DerniereCarte=self.players[nb].main.liste[n-1]
        else:
			self.DerniereCarte= self.players[nb].main.liste[n]
            for i in range(self.nbJoueurs):
                self.players[i].send.inGame(self.left)
            if self.nbManches == 3:
                # if it's a win: end game
                self.player1.send.won()
                self.player2.send.lost()
                self.finManche()
                break;
            else:
                # else switch players
                self.players[self.cpt%self.nbJoueurs].send.wait()
                cpt+=1
                self.players[self.cpt%self.nbJoueurs].send.go()

    def finManche()
        pass
 
lock = Lock()
waiting = None


class SessionOnServer(Session):

    def __init__(self, *args, **kargs):
        super(SessionOnServer, self).__init__(*args, **kargs)
        with lock:
            global waiting
            if waiting is None:
                waiting = self
                self.startmaster = False
            else:
            	players=range(4)
                players[0] = waiting
                waiting = None
                players[1] = self
				players[2]= self
				players[3]= self
                gamemaster = GameMaster(players,4)
                for i in range(4):
                players[i].master=gamemaster    
                self.startmaster = True

    def on_start(self):
        self.send.pending()
        if self.startmaster:
            self.master.start()

    def do_take(self, n):
        self.master.recv.play(self, n)

server = Server(proto, SessionOnServer)
server.run_argv()

            