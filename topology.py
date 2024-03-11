from mininet.topo import Topo


class FatTreeTopo(Topo):
    "Simple Fat Tree Topology Class."

    def build(self, k=4):
        """
        k: The number of ports per switch. This implementation assumes k is even.
           The total number of hosts will be (k^3)/4.
        """
        self.k = k
        numPods = k
        numSwitchesPerPod = k // 2
        numCoreSwitches = (k // 2) ** 2
        numHostsPerEdgeSwitch = k // 2

        # Core switches
        coreSwitches = []
        for i in range(numCoreSwitches):
            switch = self.addSwitch('c{}'.format(i + 1))
            coreSwitches.append(switch)

        # Pods
        for p in range(numPods):
            aggregationSwitches = []
            # Aggregation layer
            for a in range(numSwitchesPerPod):
                switch = self.addSwitch('a{}_{}'.format(p + 1, a + 1))
                aggregationSwitches.append(switch)
                # Connecting aggregation switches to core switches
                for s in range(numSwitchesPerPod):
                    coreIdx = s * numSwitchesPerPod + a
                    self.addLink(switch, coreSwitches[coreIdx])

            # Edge layer
            for e in range(numSwitchesPerPod):
                switch = self.addSwitch('e{}_{}'.format(p + 1, e + 1))
                # Connecting edge switches to aggregation switches
                self.addLink(switch, aggregationSwitches[e])
                # Adding hosts and connecting to edge switches
                for h in range(numHostsPerEdgeSwitch):
                    host = self.addHost('h{}_{}_{}'.format(p + 1, e + 1, h + 1))
                    self.addLink(host, switch)
