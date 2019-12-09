class machine:
    _ops = dict()
    def __init__(self, values, f_in = lambda :0, f_out = print):
        self.mem = []
        self.reset(values,f_in,f_out)
        self.debug = False
    def reset(self, values, f_in = None, f_out = None):
        self.mem[:] = values
        if f_in: self._input = f_in
        if f_out: self._output = f_out
        self.ip = 0
        self.halted = False
    def peek(self, addr):
        return self.mem[addr]
    def poke(self, addr, val):
        self.mem[addr] = val
    def step(self):
        if self.debug: self._debug_print()
        if not self.halted:
            op = self.mem[self.ip]
            self.ip += 1
            self.modes = op // 100;
            self._ops[op%100](self)
    def run(self):
        while not self.halted: self.step()
    def _debug_print(self):
        print('ip=',self.ip)
        for pos in range(0, len(self.mem), 10):
            print(pos, self.mem[pos:pos+10])

    def _get_parms(self, types):
        parms = []
        for t in types:
            p = self.mem[self.ip]
            self.ip += 1
            m = self.modes % 10
            self.modes //= 10
            if m == 0 and t == 'i': p = self.mem[p]
            parms.append(p)
        return parms

    def _add(self):
        p1,p2,p3 = self._get_parms('iio')
        self.mem[p3] = p1 + p2
    def _mul(self):
        p1,p2,p3 = self._get_parms('iio')
        self.mem[p3] = p1 * p2
    def _halt(self):
        self.halted = True

    def _cmpeq(self):
        p1,p2,p3 = self._get_parms('iio')
        self.mem[p3] = 1 if p1 == p2 else 0
    def _cmplt(self):
        p1,p2,p3 = self._get_parms('iio')
        self.mem[p3] = 1 if p1 < p2 else 0
    def _jc(self):
        p1,p2 = self._get_parms('ii')
        if p1: self.ip = p2
    def _jnc(self):
        p1,p2 = self._get_parms('ii')
        if not p1: self.ip = p2

    def _out(self):
        p = self._get_parms('i')[0]
        self._output(p)
    def _stor(self):
        p = self._get_parms('o')[0]
        x = self._input()
        self.mem[p] = x

    _ops[1] = _add
    _ops[2] = _mul
    _ops[3] = _stor
    _ops[4] = _out
    _ops[5] = _jc
    _ops[6] = _jnc
    _ops[7] = _cmplt
    _ops[8] = _cmpeq
    _ops[99] = _halt
