def palindrome(num1, num2):
  Palindrome = 0
  for i in range(num1, num2 + 1):
    num = str(i)
    backwardsnum = num[::-1]
    if num == backwardsnum:
      Palindrome = Palindrome + 1
  print(f'Palindrome numbers={Palindrome}')
  return num,backwardsnum


def isLychrel(numb1,num2):
  lychrel=0

num1 = int(input("Integer 1:"))
num2 = int(input("Integer 2:"))
palindrome(num1, num2)
isLychrel(num1, num2)