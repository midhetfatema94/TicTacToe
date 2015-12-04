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
            player2 = players.Players('machine', 'O');
        else:
            player2 = players.Players('machine', 'X');
        
    else if (players == 2):
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
            
        else:
            player1 = players.Players('player1', 'O');
            player2 = players.Players('player2', 'X');

    play_game(player1, player2, players)


def play_game(p1, p2, n):

    if (n == 1):
        game1(p1, p2);

    else:
        game2(turn1, turn2);


def who_goes_first(player1, player2):
    turn = random.randint(0, 1);
    return turn;
    
def game1(player1, player2):
    
    print('Our Board');
    print('---------');
    print(' ');
    print(' ');
    print('_1_|_2_|_3_');
    print('_4_|_5_|_6_');
    print(' 7 | 8 | 9 ');
    print(' ');
    print(' ');

    t = who_goes_first(player1, player2);
    temp = players.Players();

    if (t==0):
        temp = player1;
        player1 = player2;
        player2 = temp;
    
    tries = 0;
    tictactoe = [0,0,0,0,0,0,0,0]

    for tries in range(0,8):

        if(tries%2 == 0):
            print('What position will you want to play in?');
            input(position);
            if(tictactoe[position-1] == 0):
                tictactoe[position-1] = character;
                tries+=1;
                print_board(tictactoe);
            else:
                print('Position is already occupied');
        else:
            computer_move(tries, tictactoe, character);

def computer_move(tries, ttt, player_char):

    if(player_char == 'X' || player_char == 'x'):
        machine_char == 'O';
    else:
        machine_char == 'X';

    if(moves <= 2):

        if(ttt[4] == 0):
            ttt[4] = machine_char;
            moves+=1;

        else if(ttt[0] == 0):
            ttt[0] = machine_char;
            moves+=1;

        else if(ttt[6] == 0):
            ttt[6] = machine_char;
            moves+=1;

        else if(ttt[8] == 0):
            ttt[8] = machine_char;
            moves+=1;
    else:

        for i in ttt:
            
            if(ttt[i] == 0):
                if(ttt[i-1] == ttt[i+1] == machine_char ||
                   ttt[i-3] == ttt[i+3] == machine_char ):
                       ttt[i] = machine_char;

                else if (i == 4):
                    if(ttt[i-2] == ttt[i+2] == machine_char ||
                       ttt[i-4] == ttt[i+4] == machine_char):
                        ttt[4] = machine_char;

                if(ttt[i-1] == ttt[i+1] == player_char ||
                   ttt[i-3] == ttt[i+3] == player_char ):
                       ttt[i] = machine_char;

                else if (i == 4):
                    if(ttt[i-2] == ttt[i+2] == player_char ||
                       ttt[i-4] == ttt[i+4] == player_char):
                        ttt[4] = machine_char;

def game2(turn1, turn2, position, ):

    for i in range(0,8):
        if(i%2 == 0):
            print('Choose your move '+turn1+' :');
                input(
