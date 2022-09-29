def game(yournumber,friendsnumber):
  factor=99-yournumber
  step1=friendsnumber+factor
  step2=step1//100
  step3=step1%100
  step4=step2+step3
  step5=friendsnumber-step4
  return step5
  
print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet i know what the result of those calculations will be! ") 
yournumber=int(input("*You* This will be the answer. Select a number between 10-49:"))
friendsnumber=int(input("*Player* Pick any number 50-99: "))
print(f'I said the answer was {yournumber} and the calculation result is {game(yournumber,friendsnumber)}')



