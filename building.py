import random;

def game():
    tictactoe = [' ',' ',' ',' ',' ',' ',' ',' ',' '];

    turn = who_goes_first();

    for i in range(0,9):
        if(i%2==0):
            player_move(tictactoe, turn[0])
        else:
            position = computer_move(tictactoe, turn[1], turn[0]);
            print("\nComputer's Move: "+str(position+1));
            #print('\n The position is: '+str(position));
            tictactoe[position] = turn[1]

        draw_grid(tictactoe);
        if(i>=2):
            winner = is_winner(tictactoe);
            if(winner == 1):
                choice = raw_input('Do you want to play another game? ');
                choice.lower();
                if(choice == 'yes'):
                    game();
                else:
                    break

def draw_grid(tictactoe):

    print('\n'+str(tictactoe[0])+'|'+ str(tictactoe[1])+'|'+ str(tictactoe[2]))
    print('_|_|_')
    print(str(tictactoe[3])+'|'+ str(tictactoe[4])+'|'+ str(tictactoe[5]))
    print('_|_|_')
    print(str(tictactoe[6])+'|'+ str(tictactoe[7])+'|'+ str(tictactoe[8]))

def player_move(ttt, char):
    
    position = input('\nPosition you want to play in: ');
    if ttt[position-1] == ' ':
        ttt[position-1] = char;
    else:
        print('Position is already occupied!');
        player_move(ttt, char);
                
def computer_move(ttt, mac_char, player_char):

    mwm = []
    mwm = calculate_move(ttt, mac_char);
    pwm = make_move(ttt, player_char);
    if(mwm != []):
        position = mwm;
    else:
        position = pwm;

    #print('\nPosition: '+str(position));
    return position;

def calculate_move(ttt, char):

    position = [];
    pos = [];
    array = [];

    if ttt[0]==ttt[2]==char:
        pos.append(1);
    if ttt[0]==ttt[1]==char:
        pos.append(2);
    if ttt[1]==ttt[2]==char:
        pos.append(0);

    if ttt[3]==ttt[4]==char:
        pos.append(5);
    if ttt[3]==ttt[5]==char:
        pos.append(4);
    if ttt[4]==ttt[5]==char:
        pos.append(3);

    if ttt[6]==ttt[7]==char:
        pos.append(8);
    if ttt[7]==ttt[8]==char:
        pos.append(6);
    if ttt[6]==ttt[8]==char:
        pos.append(7);

    if ttt[0]==ttt[3]==char:
        pos.append(6);
    if ttt[0]==ttt[6]==char:
        pos.append(3);
    if ttt[3]==ttt[6]==char:
        pos.append(0);

    if ttt[1]==ttt[4]==char:
        pos.append(7);
    if ttt[1]==ttt[7]==char:
        pos.append(4);
    if ttt[4]==ttt[7]==char:
        pos.append(1);

    if ttt[2]==ttt[5]==char:
        pos.append(8);
    if ttt[2]==ttt[8]==char:
        pos.append(5);
    if ttt[5]==ttt[8]==char:
        pos.append(2);

    if ttt[0]==ttt[4]==char:
        pos.append(8);
    if ttt[0]==ttt[8]==char:
        pos.append(4);
    if ttt[4]==ttt[8]==char:
        pos.append(0);

    if ttt[2]==ttt[4]==char:
        pos.append(6);
    if ttt[2]==ttt[6]==char:
        pos.append(4);
    if ttt[4]==ttt[6]==char:
        pos.append(2);

    l = len(pos);
    if(pos):
        #print('\nPoses: '+str(pos));
        for i in range(l):
            if ttt[pos[i]] == ' ':
                array.append(pos[i])

        position = random.choice(array);

    #print('\nMachine winning move: '+str(position));
    return position;


def make_move(ttt, player_char):
    pos = [];
    position = [];
    pos = calculate_move(ttt, player_char);

    if(pos != []):
        position = pos;
    else:
        positions = get_free_moves(ttt);
        position = random.choice(positions);

    #print("\nPlayer's winning move: "+str(position));
    return position;

    
def get_free_moves(ttt):

    array = [];
    for i in range(0,9):
        if(ttt[i]==' '):
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
