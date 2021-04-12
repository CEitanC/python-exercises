
x = input()
for i in range(2, x):
    if x % i == 0:
        print("True")
        break
    if i*i > x:
        print("False")
        break
