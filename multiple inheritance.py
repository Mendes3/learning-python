class Buini():
    def name(self):
        print("buinis name is jenisha")

class mukul():
    def gender(self):
        print("mukul is dhukul")

class siblings(Buini,mukul):
    pass


x = siblings()
x.gender()
x.name()

