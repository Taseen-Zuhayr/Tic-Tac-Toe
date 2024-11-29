print("Welcome to the Tic Tac Toe game.")
the_board = {

'7': ' ', '8': ' ', '9': ' ',

'4': ' ', '5': ' ', '6': ' ',

'3': ' ', '2': ' ', '1': ' '

}

board_keys = []
for key in the_board:
    board_keys.append(key)

def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print("-+-+-")
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print("-+-+-")
    print(board['3']+'|'+board['2']+'|'+board['1'])
    print("-+-+-")

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printboard(the_board)
        print("It's your turn,"+ turn +"Move to which place?")
        move = input()
        if the_board[move]==' ':
            the_board[move]=turn
            count += 1
        else:
            print("That place is already filled. \nMove to which place?")
            continue
        if count>=5:
            if the_board['7']==the_board['8']==the_board['9']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['4']==the_board['5']==the_board['6']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['3']==the_board['2']==the_board['1']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['1']==the_board['4']==the_board['7']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['2']==the_board['5']==the_board['8']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['3']==the_board['6']==the_board['9']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['7']==the_board['5']==the_board['3']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
            elif the_board['1']==the_board['5']==the_board['9']!=' ':
                printboard(the_board)
                print("\nGame Over.\n")
                print("****"+ turn +"Won. ****")
                break
        if count==9:
            print("\nGame Over\n")
            print("It's a Tie!!!")

        if turn=='X':
            turn='O'
        else:
            turn='X'
    restart = input("Do you want to play again?(y/n)")
    if restart=='y' or restart=='Y':
        for key in board_keys:
            the_board[key]=' '
        game()
if __name__=="__main__":
    game()








