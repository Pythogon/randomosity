from random import randint as r
def select():
  global opened
  filename = input("Enter the file's name. ") + '.txt'
  with open (filename, 'r+') as filen:
    opened = filen.read()
  opened = opened.split('\n')
while True:
  opened = ''
  select()
  while True:
    try:
      gay = int(input('How many should be chosen?'))
      if len(opened) < gay:
        raise Error
      break
    except:
      print("That wasn't quite right. Please try again.")
  for x in range(gay):
   magic = r(1,len(opened))
   print(opened[magic-1])
   opened.pop(magic-1)

