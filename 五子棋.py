board = [[' ']*15 for i in range(15)]
for i in board:
    print(i)
def insert(x, y, z):
    if board[x][y] != ' ':
        print("该位置已被占用")
        return 1
    else:
        board[x][y] = z
        for i in board:
            print(i)
        return 0


def judge(board):
    for j in board:
        if  ''.join(j).find('B'*5)!=-1:
            print("黑棋获胜")
            return 0
        elif ''.join(j).find('W'*5)!=-1:
            print("白棋获胜")
            return 1
    else:
        return -1

def check_win(board):
    board_b=[l for l in zip(*board)]
    board_c = [[] for i in range(29)]
    for i in range(15):
        for j in range(15):
            board_c[i-j].append(board[i][j])
    board_d = [[] for i in range(29)]
    for i in range(15):
        for j in range(15):
            board_d[i+j].append(board[i][j])
    return [judge(board),judge(l for l in zip(*board)),judge(board_c),judge(board_d)]


flag=0
while True:
    if flag==0:
        print("黑棋回合")
        while True:
            try:
                x=int(input("输入横坐标:"))
                if x<0 or x>14:
                    print("输入错误")
                    continue
                else:
                    break
            except:
                print("输入格式错误")
        while True:
            try:
                y = int(input("输入纵坐标:"))
                if y < 0 or y > 14:
                    print("输入错误")
                    continue
                else:
                    break
            except:
                print("输入格式错误")
        if insert(x,y,'B'):
            flag=0
            continue
        flag=1
    if 0 or 1 in check_win(board):
        break
    else:
        print("白棋回合")
        while True:
            try:
                x = int(input("输入横坐标:"))
                if x < 0 or x > 14:
                    print("input error")
                    continue
                else:
                    break
            except:
                print("输入格式错误")
        while True:
            try:
                y = int(input("输入纵坐标:"))
                if y < 0 or y > 14:
                    print("input error")
                    continue
                else:
                    break
            except:
                print("输入格式错误")
        if insert(x, y, 'W'):
            flag = 1
            continue
        flag = 0
    if 0 or 1 in check_win(board):
        break