import players;

def choose_players():

    print("1 player game or 2 player game?");
    input(players);

    if(players != 1 || players != 2)
        print("Invalid Input!");

    return players;

def choose_character():

    players = choose_players();
    
    if(players == 1):
        print("Choose your character: X or O");
        input(character)

        if(character != 'X' ||
           character != 'x' ||
           character != 'O' ||
           character != 'o'):
            print("Invalid Input!");

        player1 = players.Players('player', character);

        if(character == 'X' || character == 'x'):
            machine = players.Players('machine', 'O');
            game1(player1, machine)
        else:
            machine = players.Players('machine', 'X');
            game1(player1, machine)
        
    else:
        print("1st player will choose its character: X or O");
        input(character1);
        
        if(character1 != 'X' ||
           character1 != 'x' ||
           character1 != 'O' ||
           character1 != 'o'):
            print("Invalid Input!");

        else if(character1 == 'X' || character1 == 'x'):
            player1 = players.Players('player1', 'X');
            player2 = players.Players('player2', 'O');
            game2(player1, player2)
            
        else:
            player1 = players.Players('player1', 'O');
            player2 = players.Players('player2', 'X');
            game2(player1, player2)


def who_goes_first(player1, player2):
    turn = random.randint(0, 1);
    return turn;
    
def game1(player1, machine):
    
    print('Our Board');
    print('---------');
    print(' ');
    print(' ');
    print('_1_|_2_|_3_');
    print('_4_|_5_|_6_');
    print(' 7 | 8 | 9 ');
    print(' ');
    print(' ');

    t = who_goes_first(player1, machine);
    temp = players.Players();

    if (t==0):
        temp = player1;
        player1 = machine;
        machine = temp;
    
    tries = 0;
    tictactoe = [0,0,0,0,0,0,0,0,0]

    for tries in range(1,9):

        if(tries%2 != 0):
            print('What position will you want to play in?');
            input(position);
            if(tictactoe[position-1] == 0):
                tictactoe[position-1] = character;
                tries+=1;
                print_board(tictactoe);
            else:
                print('Position is already occupied');
        else:
            computer_move(tries, tictactoe, player1, player2);
    isWinner(tictactoe, );
    
def get_possible_moves(ttt):
    moves = [];
    for i in ttt:
        if(ttt[i] == 0):
            moves.append(i);

    return moves;

def computer_move(tries, ttt, p1, p2):

    t = who_goes_first(player1, player2);
    temp = players.Players();

    if (t==0):
        temp = player1;
        player1 = player2;
        player2 = temp;

    if(player1.label == 'Machine'):
        machine_char = player1.char;

    else:
        machine_char = player2.char;
        
    if(tries <= 3):
        random.choice(get_possible_moves(ttt));
    
    else:
        for i in ttt:   
            if(ttt[i] == 0):
                if(ttt[i-1] == ttt[i+1] == machine_char ||
                   ttt[i-3] == ttt[i+3] == machine_char ):
                       ttt[i] = machine_char;
                       tries+=1;
                else if (i == 4):
                    if(ttt[i-2] == ttt[i+2] == machine_char ||
                       ttt[i-4] == ttt[i+4] == machine_char):
                        ttt[4] = machine_char;
                        tries+=1;
                if(ttt[i-1] == ttt[i+1] == player_char ||
                   ttt[i-3] == ttt[i+3] == player_char ):
                       ttt[i] = machine_char;
                       tries+=1;
                else if (i == 4):
                    if(ttt[i-2] == ttt[i+2] == player_char ||
                       ttt[i-4] == ttt[i+4] == player_char):
                        ttt[4] = machine_char;
                        tries+=1;

def game2(turn1, turn2, position, ):
    print('We are in game 2!');

def isWinner(ttt):

        if((ttt[0] == ttt[1] == ttt[2] == machine_char) or
           (ttt[3] == ttt[4] == ttt[5] == machine_char) or
           (ttt[6] == ttt[7] == ttt[8] == machine_char) or
           (ttt[0] == ttt[3] == ttt[6] == machine_char) or
           (ttt[1] == ttt[4] == ttt[7] == machine_char) or
           (ttt[2] == ttt[5] == ttt[8] == machine_char) or
           (ttt[0] == ttt[4] == ttt[8] == machine_char) or
           (ttt[2] == ttt[6] == ttt[4] == machine_char)):
            print('Machine has won');
            
        if ((ttt[0] == ttt[1] == ttt[2] == player_char) or
           (ttt[3] == ttt[4] == ttt[5] == player_char) or
           (ttt[6] == ttt[7] == ttt[8] == player_char) or
           (ttt[0] == ttt[3] == ttt[6] == player_char) or
           (ttt[1] == ttt[4] == ttt[7] == player_char) or
           (ttt[2] == ttt[5] == ttt[8] == player_char) or
           (ttt[0] == ttt[4] == ttt[8] == player_char) or
           (ttt[2] == ttt[6] == ttt[4] == player_char)):
            print('Player has won');
