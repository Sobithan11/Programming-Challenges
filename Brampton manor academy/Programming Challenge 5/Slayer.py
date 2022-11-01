import random
num_list=["0","1","2","3","4","5","6","7","8","9"]
def process():
  condition=False
  while condition!=True:
    randomNum=random.sample(num_list,10)
    S=randomNum[1]
    L=randomNum[2]
    A=randomNum[3]
    Y=randomNum[4]
    E=randomNum[5]
    R=randomNum[6]
    number=S+L+A+Y+E+R
    number2=L+A+Y+E+R+S
    if int(number)*3==int(number2):
      condition=True
      return number
ans=int(process())
ans1=int(process())
while ans==ans1:
  if ans==ans1:
    ans1=int(process())
ans1=int(ans1)
ans=int(ans)


def output():
  print("Guess a six digit number SLAYER so that the following equation is true where each letter stands for the digit in the position shown:SLAYER+SLAYER+SLAYER=LAYERS")
  guess=int(input("Enter your guess for slayer"))
  if guess!=ans1 and guess!=ans :
    print("Your guess is incorrect:")
    print(f'SLAYER+SLAYER+SLAYER={guess*3}')
    guess=str(guess)
    print(f"LAYERS={guess[1]+guess[2]+guess[3]+guess[4]+guess[5]+guess[0]}")
    print("Thanks for playing")
  elif guess==ans1 or guess==ans:
    print("Your guess is correct")
    print(f'SLAYER+SLAYER+SLAYER={guess*3}')
    guess=str(guess)
    print(f"LAYERS={guess[1]+guess[2]+guess[3]+guess[4]+guess[5]+guess[0]}")
    print("Thanks for playing")
print(output())   