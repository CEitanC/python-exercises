def is_perfect_num(num):
    sum=1
    for i in range(2, num-1):
        if sum>num:
            break
        if num%i==0:
            sum+=i
    if sum==num:
        print("True")
    else:
        print("False")



is_perfect_num(6)
is_perfect_num(35)