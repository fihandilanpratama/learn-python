user_groups = [
  [
    { 'name' : 'fihan', 'age' : 22 },
    { 'name' : 'dilan', 'age' : 21 }
  ],
  [
    { 'name' : 'miku', 'age' : 19 },
    { 'name' : 'itsuki', 'age' : 19 }
  ]
]

users_name = [person['name'] for group in user_groups for person in group if person['age'] < 20]
print(user_groups)
print(users_name)