import random;

def game():
    tictactoe = [0,0,0,0,0,0,0,0,0];
    
    turn = who_goes_first();
   
    for i in range(0,9):
        if(i%2==0):
            position = input('\nPosition you want to play in: ');
            tictactoe[position-1] = turn[0];
        else:
            print("\nComputer's Move: "+str(i+1))
            position = computer_move(tictactoe, turn[1], turn[0]);
            print('\n The position is: '+str(position));
            tictactoe[position] = turn[1]
            
        draw_grid(tictactoe);
        if(i>=2):
            winner = is_winner(tictactoe);
            if(winner == 1):
                break

def draw_grid(tictactoe):

    print('\n'+str(tictactoe[0])+'|'+ str(tictactoe[1])+'|'+ str(tictactoe[2]))
    print('_|_|_')
    print(str(tictactoe[3])+'|'+ str(tictactoe[4])+'|'+ str(tictactoe[5]))
    print('_|_|_')
    print(str(tictactoe[6])+'|'+ str(tictactoe[7])+'|'+ str(tictactoe[8]))

def computer_move(ttt, mac_char, player_char):
    
    if(ttt[0]==ttt[2]==mac_char) or (ttt[0]==ttt[2]==player_char):
        return 1;
    elif(ttt[0]==ttt[1]==mac_char) or (ttt[0]==ttt[1]==player_char):
        return 2;
    elif(ttt[1]==ttt[2]==mac_char) or (ttt[1]==ttt[2]==player_char):
        return 0;
    elif(ttt[3]==ttt[4]==mac_char) or (ttt[3]==ttt[4]==player_char):
        return 5;
    elif(ttt[3]==ttt[5]==player_char) or (ttt[3]==ttt[5]==mac_char):
        return 4;
    elif(ttt[4]==ttt[5]==mac_char) or (ttt[4]==ttt[5]==player_char):
        return 3;
    elif(ttt[6]==ttt[7]==mac_char) or (ttt[6]==ttt[7]==player_char):
        return 8;
    elif(ttt[7]==ttt[8]==player_char) or (ttt[7]==ttt[8]==mac_char):
        return 6;
    elif(ttt[6]==ttt[8]==mac_char) or (ttt[6]==ttt[8]==player_char):
        return 7;
    elif(ttt[0]==ttt[3]==mac_char) or (ttt[0]==ttt[3]==player_char):
        return 6;
    elif(ttt[0]==ttt[6]==player_char) or (ttt[0]==ttt[6]==mac_char):
        return 3;
    elif(ttt[3]==ttt[6]==mac_char) or (ttt[3]==ttt[6]==player_char):
        return 0;
    elif(ttt[1]==ttt[4]==mac_char) or (ttt[1]==ttt[4]==player_char):
        return 7;
    elif(ttt[1]==ttt[7]==player_char) or (ttt[1]==ttt[7]==mac_char):
        return 4;
    elif(ttt[4]==ttt[7]==mac_char) or (ttt[4]==ttt[7]==player_char):
        return 1;
    elif(ttt[2]==ttt[5]==mac_char) or (ttt[2]==ttt[5]==player_char):
        return 8;
    elif(ttt[2]==ttt[8]==player_char) or (ttt[2]==ttt[8]==mac_char):
        return 5;
    elif(ttt[5]==ttt[8]==mac_char) or (ttt[5]==ttt[8]==player_char):
        return 2;
    elif(ttt[0]==ttt[4]==mac_char) or (ttt[0]==ttt[4]==player_char):
        return 8;
    elif(ttt[0]==ttt[8]==player_char) or (ttt[0]==ttt[8]==mac_char):
        return 4;
    elif(ttt[4]==ttt[8]==mac_char) or (ttt[4]==ttt[8]==player_char):
        return 0;
    elif(ttt[2]==ttt[4]==mac_char) or (ttt[2]==ttt[4]==player_char):
        return 6;
    elif(ttt[2]==ttt[6]==player_char) or (ttt[2]==ttt[6]==mac_char):
        return 4;
    elif(ttt[4]==ttt[6]==mac_char) or (ttt[4]==ttt[6]==player_char):
        return 2;
    else:
        position = get_free_moves(ttt)
        return random.choice(position)
    
def get_free_moves(ttt):

    array = [];
    for i in range(0,9):
        if(ttt[i]==0):
            array.append(i);
    return array;

def who_goes_first():

    status = random.randint(0,1);

    if(status == 1):
        one = 'X'
        two = 'O'

    else:
        one = 'O'
        two = 'X'
        
    return one, two;

def is_winner(ttt):
    if((ttt[0]==ttt[1]==ttt[2]=='X') or
       (ttt[3]==ttt[4]==ttt[5]=='X') or
       (ttt[6]==ttt[7]==ttt[8]=='X') or
       (ttt[0]==ttt[3]==ttt[6]=='X') or
       (ttt[1]==ttt[4]==ttt[7]=='X') or
       (ttt[2]==ttt[5]==ttt[8]=='X') or
       (ttt[0]==ttt[4]==ttt[8]=='X') or
       (ttt[2]==ttt[4]==ttt[6]=='X')):
        print('X is the winner!');
        return 1
        

    elif ((ttt[0]==ttt[1]==ttt[2]=='O') or
       (ttt[3]==ttt[4]==ttt[5]=='O') or
       (ttt[6]==ttt[7]==ttt[8]=='O') or
       (ttt[0]==ttt[3]==ttt[6]=='O') or
       (ttt[1]==ttt[4]==ttt[7]=='O') or
       (ttt[2]==ttt[5]==ttt[8]=='O') or
       (ttt[0]==ttt[4]==ttt[8]=='O') or
       (ttt[2]==ttt[4]==ttt[6]=='O')):
        print('O is the winner!');
        return 1

    return 0
        
game()
