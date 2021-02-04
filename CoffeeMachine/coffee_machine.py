print('Write how many cups of coffee you will need:')
x = int(input())
water = 200 * x
milk = 50 * x
coffee_beans = 15 * x
print(f'For {x} cups of coffee you will need:')
print(f'{water} ml of water')
print(f'{milk} ml of milk')
print(f'{coffee_beans} g of coffee beans')