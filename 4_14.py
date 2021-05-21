all_users = ['user1', 'user2', 'user3']
all_users.append('user4')

untrusted_users =['user1', 'user4']
print(untrusted_users)

trusted_users =[]
for users in all_users:
    trusted_users.append(users)
for users in untrusted_users:
    trusted_users.append(users)

print(trusted_users)

all_users = {'username1','username2','username3','username4','username5'}
untrusted_users = {'username1', 'username6'}

trusted_users = all_users - untrusted_users
print(trusted_users)