import copy
ALIVE = 1
DEAD = 0


def game_of_life(board, steps):

    rows = len(board)
    cols= len(board[0])
    next_board= copy.deepcopy(board)
    for s in range(steps):
        for i in range(rows):
            for j in range(cols):
                sum =0
                #a[i-1][j-1]
                if (((i-1)>=0)and(i-1<rows))and((j-1>=0)and(j-1<cols)):
                    sum+=board[i-1][j-1]
                if (((i - 1) >= 0) and (i - 1 < rows)) and ((j  >= 0) and (j  < cols)):
                    sum += board[i - 1][j ]
                if (((i - 1) >= 0) and (i - 1 < rows)) and ((j + 1 >= 0) and (j + 1 < cols)):
                    sum += board[i - 1][j + 1]
                if (((i ) >= 0) and (i  < rows)) and ((j - 1 >= 0) and (j - 1 < cols)):
                    sum += board[i ][j - 1]
                if (((i ) >= 0) and (i  < rows)) and ((j + 1 >= 0) and (j + 1 < cols)):
                    sum += board[i ][j + 1]
                if (((i + 1) >= 0) and (i + 1 < rows)) and ((j - 1 >= 0) and (j - 1 < cols)):
                    sum += board[i + 1][j - 1]
                if (((i + 1) >= 0) and (i + 1 < rows)) and ((j  >= 0) and (j  < cols)):
                    sum += board[i +1][j]
                if (((i + 1) >= 0) and (i + 1 < rows)) and ((j + 1 >= 0) and (j + 1 < cols)):
                    sum += board[i +1][j + 1]

                if board[i][j]==ALIVE:
                    if (sum<2)or(sum>3):
                        next_board[i][j]= DEAD
                else:
                    if sum==3:
                        next_board[i][j]=ALIVE

        board=copy.deepcopy(next_board)


    print(board)




initial_board = [

[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],

[DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],

[DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],

[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],

[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],

]

game_of_life(initial_board, 1)
