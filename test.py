from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from topology import *
from mininet.util import dumpNodeConnections


# def run():
#     topo = FatTreeTopo(k=4)  # Create a fat tree topology with k=4
#     net = Mininet(topo=topo, autoSetMacs=True)
#     net.start()
#
#     print("Dumping host connections...")
#     dumpNodeConnections(net.hosts)
#
#     print("Testing connectivity between hosts...")
#     for src in net.hosts:
#         for dst in net.hosts:
#             if src != dst:
#                 src.cmdPrint(f'ping -c 3 {dst.IP()}')
#
#     print("Testing bandwidth between hosts...")
#     for src in net.hosts:
#         for dst in net.hosts:
#             if src != dst:
#                 net.iperf((src, dst))
#
#     CLI(net)
#
#     net.stop()


def run():
    topo = FatTreeTopo(k=4)  # You can adjust k as needed.
    net = Mininet(topo=topo, controller=Controller)
    net.start()

    print("Testing network connectivity")
    # net.pingAll()
    print("Running CLI")
    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
