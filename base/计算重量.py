while True:
    try:
        weight = int(input("请输入货物重量以计算运费："))
        if weight > 0 and weight <= 50:
            price = weight * 80500
        elif weight > 50 and weight < 100:
            price = weight * 75
        elif weight >= 100 and weight < 1000:
            price = weight * 60
        elif weight >= 1000:
            price = weight * 55
        else:
            print("请输入符合规定的重量")
        print(f"此次的货物重量是：{weight},此次的总运费是{price}")
    except:
        break
