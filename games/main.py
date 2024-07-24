import random

def text(option):
  if option.lower() == 'piedra': return 0, 'piedra'
  elif option.lower() == 'papel': return 1, 'papel'
  elif option.lower() == 'tijera': return 2, 'tijera'
  else: return 10

def choice(option_user, option_computer):
  if option_user[0] - option_computer[0] == 0:
    return f'EMPATE LA MAQUINA ESCOGIÓ {option_computer[1]}', 'same'
  elif option_user[0] - option_computer[0] in (-2, 1):
    return f'GANASTE LA MAQUINA ESCOGIÓ {option_computer[1]}', 'win'
  elif option_user[0] - option_computer[0] in (-1, 2):
    return f'PERDISTE LA MAQUINA ESCOGIÓ {option_computer[1]}', 'lose'
  else: return 'OPCION INCORRECTA'

def game():
  machine = 0
  user = 0
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    choice_maquina = random.choice(['piedra', 'papel', 'tijera'])
    choice_user = input('Escoge piedra, papel o tijera => ')
    result, win = choice(text(choice_user), text(choice_maquina))
    print(result)
    if win == 'same':
      rounds+=1
      continue
    elif win == 'win':
      user+=1
    else:
      machine+=1
    if machine == 2 or user == 2:
      if machine == 2: print(f'Ganadror es la maquina {machine} a {user}')
      else: print(f'Ganadror es el usuario {user} a {machine}')
      break
    rounds+=1
game()