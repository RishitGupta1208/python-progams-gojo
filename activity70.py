class india():
    def capital(self):
        print("New Dehli is the capital of India")
    def language(self):
        print("Hindi is widely spoken here")
    def type(self):
        print("india is a developing country")
class USA():
    def capital(self):
        print("Washinton D.C. is the capital of USA")
    def language(self):
        print("English is the primary language spoken here")
    def type(self):
        print("USA is a developed country")
obji=india()
obju=USA()
for i in(obji,obju):
    i.capital()
    i.language()
    i.type()