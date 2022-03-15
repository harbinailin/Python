# 顾客买披萨，查看顾客要求的披萨配料在不在店家的配料表中，在的话返回可提供，不在配料表中，返回不存在。
available_toppings=['mushrooms','olivers','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','apple','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"{requested_topping.title()} is available")
    else:
        print(f"Sorry! We dont have {requested_topping.title()}")
print('finish ordering!')