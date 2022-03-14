import ipaddress
from io import BytesIO

from dpkt.ip import IP
from dpkt.tcp import TCP
from dpkt.ethernet import Ethernet, ETH_TYPE_IP
from dpkt import pcap
import msgpack


class MsgpHandler:
    def __init__(self, dump_bytes=False):
        self.conn = dict()
        self.rere = dict()
        self.dump_bytes = dump_bytes

    def process(self, ts, pkt):
        eth = Ethernet(pkt)
        buff = dict()
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
            if tupl not in buff:
                buff[tupl] = BytesIO()
            self.conn[tupl].feed(tcp.data)
            buff[tupl].write(tcp.data)
            if len(tcp.data):
                print("{0}:{2} -> {1}:{3}".format(*tupl))
                ok = False
                for unpacked in self.conn[tupl]:
                    print("\t", unpacked)
                    ok = True
                if ok:
                    buff[tupl].seek(0)
                    if self.dump_bytes:
                        print(buff[tupl].read())


if __name__ == "__main__":
    import sys
    import os

    f = open(sys.argv[1], "rb")
    src = pcap.Reader(f)
    m = MsgpHandler(dump_bytes=(os.getenv("BINARY") is not None))
    for ts, pkt in src:
        m.process(ts, pkt)
