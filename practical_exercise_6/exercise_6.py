from sense_hat import SenseHat
import time

##Coding exercise 6a
def exercise_6a():
    sense = SenseHat()
    while True:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        yaw = sense.get_orientation()['yaw']
        print("pitch {0} roll {1} yaw {2}".format(round(pitch,0), round(roll,0), round(yaw,0)))
        time.sleep(0.05)
#exercise_6a()

## Coding exercise 6b
def exercise_6b():
    sense = SenseHat()
    b = (0,0,0)
    w = (255,255,255)
    board = [[b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b]]


    y = 2
    x = 2
    board[y][x] = w
    board_1D = sum(board, [])
    print(board_1D)
    sense.set_pixels(board_1D)

#exercise_6b()


def exercise_6c():

    def check_wall(x,y,new_x,new_y, board):
        if board[new_y][new_x] != r:
            return new_x, new_y
        elif board[new_y][x] != r:
            return x, new_y
        elif board[y][new_x] != r:
            return new_x, y
        else:
            return x,y

    def move_marble(pitch, roll, x, y, board):
        new_x = x
        new_y = y
        print(x,y)
        if 1 < pitch < 179 and x != 0:
            new_x -= 1
        elif 359 > pitch > 179 and x != 7:
            new_x += 1

        if 1 < roll < 179 and y != 7:
            new_y += 1
        elif 359 > roll > 179 and  y != 0:
            new_y -= 1
        
        return check_wall(x,y,new_x,new_y, board)
    
    sense = SenseHat()
    b = (0,0,0)
    w = (255,255,255)
    r = (255,0,0)
    g = (0,255,0)
    x = 2
    y = 2
    game_over = False

    while not game_over:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        yaw = sense.get_orientation()['yaw']
        board = [[b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b],
                 [b,b,b,b,b,b,b,b]]
        board = [[r,r,r,b,b,b,b,r],
                 [r,b,b,b,b,b,b,r],
                 [b,b,b,b,b,r,b,r],
                 [b,r,r,b,r,r,b,r],
                 [b,b,b,b,b,b,b,b],
                 [b,r,b,r,r,b,b,b],
                 [b,b,b,r,b,b,g,r],
                 [r,r,b,b,b,r,r,r]]
    
        x,y = move_marble(pitch, roll, x, y, board)
        if board[y][x] == g:
            sense.show_message("You won!")
            game_over = True
            return
        board[y][x] = w
        board_1D = sum(board, [])
        #print(board_1D)
        sense.set_pixels(board_1D)
        time.sleep(0.05)

exercise_6c()

