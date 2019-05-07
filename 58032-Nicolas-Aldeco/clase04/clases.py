class Calculator(object):
    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.op = None
    
    def ingresar(self,input_x):
        if input_x == 'C':
            self.input1 = 0
            self.input2 = 0
            self.op = None
            return
        try:
            num = int(input_x)
            if self.op == None:
                self.input1 = self.input1 * 10 + num
                return
            self.input2 = self.input2 * 10 + num
        except:
            op_ant = False
            if self.op != None:
                op_ant = True
            if input_x == '=' or op_ant == True:
                if self.op == '+':
                    self.input1 += self.input2
                if self.op == '-':
                    self.input1 -= self.input2
                if self.op == '/':
                    self.input1 /= self.input2
                if self.op == '*':
                    self.input1 *= self.input2
            else:
                self.op = input_x
                return
            self.op = None
            self.input2 = 0
            if op_ant == True:
                self.op = input_x
    def display(self):
        return str(self.input1)