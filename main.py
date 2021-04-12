def is_prime(x):


    for i in range(2, x):
        if x % i == 0:
            print("False")
            break
        if i*i > x:
            print("True")
            break
is_prime(21)
is_prime(27)
is_prime(333)
is_prime(113)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
