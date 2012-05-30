from pynetez.Protocol import Protocol, int32, char

proto = Protocol()
proto.define("pending")
proto.define("connected")
proto.define("go")
proto.define("wait")
proto.define("posed", int32, char)
proto.define("err")
proto.define("abort")
proto.define("won") 

