# The code to play game
from maps import data, data_1

actions = ['* FBI (suspects map)', '* Lab (evidence map)']
print('\nWhere would you like to go:')
print('\n'.join(actions))
while True:
  items = input('\nEnter choice: ')
# Code goes to FBI map
  if items == 'FBI' or items == 'fbi':
    print("Map for FBI:\n")
    for i in range(len(data)):
      for j in range(len(data[i])):
        print(data[i][j], end='  ')
      print()
    direct = input('\nEnter direction (up, down or right) :')
    if direct == 'down' or direct == 'Down':
      print("You are going to interview Blake Morris.")
      break
    if direct == 'right':
      print("You are going to interview suspect Emily Joy.")
      break
    if direct == 'up':
      print("You are interviewing Patty Rose?")
      break
    else:
      print("Invalid input please enter valid choose")

  if items == 'Lab' or items == 'lab':
    print("Map for Lab:\n")
    for i in range(len(data_1)):
      for j in range(len(data_1[i])):
        print(data_1[i][j], end='  ')
      print()
    direct = input('\nEnter direction (up, down or right) :')
    if direct == 'down':
      print("Would you like a clue?")
      break
    if direct == 'up':
      print("Would you like to examine pencil?")
      break
    if direct == 'right':
      print("You are examining the fabric.")
      break
    else:
      print("Invalid, please print valid answer.")

  else:
    print("Invalid, please print valid answer.")