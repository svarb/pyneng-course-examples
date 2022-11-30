class IPAddress:
    def __init__(self, ip, mask):
        self.address = ip
        self.mask = mask

    def info(self):
        print(f"IP address\nIP {self.address}")

    def to_bin(self):
        octets = [f"{int(octet):08b}" for octet in self.address.split(".")]
        return "".join(octets)


ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.2.2.2", 24)


