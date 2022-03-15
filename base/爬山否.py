# 录入人名和想要爬的山名 循环
responses = {}
polling_active = True
while polling_active:
    name = input("please enter your name: ")
    response = input("which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("would you like to let another person respond(yes/no)?")
    if repeat == 'no':
        polling_active = False
print("\n---polling results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
