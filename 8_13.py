def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('David', 'Navarro',location='Los Angeles',field='Computer Science', hobby='Painting')
print(user_profile)

if 'hobby' in user_profile:
    print("Hobby is present")