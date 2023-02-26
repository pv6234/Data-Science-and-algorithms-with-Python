def rainaverage(l):
  raindata = {}
  for (c,r) in l:
    if c in raindata.keys():
      raindata[c].append(r)
    else:
      raindata[c] = [r]
  outputlist = []
  for c in sorted(raindata.keys()):
    thisaverage = sum(raindata[c])/len(raindata[c])
    outputlist.append((c,thisaverage))
  return(outputlist)

def flatten(l):
  if not(listtype(l)):
    return([l])
  flatlist = []
  for e in l:
    flatlist.extend(flatten(e))
  return(flatlist)

###########

def listtype(l):
  return(type(l) == type([]))

import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "rainaverage":
  arg = parse(farg)
  print(rainaverage(arg))

if fname == "flatten":
  arg = parse(farg)
  print(flatten(arg))
