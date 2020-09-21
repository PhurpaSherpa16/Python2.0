class Comp:
    def __init__(self,cpu,gpu):
        self.cpu = cpu
        self.gpu = gpu

    def config(self):
        print("Config is ", self.cpu, self.gpu)


comp1 = Comp('i5',16)
comp1.config()