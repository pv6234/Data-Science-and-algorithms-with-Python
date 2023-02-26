def remdup(l):
    result = []
    for x in l:
        if x not in result:
            result.append(x)
        else:
            result.remove(x)
            result.append(x)
    return result

def splitsum(l):
    pos = sum(x ** 2 for x in l if x > 0)
    neg = sum(x ** 3 for x in l if x < 0)
    return [pos, neg]


def matrixflip(m, d):
    if d == 'h':
        return [row[::-1] for row in m]
    elif d == 'v':
        return m[::-1]
    else:
        return m

import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "remdup":
   arg = parse(farg)
   print(remdup(arg))
elif fname == "splitsum":
   arg = parse(farg)
   print(splitsum(arg))
elif fname == "matrixflip":
  (arg1,arg2) = parse(farg)
  savearg1 = []
  for row in arg1:
    savearg1.append(row[:])
  myans = matrixflip(arg1,arg2)
  if savearg1 == arg1:
    print(myans)
  else:
    print("Illegal side effect")
else:
   print("Function", fname, "unknown")

