list = []
for i in range(int(input())):
    list.append(int(input()))
for i in range(0, len(list), 1):
    if i%2 == 0:
        print(list[i])
