import std_c_types

class Bools:

    def __init__(self,n):
        self.n = n
        self.bits = [0] * n

    def get_bits(self):
        return self.bits
 
    def set_bits(self,*args):
        self.m = len(args)
        # slice
        if self.m > self.n:
            self.index = self.n
        else:
            self.index = self.m
        self.bits = args[0 : self.index]

    def get_bytes(self):
        ret = 0
        cnt = 0
        for i in self.bits:
            if i == 0:
                ret = ret & ~pow(2, cnt)
            else:
                ret = ret | pow(2,cnt)
            cnt = cnt + 1
        return ret
    
    def set_bytes(self,c):
        for i in range(self.n):
            self.bits[i] = (c >> i) & 0x01

class Bools8Type(std_c_types.std_c_types.Type):
    BOOLS8_SIZE = 1 #byte
    def __init__(self):
        super(Bools8Type,self).__init__("bools8_t","B", self.BOOLS8_SIZE)
        
    data = Bools(BOOLS8_SIZE*8)

#class Bools16Type(std_c_types.std_c_types.Type):
#    BOOLS16_SIZE = 2 #byte
#    def __init__(self):
#        super(Bools16Type,self).__init__("bools16_t","H", self.BOOLS16_SIZE)
#        
#    data = Bools(BOOLS16_SIZE*8)
