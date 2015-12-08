number = input()
if number < 0: goto negative
if number % 2 == 0:
   print "even"
else:
   print "odd"
goto end
label: negative
print "negative"
label: end
print "all done"def computer_move():
    mac_char = 'X'
    player_char = 'O'
    n=3
    ttt = ['X', 0, 0, 0, 0, 0, 0, 0, 'X']
    if(n<=2):
        position = 0
        return random.choice(position)

    elif((ttt[0]==ttt[2]==(mac_char or player_char)) or
         (ttt[0]==ttt[1]==(mac_char or player_char)) or
         (ttt[1]==ttt[2]==(mac_char or player_char))):
        for j in range(0,3):
            if(ttt[j]==0):
                print j

    elif((ttt[3]==ttt[4]==(mac_char or player_char)) or
         (ttt[3]==ttt[5]==(mac_char or player_char)) or
         (ttt[4]==ttt[5]==(mac_char or player_char))):
        for j in range(3,6):
            if(ttt[j]==0):
                print j

    elif((ttt[6]==ttt[7]==(mac_char or player_char)) or
         (ttt[7]==ttt[8]==(mac_char or player_char)) or
         (ttt[6]==ttt[8]==(mac_char or player_char))):
        for j in range(6,9):
            if(ttt[j]==0):
                print j

    elif((ttt[0]==ttt[3]==(mac_char or player_char)) or
         (ttt[3]==ttt[6]==(mac_char or player_char)) or
         (ttt[0]==ttt[6]==(mac_char or player_char))):
        for j in range(0,7,3):
            if(ttt[j]==0):
                print j

    elif((ttt[1]==ttt[4]==(mac_char or player_char)) or
         (ttt[4]==ttt[7]==(mac_char or player_char)) or
         (ttt[1]==ttt[7]==(mac_char or player_char))):
        for j in range(1,8,3):
            if(ttt[j]==0):
                print j

    elif((ttt[5]==ttt[2]==(mac_char or player_char)) or
         (ttt[2]==ttt[8]==(mac_char or player_char)) or
         (ttt[5]==ttt[8]==(mac_char or player_char))):
        for j in range(2,9,3):
            if(ttt[j]==0):
                print j

    elif((ttt[0]==ttt[4]==(mac_char or player_char)) or
         (ttt[0]==ttt[8]==(mac_char or player_char)) or
         (ttt[4]==ttt[8]==(mac_char or player_char))):
        for j in range(0,9,4):
            if(ttt[j]==0):
                print j

    elif((ttt[4]==ttt[2]==(mac_char or player_char)) or
         (ttt[4]==ttt[6]==(mac_char or player_char)) or
         (ttt[2]==ttt[6]==(mac_char or player_char))):
        for j in range(2,7,4):
            if(ttt[j]==0):
                print j

computer_move()
