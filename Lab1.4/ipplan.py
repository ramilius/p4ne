from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        mask = random.randint(8,23)
        network = random.randint(11,223)
        network = str(network) + ".0.0.0" + "/" + str(mask)
        IPv4Network.__init__(self,network,strict = False)

    def key_value(self):
        return (self.netmask._ip,self.network_address._ip)


Nets = []
for i in range(0,50):
    net = IPv4RandomNetwork()
    Nets.append(net)



Nets2 = sorted(Nets,key = IPv4RandomNetwork.key_value)
print(Nets2)









