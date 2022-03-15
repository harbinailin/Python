# pastrami 卖完了，将其从列表中删除，并将列表中已经做好的三明治打印出来
sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami','turkey', 'roast beef', 'pastrami']
finished_sandwich=[]
print("Sorry,pastrami is sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"i am working on your {current_sandwich} sandwich")
    finished_sandwich.append(current_sandwich)
for sandwich in finished_sandwich:
    print(f"{sandwich.title()} has finished")
