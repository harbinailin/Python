users = {
    'ailin': {
        'age': 20,
        'subject': 'computer',
        'school': 'hlju'
    },
    'yyds': {
        'age': 22,
        'subject': 'software',
        'school': 'dbld'
    }
}
for user_name,user_info in users.items():
    print(f"Username:{user_name}")
    print(f"Userinfo: {user_info['school'].upper()} {user_info['subject'].title()} ")
