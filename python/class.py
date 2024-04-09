class router(object):
    def __init__(self, name, interface_number, vendor):
        self.name = name
        self.interface_number = interface_number
        self.vendor = vendor

    def __str__(self):
        return f"Router: {self.name}, Interfaces: {self.interface_number}, Vendor: {self.vendor}"

r1 = router("SF01-R1", 64, "Cisco")
print(r1)
