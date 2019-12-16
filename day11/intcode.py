from collections import defaultdict
class machine:
    _ops = dict()
    def __init__(self, values):
        self.mem = defaultdict(int)
        for i in range(len(values)): self.mem[i] = values[i] 
        self.ip = 0
        self.rb = 0
        self.halted = False
        self.blocked = False
        self._inputs = []
        self._outputs = []
        self.debug = False
        self.pause_on_output = False
    def get(self):
        return self._outputs.pop(0) if self._outputs else None
    def put(self, x):
        self._inputs.append(x)
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
        self.blocked = False
        while not self.halted and \
              not self.blocked and \
              not (self.pause_on_output and self._outputs): self.step()
    def _debug_print(self):
        print('ip=',self.ip,' rb=',self.rb)
        print(self.mem)

    def _get_parms(self, n):
        parms = []
        for i in range(n):
            p = self.mem[self.ip]
            m = self.modes % 10
            self.modes //= 10
            if m == 1: p = self.ip
            if m == 2: p += self.rb
            parms.append(p)
            self.ip += 1
        return parms

    def _add(self):
        p1,p2,p3 = self._get_parms(3)
        self.mem[p3] = self.mem[p1] + self.mem[p2]
    def _mul(self):
        p1,p2,p3 = self._get_parms(3)
        self.mem[p3] = self.mem[p1] * self.mem[p2]
    def _halt(self):
        self.halted = True
    def _cmpeq(self):
        p1,p2,p3 = self._get_parms(3)
        self.mem[p3] = 1 if self.mem[p1] == self.mem[p2] else 0
    def _cmplt(self):
        p1,p2,p3 = self._get_parms(3)
        self.mem[p3] = 1 if self.mem[p1] < self.mem[p2] else 0
    def _jc(self):
        p1,p2 = self._get_parms(2)
        if self.mem[p1]: self.ip = self.mem[p2]
    def _jnc(self):
        p1,p2 = self._get_parms(2)
        if not self.mem[p1]: self.ip = self.mem[p2]
    def _out(self):
        p = self._get_parms(1)[0]
        self._outputs.append(self.mem[p])
    def _stor(self):
        p = self._get_parms(1)[0]
        if self._inputs:
            self.mem[p] = self._inputs.pop(0)
            self.blocked = False
        else:
            self.ip -= 2
            self.blocked = True
    def _setrb(self):
        p = self._get_parms(1)[0]
        self.rb += self.mem[p]

    _ops[1] = _add
    _ops[2] = _mul
    _ops[3] = _stor
    _ops[4] = _out
    _ops[5] = _jc
    _ops[6] = _jnc
    _ops[7] = _cmplt
    _ops[8] = _cmpeq
    _ops[9] = _setrb
    _ops[99] = _halt
