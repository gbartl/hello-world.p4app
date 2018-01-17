from bm_runtime.standard import Standard
from bm_runtime.standard.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
import struct

def thrift_connect(thrift_ip, thrift_port):
    transport = TSocket.TSocket(thrift_ip, thrift_port)
    transport = TTransport.TBufferedTransport(transport)
    bprotocol = TBinaryProtocol.TBinaryProtocol(transport)
    protocol = TMultiplexedProtocol.TMultiplexedProtocol(bprotocol, "standard")
    client = Standard.Client(protocol)
    transport.open()
    return client

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = thrift_connect('localhost', 9090)

transport.open()

x = client.bm_mgmt_get_info()
print x

matchParams  = [BmMatchParam(type=BmMatchParamType.EXACT, exact=BmMatchParamExact('\x20\x10\x14\x14'))]

client.bm_mt_add_entry(0, "forward", matchParams, "_drop", [], BmAddEntryOptions(0))
