import random
from random import randint

def check_password(line : str):
  output = []
  elem_alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  elem_sym = '!@#\$%^&*()-+'
  k = 0

  if (len(line) < 12):
   output.append("увеличить число символов - " + str(12 - len(line)))

  for i in line:
      if(i.isdigit()):
       k += 1
  if(k == 0):
    output.append("добавить 1 цифру")

  k = 0
  n = 0
  for i in line:
    if(i.isupper()):
      k += 1
    if(i.islower()):
      n += 1
  if(k == 0):
    output.append("добавить 1 заглавную букву")
  if(n == 0):
    output.append("добавить 1 строчную бувку")

  k = 0
  b = True
  for i in line:
    if i in elem_sym:
      k += 1
    elif i.isdigit():
      next
    elif i in elem_alph:
      next
    else:
      print("Недопустисый символ: " + i)
      b = False
  if(k == 0):
    output.append("добавить 1 символ из списка '!@#\$%^&*()-+'")

  if b:
    if not output:
      print("Сильный пароль")
    else:
      print("Пароль слабый. Рекомендации: " + str(", ".join(output)) + ".")
  return

def gen_password(n):
    password = []
    num = randint(1, n - 3)
    for i in range(num):
        password.append(random.choice('1234567890'))
    n -= num
    num = randint(1, n - 2)
    for i in range(num):
        password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    n -= num
    num = randint(1, n - 1)
    for i in range(num):
        password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    n -= num
    for i in range(n):
        password.append(random.choice('!@#\$%^&*()-+'))
    random.shuffle(password)
    return ''.join(password)