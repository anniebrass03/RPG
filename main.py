# Course: CS 30
# Period: 1
# Date created: Feb 5th 2021
# Date last modified: Feb 11th 2021
# Name: Annabelle Brass
# Description: Modules and maps for RPG

from maps import data, data_1

# Start of RPG
print('Welcome to Crime Solver.')
print('You are here to solve the murder of Joel Mann.\n')

print('What would you like to do?')
things = ['* start game', '* view description of suspect and evidence list']
print('\n'.join(things))

while True:
  do = input('Enter choice (start/view): ')
  if do == 'start' or do == 'Start':
    # Importing game code for 'Start' option
    import game as game
    break
  if do == 'view' or do == 'View':
    # Importing inventory and character info for 'View' option
    import inventory as inventory
    import characters as characters
    break
  else:
    print("That is not an option.")
