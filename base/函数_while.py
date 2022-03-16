def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    fullname = f"{first_name} {last_name}"
    return fullname.title()


while True:
    print("\n please tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("first_name:")
    if f_name == 'q':
        break
    l_name = input("last_name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\n Hello, {formatted_name}")
