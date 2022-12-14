def getWinner (filename):
    print("학번: 202126327, 이름: 조은산")
    # 텍스트파일 불러오기 & 리스트로 형태 변환
    with open(filename) as file:
        list_file = []
        lines = file.readlines()
        # , 제거
        list_file2 = []
        for new_line in lines:
            lines_del = new_line.replace(",", "")
            list_file2.append(lines_del)
        for line in list_file2:
            list_file.append(line.strip().split())
    #print(list_file)

    # 3X3판 만들기
    board = [["" for x in range(3)] for y in range(3)]
    #print(board)

    # 게임 시작
    count = 0 # 횟수 정의
    ox_list=[]
    for who in [i[0] for i in list_file]:
        # 텍스트 파일 적합성 판단
        ox_list.append(who)
        if (count >= 1):
            if (ox_list[count] == ox_list[count-1]):
                print("-")
                break
        if ((list_file[count][0] == 'O') or (list_file[count][0] =='X')) and (len(list_file[count]) == 3):
            x = list_file[count][1]
            y = list_file[count][2]
            # 패가 들어있는지 확인
            if board[int(x)-1][int(y)-1] != '':
                print("-")
                break
            else:
                if who == 'O':
                    board[int(x)-1][int(y)-1] = 'O'
                else:
                    board[int(x)-1][int(y)-1] = 'X'
            count += 1
            if (count == len(list_file)): # 입력 길이만큼 loop
                break
            elif count >= 10: # 횟수 넘기면 무승부
                print("-")
        else:
            print("-")
            break


    # 승리 판별
    if (board[0][0] == board[0][1] == board[0][2] == 'O' or
            board[1][0] == board[1][1] == board[1][2] == 'O' or
            board[2][0] == board[2][1] == board[2][2] == 'O' or
            board[0][0] == board[1][0] == board[2][0] == 'O' or
            board[0][1] == board[1][1] == board[2][1] == 'O' or
            board[0][2] == board[1][2] == board[2][2] == 'O' or
            board[0][0] == board[1][1] == board[2][2] == 'O' or
            board[0][2] == board[1][1] == board[2][0] == 'O'):
            print("Congratulation! The WINNER is O")
    elif (board[0][0] == board[0][1] == board[0][2] == 'X' or
            board[1][0] == board[1][1] == board[1][2] == 'X' or
            board[2][0] == board[2][1] == board[2][2] == 'X' or
            board[0][0] == board[1][0] == board[2][0] == 'X' or
            board[0][1] == board[1][1] == board[2][1] == 'X' or
            board[0][2] == board[1][2] == board[2][2] == 'X' or
            board[0][0] == board[1][1] == board[2][2] == 'X' or
            board[0][2] == board[1][1] == board[2][0] == 'X'):
            print("Congratulation! The WINNER is X")

# 함수 호출
getWinner('tictactoe.txt')