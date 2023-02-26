def isP(n):
    if n==2:
        return True
    if n%2==0:
        return False
    return all(n%x>0 for x in range(3, int(n**0.5)+1, 2))
 
def genP(n):
    p = [2]
    p.extend([x for x in range(3, n+1, 2) if isP(x)])
    return p
def primepartition(n):
    p = genP(n)
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if p[i]+p[j]==n:
                return True
    return False
def matched(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack
def rotatelist(l,k): 
    output_list = [] 
    k = k%len(l)
      
    
    for item in range(k, len(l)): 
        output_list.append(l[item]) 
      
      
    for item in range(0, k):  
        output_list.append(l[item]) 
          
    return output_list 
###########

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

if fname == "primepartition":
   arg = parse(farg)
   print(primepartition(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "rotatelist":
   (arg1,arg2) = parse(farg)
   myarg1 = arg1[:]
   rotatelist(arg1,arg2)
   if myarg1 == arg1:
     print(rotatelist(arg1,arg2))
   else:
     print("Illegal side effect")
else:
   print("Function", fname, "unknown")
