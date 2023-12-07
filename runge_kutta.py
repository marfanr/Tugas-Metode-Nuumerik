import string

class RungeKutta:
    plus = []
    minus = []
    variables = []
    items = []

    def __init__(self, df, xout, x0, y0, h):
        # split for +
        self.plus = df.split('+')        
        
        # find kontant
        for i in self.plus:
            # parse konstant and variable
            variable = []
            constant = []
            power = []
            for j in range(len(i)):
                if i[j] in string.ascii_letters:
                    variable.append(i[j])
                    if i[j] not in self.variables:
                        self.variables.append(i[j])
                    if i[j-1] in string.digits and j < len(i):
                        constant.append(i[:j])                        
                    if j < len(i)-2 and  i[j+1] is '^':
                        if i[j+2] in string.digits:
                            power.append(i[j+2])                               
                    else:                                                    
                        power.append('-')
                    if j < len(i)-1 and i[j+1] is string.ascii_letters:
                        constant.append(1)     
            self.items.append([constant, variable, power])


    def calc_derivative(self, *params):
        params_len  = 0
        for i in params:
            params_len += 1
        if params_len != len(self.variables):
            print("Error: params length not equal variables length")
            return
        
        total = 0
        for i in self.items:            
            const = int(i[0][0])
            for j in range(len(i[1])):
                if i[2][j] is not '-':
                    const *= pow(params[j], int(i[2][j]))
                else:
                    const *= params[j]
            total += const
        return total
    

def main():
    x = "2x^2+3y^2+4xy"
    rk = RungeKutta(x, 1.2, 1, 1, 0.2)
    print("F(1,2) = %s\n = %d" % (x, rk.calc_derivative(1, 2)))
    pass

if __name__ == '__main__':
    main()