a = [13, 10, 12, 6, 19, 2]

for a in a:
    if a % 5 == 0:
        print(a)
        break
else:  # it's for, for loop or you can simple write else in if then in else use break after print statement
    print("not found")

for num in range(1, 50):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
