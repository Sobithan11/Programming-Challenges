I=1
V=5
X=10
L=50
C=100
pre_romans = {'VC': 95, 'IC': 99, 'VL': 45, 'XL': 40, 'XC': 90,'IL': 49, 'IX': 9, 'IV': 4}
def convert(num):
  integer=0
  n1=0
  for i in range (0,len(num)):
    for x in pre_romans.keys():
      if x in num:
        integer+=pre_romans[x]
        num.replace(pre_romans[x],"")
    if (num[i])== "I":
      integer+=1
    elif (num[i])=="V":
      integer+=5
    elif (num[i])=="X":
      integer+=10
    elif (num[i])=="L":
      integer+=50
    elif (num[i])=="C":
      integer+=100
  return integer
print(pre_romans.keys())
int1=(str(input("Please enter first roman numeral")).upper())
int2=(str(input("Please enter second roman numeral")).upper())
int1=convert(int1)
print(int1)
int2=convert(int2)
print(int2)
int3=int1+int2
print (int3)