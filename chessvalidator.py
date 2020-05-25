#! python3
# chessvalidator - checks if provided chess board is valid

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# TODO: add validation that no cells appear more than 1 time
chess_board = {'1h': 'bpawn', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3f': ''}

# Dictionary with invalid items for testing
invalid_items = {'10z': '', '': 'wking', '2a': 'zpawn', '3a': 'zqueen'}
chess_board.update(invalid_items)

def names_check(chess_board):
    logging.info('Executing NAMES_CHECK')
    colour_list = ['b', 'w']
    pieces_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    correct_names_list = []
    wrong_names_list = []
    
    axis_x = [1, 2, 3, 4, 5, 6, 7, 8]
    axis_y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    correct_board = []
    wrong_position_list = []

    # Setting list of possible chess pieces
    for i in colour_list:
        for m in range(len(pieces_list)):
            newElement = i + pieces_list[m]
            correct_names_list.append(newElement)
    # Setting list of possible positions
    for i in axis_x:
        for m in range(len(axis_y)):
            newElement = str(i) + axis_y[m]
            correct_board.append(newElement)

    for key, value in chess_board.items():
        # Checking if possition is correct
        if key not in correct_board:
            if key == '':
                wrong_position_list.append('blank field')
            else:
                wrong_position_list.append(key)
        # Checking if piece name is correct
        if value != '':
            if value not in correct_names_list:
                wrong_names_list.append(value)

    # Error messages
    if wrong_names_list:
        logging.debug('piece_name_check False')
        print(f"Piece names {', '.join(wrong_names_list)} are incorrect")
    else:
        logging.info('piece_name_check True')
    if wrong_position_list:
        logging.debug('board_check False')
        print(f"Positions {', '.join(wrong_position_list)} are invalid")
    else:
        logging.info('board_check True')

    # Final output of function
    if not wrong_names_list and not wrong_position_list:
        logging.info('NAMES_CHECK is True')
        return True
    else:
        logging.debug('NAMES_CHECK is False')
        return False
    

def amounts_check(chess_board):
    logging.info('Executing AMOUNTS_CHECK')
    b_counter = 0
    w_counter = 0
    max_amount = 1 #16
    bpawn_counter = 0
    wpawn_counter = 0
    max_pawn_amount = 1 #8
    bking_counter = 0
    wking_counter = 0
    max_king_amount = 1
    
    # if value != '':
    for value in chess_board.values():
        if value != '':
            if value[0] == 'b':
                b_counter = b_counter + 1
            elif value[0] == 'w':
                w_counter = w_counter + 1
            if value == 'bpawn':
                bpawn_counter = bpawn_counter + 1
            elif value == 'wpawn':
                wpawn_counter = wpawn_counter + 1
            if value == 'bking':
                bking_counter = bking_counter + 1
            elif value == 'wking':
                wking_counter = wking_counter + 1

    if b_counter <= max_amount and w_counter <= max_amount:
        logging.info('total_amount_check True')
    else:
        if b_counter > max_amount:
            logging.debug('total_amount_check False')
            print(f'Total amount {b_counter} of black pieces if more than {max_amount}')
        else:
            logging.debug('total_amount_check False')
            print(f'Total amount {w_counter} of white pieces if more than {max_amount}')

    if bpawn_counter <= max_pawn_amount and wpawn_counter <= max_pawn_amount:
        logging.info('pawns_check True')
    else:
        if bpawn_counter > max_pawn_amount:
            logging.debug('pawns_check False')
            print(f'Total amount {bpawn_counter} of black pawns if more than {max_pawn_amount}')
        else:
            logging.debug('pawns_check False')
            print(f'Total amount {wpawn_counter} of white pawns if more than {max_pawn_amount}')

    if bking_counter <= max_king_amount and wking_counter <= max_king_amount:
        logging.info('kings_check True')
    else:
        if bking_counter > max_king_amount:
            logging.debug('kings_check False')
            print(f'Total amount {bking_counter} of black kings if more than {max_king_amount}')
        else:
            logging.debug('kings_check False')
            print(f'Total amount {wking_counter} of white kings if more than {max_king_amount}')

    if b_counter <= max_amount and w_counter <= max_amount and bpawn_counter <= max_pawn_amount and wpawn_counter <= max_pawn_amount\
        and bking_counter <= max_king_amount and wking_counter <= max_king_amount:
        logging.info('AMOUNTS_CHECK is True')
        return True
    else:
        logging.info('AMOUNT_CHECK is False')
        return False
    

def is_valid_chess_board(chess_board):
    logging.info('Executing IS_VALID_CHESS_BOARD')
    names_check_result = names_check(chess_board)
    amounts_check_result = amounts_check(chess_board)
    
    if names_check_result and amounts_check_result:
        print('Your board is valid')
        return True
    else:
        print('Your board is invalid')
        return False
    
logging.disable(logging.CRITICAL)

print(str(is_valid_chess_board(chess_board)))