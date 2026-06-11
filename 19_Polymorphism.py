class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it frpm Two")

one = One()
two = Two()
one.doanything()  # Output: do_it from One
two.doanything()
