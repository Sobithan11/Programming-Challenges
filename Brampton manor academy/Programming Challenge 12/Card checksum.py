def valid_number(number):
  if len(number) != 16:
    if len(number) > 16:
      print("Too long")
    elif len(number) < 16:
      print("Too short")
    return False
  else:
    return True


number = input("Enter a number")
integer = int(number)
payload = integer // 10


def luhn_checksum(payload):

  def digits_of(n):
    return [int(d) for d in str(n)]

  digits = digits_of(number)
  odd_digits = digits[-1::-2]
  even_digits = digits[-2::-2]
  checksum = 0
  checksum += sum(odd_digits)
  for d in even_digits:
    checksum += sum(digits_of(d * 2))
  if checksum % 10 == 0:
    return True
