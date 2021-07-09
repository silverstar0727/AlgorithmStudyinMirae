N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(str, input())))

def count_(board):
    bcount = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'B':
                    bcount += 1
            else:
                if board[i][j] != 'W':
                    bcount += 1


    wcount = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'W':
                    wcount += 1
            else:
                if board[i][j] != 'B':
                    wcount += 1

    return min([bcount, wcount])


ans = []
for i in range(N-7):
    for j in range(M-7):
        board = arr[i : i+8][j : j+8]
        print(i, j)
        for k in range(8):
            print(board[k])
        ans.append(count_(board))
print(min(ans))
        
"""
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
"""