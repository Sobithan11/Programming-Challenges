
def addition(num1,num2):
  return num1+num2
def subtraction(num1,num2):
  return num1-num2
def multiplication(num1,num2):
  return num1+num2
def division(num1,num2):
  return num1/num2
def integer_division(num1,num2):
  return num1//num2
def modulo(num1,num2):
  return num1%num2
def exponentiation(num1,num2):
  return num1**num2

def RPN(calculation):
  splitcalc=calculation.split(" ")
  num1=int(splitcalc[0])
  num2=int(splitcalc[1])
  operator=splitcalc[2]
  return num1,num2,operator

calculation=input("Enter your calculation:")
if calculation=="q":
  print("")
else:
  num1=int(RPN(calculation)[0])
  num2=int(RPN(calculation)[1])
  operator=RPN(calculation)[2] 
  def output(num1,num2,operator):
    if operator=="+":
      print(addition(num1,num2))
    if operator=="-":
      print(subtraction(num1,num2))
    if operator=="*":
      print(multiplication(num1,num2))
    if operator=="/":
      print(division(num1,num2))
    if operator=="//":
      print(integer_division(num1,num2))
    if operator=="%":
      print(modulo(num1,num2))
    if operator=="**":
      print(exponentiation(num1,num2)) 
  output(num1,num2,operator)




while calculation!="q":
  calculation=input("Enter your calculation:")
  if calculation=="q":
    print("")
  else:    
    num1=int(RPN(calculation)[0])
    num2=int(RPN(calculation)[1])
    operator=RPN(calculation)[2]
    output(num1,num2,operator)

