def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = 54
num2 = 24
print("The L.C.M. of" , num1,"and", num2,"is", lcm(num1, num2))
def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i           
    return hcf

num1 = 54 
num2 = 24
print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))
