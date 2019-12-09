class machine:
    _ops = dict()
    def __init__(self, values):
        self.mem = []
        self.reset(values)
        self.debug = False
    def reset(self, values):
        self.mem[:] = values
        self.ip = 0
        self.halted = False
    def peek(self, addr):
        return self.mem[addr]
    def poke(self, addr, val):
        self.mem[addr] = val
    def step(self):
        if self.debug: self._debug_print()
        op = self.mem[self.ip]
        if not self.halted: self._ops[op](self)
    def run(self):
        while not self.halted: self.step()
    def _debug_print(self):
        print('ip=',self.ip)
        for pos in range(0, len(self.mem), 10):
            print(pos, self.mem[pos:pos+10])
    def _add(self):
        p1,p2,p3 = self.mem[self.ip+1:self.ip+4]
        self.mem[p3] = self.mem[p1] + self.mem[p2]
        self.ip += 4
    def _mul(self):
        p1,p2,p3 = self.mem[self.ip+1:self.ip+4]
        self.mem[p3] = self.mem[p1] * self.mem[p2]
        self.ip += 4
    def _halt(self):
        self.halted = True

    _ops[1] = _add
    _ops[2] = _mul
    _ops[99] = _halt
