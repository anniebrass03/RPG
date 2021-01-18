# Course: CS 30
# Period: 1
# Date created: Jan 14th 2021
# Date last modified: Jan 15th 2021
# Name: Annabelle Brass
# Description: Inventory using numerical list for RPG game

# Numbered list for suspects
suspects = ['Blake Morris', 'Patty Rose', 'Jacob Chamber', 'Emily Joy']
print("List of suspects:")
for i, suspects in enumerate(suspects, 1):
  print(f"{i}. {suspects}")
print("")

# Numbered list or evidence
evidence = ['Pencil', 'hair', 'glasses', 'dirt']
print("List of evidence:")
for i, evidence in enumerate(evidence, 1):
  print(f"{i}. {evidence}")
