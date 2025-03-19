class DB:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return "Name:{}; Address:{}".format(self.name, self.address)
