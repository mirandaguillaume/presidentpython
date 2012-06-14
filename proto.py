# -*- coding: utf-8 -*-
from pynetez.Protocol import Protocol, string, int8, listof, int32

proto = Protocol()
proto.define("demande",string, int32)
proto.define("wait",string)
proto.define("pose", int8,int8)
proto.define("inGame", listof)
proto.define("err1")
proto.define("err2")
proto.define("abort")
proto.define("won_manche",int8)
proto.define("lost_manche",int8)
proto.define("logIn_OK")
proto.define("logIn_Refused")
proto.define("logIn", string)  
proto.define("bonjour",string)
proto.define("affiche",string)
