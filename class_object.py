__author__ = 'lyndsay.beaver'


class Example:
    def __init__(self, **kwargs):  # passes in a dictionary  a single * passes in a touple
        self.variables = kwargs

    def set_vars(self, k, v):  # key and value
        self.variables[k] = v

    def get_vars(self, k):
        return self.variables.get(k, None)


var = Example()
var.set_vars('name', 'lyndsay')
print(var.get_vars('name'))