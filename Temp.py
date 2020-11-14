class A():

    def alfa(self):
        self.change = 'hit'
        return self.change

class B():

    def beta(self):
        self.otherclass = A()
        print(self.otherclass.alfa())
        return '50'


run = B()
run.beta()
