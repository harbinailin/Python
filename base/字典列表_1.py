# 字典里嵌套列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'pepperoni']
}
print(f"you have ordered a {pizza['crust']}-curst pizza\nwith the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)
