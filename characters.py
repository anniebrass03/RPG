# Description for characters/suspects for view option
print ("Description of suspects:")
blake = {
  'name': 'Blake Morris',
  'age': '30',
  'job': 'banker',
  'relation': 'co-workers'
  }

# printing sentences describing Blake Morris
for q, a in blake.items():
  name = blake['name']
  age = blake['age']
  job = blake['job']
  relation = blake['relation']
print (f'{name} is a family man, husband and dad to 2 girls.')
print (f'He is {age} years old.')
print (f'He and the victim were {relation} at their {job} job.')
print ('Was investigated for connections with a drug cartel.\n')

# Dictionary describing suspect Patty Rose
patty = {
    'name': 'Patty Rose',
    'age': '52',
    'job': 'retired',
    'relation': 'neighbors'
}

# printing sentences describing Patty Rose
for q, a in patty.items():
  name = patty['name']
  age = patty['age']
  job = patty['job']
  relation = patty['relation']
print (f'{name} is a {job} school teacher.')
print (f'She is {age} years old.')
print (f'She was {relation} with the victim.')
print (f'Seemingly kind, {name} is disliked for being a strict neighbour.\n')

# Dictionary describing suspect Emily Joy
emily = {
  'name': 'Emily Joy',
  'age': '17',
  'job': 'student',
  'relation': 'stepdad'
}

# printing sentences describing Emily Joy
for q, a in emily.items():
  name = emily['name']
  age = emily['age']
  job = emily['job']
  relation = emily['relation']
print (f'{name} is a troubled highschool {job}.')
print (f'She is {age} years old.')
print (f'The victim was her {relation}.')
print(f'{name} is known for her mean demeanor and her rebelious tendencies.\n')
print('You can interview these suspects by going to the FBI map.')
