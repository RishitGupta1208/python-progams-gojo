class priv:
    __privar=234
    def __privmeth(self):
        print("hi i am private funtion")
    def helllo(self):
        print(priv.__privmeth)
obj=priv()
obj.__privmeth
obj.helllo