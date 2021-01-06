
def prnt(x):
  return lambda: print(x)

def sequence(x):
  return lambda: [i() for i in x]
