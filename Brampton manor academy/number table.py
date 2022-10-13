import operator
ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }

def output(operator,number):
    print(operator,end="│")
    for x in range(number+1):
        print(x,end=" ")
    print("")
    for i in range(number+1):
        print(i,end="│")
        for j in range(number+1):
            print(ops[operator](i,j),end=" ")
        
        print("\n")
    
    
     
operator=input("Please enter an operator")
number=int(input("Please enter a natural number"))
print(output(operator,number))

