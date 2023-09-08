class Calculator(AdvancedArithmetic):
    self.n, self.l = n, []
    for i in range(1, self.n + 1):
        if self.n%i == 0:
            self.l.append(i)
    return sum(self.l)
