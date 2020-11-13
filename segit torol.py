class A():
   # change = ''
    def alfa(self):
        self.change = 'hit'
        return self.change

class B():
    otherclass = A()
    def beta(self):
        print(self.otherclass.alfa())


run = B()
run.beta()
