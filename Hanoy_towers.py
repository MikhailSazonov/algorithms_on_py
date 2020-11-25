def move(current_height, column_num, where_move):
    if current_height == 1:
        print(current_height, column_num, where_move)
    else:
        move(current_height - 1, column_num, 6 - where_move - column_num)
        print(current_height, column_num, where_move)
        move(current_height - 1, 6 - where_move - column_num, where_move)


n = int(input())
move(n, 1, 3)
