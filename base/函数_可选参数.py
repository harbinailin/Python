def whole_name(first_name, second_name, middle_name=''):
    if middle_name:
        print(f"whole name is {first_name} {middle_name} {second_name}")
    else:
        print(f"whole is {first_name} {second_name}")


whole_name('alice', 'shoort')
whole_name('alice', 'shooo', 'hshai')
