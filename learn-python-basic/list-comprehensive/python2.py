users = [
  { 'name' : 'fihan', 'age' : 22 },
  { 'name' : 'dilan', 'age' : 20},
  { 'name' : 'pratama', 'age' : 21 }
]
users_name = [user['name'] for user in users]
users_name2 = [user['name'] for user in users if user['age'] > 20]

print(users)
print(users_name)
print(users_name2)