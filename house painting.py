x = float(input())
y = float(input())
h = float(input())

front_wall = ((x * x) - (1.2 * 2))
back_wall = x * x

side_walls = 2 * (x * y - 1.5 * 1.5)

roof = 2 * (x * y) + 2 * ((x * h)/2)

green = (front_wall + back_wall + side_walls) / 3.4
red = roof / 4.3

print(f'{green:.2f}')
print(f'{red:.2f}')

