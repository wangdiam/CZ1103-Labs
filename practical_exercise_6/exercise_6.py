from sense_hat import SenseHat
import time

##Coding exercise 7a
def exercise_7a():
    sense = SenseHat()
    while True:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        yaw = sense.get_orientation()['yaw']
        print("pitch {0} roll {1} yaw {2}".format(round(pitch,0), round(roll,0), round(yaw,0)))
        time.sleep(0.05)
#exercise_7a()

## Coding exercise 7b
def exercise_7b():
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

#exercise_7b()

def exercise_7c():
    def move_marble(pitch, roll, x, y):
        new_x = x
        new_y = y
        if 1 < pitch < 179 and x != 0:
            new_x -= 1
        elif 359 > pitch > 179 and x != 7:
            new_x += 1

        if 1 < roll < 179 and y != 7:
            new_y += 1
        elif 359 > roll > 179 and  y != 0:
            new_y -= 1
        
        return new_x, new_y
    
    sense = SenseHat()
    b = (0,0,0)
    w = (255,255,255)


    while True:
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
        x,y = move_marble(pitch, roll, x, y)
        board[y][x] = w
        board_1D = sum(board, [])
        print(board_1D)
        sense.set_pixels(board_1D)
        time.sleep(0.05)

exercise_7c()
