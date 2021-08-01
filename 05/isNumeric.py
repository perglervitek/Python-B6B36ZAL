def isNumeric(n):
  try:
    f = float(n)
    return True
  except ValueError:
    return False

counter = 5
while counter > 0:
  num = input('Zadejte číslo: ')
  if isNumeric(num):
    counter -= 1
  else:
    print('CHYBA: není číslo')