from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        network1 = random.randint(11,223)
        IPv4Network.__init__(self

    def key_value(self):
       for i in range(0,50):
            network_list = IPv4Network((0x0b,8),strict=False)









