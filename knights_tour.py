import copy
def find_path(m,n):
    board =[[0 for a in range(n)] for b in range(m)]
    path_=[]
    new_path=make_step(board,m,n,0,0,0,path_)
    if(new_path==True):
        tuple_p=tuple(path_)
        print(tuple_p)
        return (path_)
    else:
        print("None")
        return None


def make_step(board,m,n,x,y,step_num,path):
    # check valid
    if (x<0)or(x>=m)or(y<0)or(y>=n):
        return False
    #has ivsited?
    if(board[x][y]==1):
        return  False
    step_num+=1
    board[x][y]=1
    path.append((x,y))
    if step_num == m * n:
        return True
    ##find the next point
    row_op=[-2,-2,-1,-1,1,1,2,2]
    col_op=[-1,1,-2,2,-2,2,-1,1]
    for i in range(8):
       if make_step(board,m,n,x+row_op[i],y+col_op[i],step_num,path)==True:
           return True
    step_num-=1
    board[x][y]=0
    path.remove((x,y))

    return False

def fill_board(m,n,path):
    board = [[0 for a in range(n)] for b in range(m)]

    for i in range(m*n):
        x=path[i][0]
        y=path[i][1]
        board[x][y]=i

    print(board)






path =find_path(5,5)
fill_board(5,5,path)

