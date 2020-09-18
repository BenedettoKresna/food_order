class MenuPesanan:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def information(self):
        return self.name + ": Rp." + str(self.price)

    def biaya(self, porsi):
        return self.price * porsi

