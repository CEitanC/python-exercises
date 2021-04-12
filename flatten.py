def flatten(x):
    my_list=[]
    for i in range(len(x)):
        if isinstance(x[i], int) == True:
            my_list.append(x[i])
        else:
            my_sub_list= sub_list(x[i])
            for j in range(len(my_sub_list)):
                 my_list.append(my_sub_list[j])
    print(my_list)

def sub_list(y):
    if isinstance(y[0],int)==True:
        return y;
    else:
        return sub_list(y[0])

flatten([])
flatten([0, 1, [2, 3], 4, [5, 6]])
flatten([0, [[[1]]], [[2, 3], [4, [[5, 6]]]]])
