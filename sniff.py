import sys
import ipaddress
from io import BytesIO

from dpkt.ip import IP
from dpkt.tcp import TCP
from dpkt.ethernet import Ethernet, ETH_TYPE_IP
from dpkt import pcap
import msgpack


class MsgpHandler:
    def __init__(self):
        self.conn = dict()
        self.rere = dict()

    def process(self, ts, pkt):
        eth = Ethernet(pkt)
        if eth.type == ETH_TYPE_IP:
            ip = eth.data
            # print("ip", dir(ip))
            tcp = ip.data
            # print("tcp", dir(tcp))
            ip1, ip2 = map(ipaddress.ip_address, [ip.src, ip.dst])
            sport, dport = [tcp.sport, tcp.dport]
            tupl = (str(ip1), str(ip2), tcp.sport, tcp.dport)
            if tupl not in self.conn:
                self.conn[tupl] = msgpack.Unpacker(raw=True)
            self.conn[tupl].feed(tcp.data)
            if len(tcp.data):
                print("{0}:{2} -> {1}:{3}".format(*tupl))
                for unpacked in self.conn[tupl]:
                    print("\t", unpacked)



if __name__ == '__main__':
    f = open(sys.argv[1], "rb")
    src = pcap.Reader(f)
    m = MsgpHandler()
    for ts, pkt in src:
        m.process(ts, pkt)

