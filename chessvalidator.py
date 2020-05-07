chess_board = {'1h': 'bpawn', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# bla poop
def name_check(chess_board):
    print('Executing name_check')
    correct_names_list = []
    wrong_names_list = []
    colour_list = ['b', 'w']
    pieces_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for i in colour_list:
        for m in range(len(pieces_list)):
            newElement = i + pieces_list[m]
            correct_names_list.append(newElement)

    for value in chess_board.values():
        if value not in correct_names_list:
            wrong_names_list.append(value)
            
    if not wrong_names_list:
        print('name_check True')
        return True
    else: 
        print(f"Piece names {', '.join(wrong_names_list)} are incorrect")
        print('name_check False')
        return False 

def total_amount_check(chess_board):
    print('Executing total_amount_check')
    b_counter = 0
    w_counter = 0
    max_amount = 16
    for value in chess_board.values():
        if value[0] == 'b':
            b_counter = b_counter + 1
        elif value[0] == 'w':
            w_counter = w_counter + 1

    if b_counter <= max_amount and w_counter <= max_amount:
        print('total_amount_check True')
        return True
    else:
        if b_counter > max_amount:
            print(f'Total amount {b_counter} of black pieces if more than {max_amount}')
            print('total_amount_check False')
            return False
        else:
            print(f'Total amount {w_counter} of white pieces if more than {max_amount}')
            print('total_amount_check False')
            return False
        
def pawns_check(chess_board):
    #TO DO: Refactor this function for general check.
    print('Executing pawns_check')
    bpawn_counter = 0
    wpawn_counter = 0
    max_pawn_amount = 8
    for value in chess_board.values():
        if value == 'bpawn':
            bpawn_counter = bpawn_counter + 1
        elif value == 'wpawn':
            wpawn_counter = wpawn_counter + 1
    #TO DO: Define error for no pawns situation.
    if bpawn_counter <= max_pawn_amount and wpawn_counter <= max_pawn_amount:
        print('pawns_check True')
        return True
    else:
        if bpawn_counter > max_pawn_amount:
            print(f'Total amount {bpawn_counter} of black pawns if more than {max_pawn_amount}')
            print('pawns_check False')
            return False
        else:
            print(f'Total amount {wpawn_counter} of white pawns if more than {max_pawn_amount}')
            print('pawns_check False')
            return False

def kings_check(chess_board):
    #TO DO: Refactor this function for general check.
    print('Executing kings_check')
    bking_counter = 0
    wking_counter = 0
    max_king_amount = 1
    for value in chess_board.values():
        if value == 'bking':
            bking_counter = bking_counter + 1
        elif value == 'wking':
            wking_counter = wking_counter + 1
    #TO DO: Define error from no kings situation.
    if bking_counter <= max_king_amount and wking_counter <= max_king_amount:
        print('kings_check True')
        return True
    else:
        if bking_counter > max_king_amount:
            print(f'Total amount {bking_counter} of black kings if more than {max_king_amount}')
            print('kings_check False')
            return False
        else:
            print(f'Total amount {wking_counter} of white kings if more than {max_king_amount}')
            print('kings_check False')
            return False

def board_check(chess_board):
    print('Executing board_check')
    axis_x = [1, 2, 3, 4, 5, 6, 7, 8]
    axis_y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    correct_board = []
    wrong_position_list = []
    for i in axis_x:
        for m in range(len(axis_y)):
            newElement = str(i) + axis_y[m]
            correct_board.append(newElement)
    
    for key in chess_board.keys():
        if key not in correct_board:
            wrong_position_list.append(key)

    if not wrong_position_list:
        print('board_check True')
        return True
    else:
        print(f"Position {', '.join(wrong_position_list)} is invalid")
        print('board_check False')
        return False

def is_valid_chess_board(chess_board):
    print('Executing is_valid_chess_board')
    name_check_result = name_check(chess_board)
    total_amount_check_result = total_amount_check(chess_board)
    pawns_check_result = pawns_check(chess_board)
    kings_check_result = kings_check(chess_board)
    board_check_result = board_check(chess_board)
    
    if name_check_result and total_amount_check_result and pawns_check_result and kings_check_result and board_check_result:
        print('Your board is valid')
        return True
    else:
        print('Your board is invalid')
        return False
 
print(str(is_valid_chess_board(chess_board))) 
