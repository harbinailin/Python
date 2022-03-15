# 嵌套 字典和列表的组合
alien_0 = {'age': 20, 'color': 'green', 'sex': 'female'}
alien_1 = {'age': 22, 'color': 'red', 'sex': 'male'}
alien_2 = {'age': 21, 'color': 'blue', 'sex': 'male'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 自动生成n个外星人
alienss = []
for alien_number in range(30):
    new_alien = {'age': 20, 'color': 'green', 'sex': 'female', 'hhh': 2}
    alienss.append(new_alien)
# 显示前五个外星人
for alien in alienss[0:5]:
    print(alien)
print('....')
# 打印外星人的总数
print(f"Total number of aliens {len(alienss)}")

for alien in alienss[:5]:
    if alien['age'] == 20:
        alien['age'] = 16
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
    print(alien)
