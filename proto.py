from pynetez.Protocol import Protocol, int32, listof

proto = Protocol()
proto.define("pending")
proto.define("connected")
proto.define("go")
proto.define("wait")
proto.define("pose", int32 )
proto.define("inGame", listof)
proto.define("err1")
proto.define("err2")
proto.define("abort")
proto.define("won") 
proto.define("CreatePlayer",listeof)
proto.define("AfficheMain",listeof)

