li = []
for i in range(3):
    x, y = map(int, input().split())
    li.append([x, y])

new_x = 0
new_y = 0

if li[0][0] == li[1][0]:
    new_x = li[2][0]
elif li[0][0] == li[2][0]:
    new_x = li[1][0]
elif li[1][0] == li[2][0]:
    new_x = li[0][0]

if li[0][1] == li[1][1]:
    new_y = li[2][1]
elif li[0][1] == li[2][1]:
    new_y = li[1][1]
elif li[1][1] == li[2][1]:
    new_y = li[0][1]

print(new_x, new_y)