import time, random
from sense_hat import SenseHat
def light_up_four_corners():
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    sense = SenseHat()
    sense.set_pixel(0,0,red)
    sense.set_pixel(0,7,green)
    sense.set_pixel(7,7,blue)
    sense.set_pixel(7,0,yellow)
    time.sleep(1)
    sense.clear()

light_up_four_corners()

def random_display():
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    sense = SenseHat()
    sense.set_pixel(random.randint(0,7),random.randint(0,7),red)
    sense.set_pixel(random.randint(0,7),random.randint(0,7),green)
    sense.set_pixel(random.randint(0,7),random.randint(0,7),blue)
    sense.set_pixel(random.randint(0,7),random.randint(0,7),yellow)
    time.sleep(1)
    sense.clear()

random_display()

def display_image():
    sense = SenseHat()
    count = 0
    orientation = [0,90,180,270]
    while True:
        y = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        b = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        image_pixels = [b, b, b, b, b, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, y, y, y, y, b, b,
                b, y, y, y, y, y, y, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b]
        sense.set_pixels(image_pixels)
        sense.set_rotation(orientation[random.randint(0,3)])
        time.sleep(1)
        sense.clear()
        count += 1

#display_image()

def accelerometer_game():
    sense = SenseHat()
    sense.clear()
    arrow_orientations = [0,90,180,270]
    y = (0,255,0)
    b = (255,0,0) 
    image_pixels = [b, b, b, b, b, b, b, b,
            b, b, b, y, y, b, b, b,
            b, b, y, y, y, y, b, b,
            b, y, y, y, y, y, y, b,
            b, b, b, y, y, b, b, b,
            b, b, b, y, y, b, b, b,
            b, b, b, y, y, b, b, b,
            b, b, b, y, y, b, b, b]
    won_count = 0
    while True:
        orientation = arrow_orientations[random.randint(0,3)]
        sense.set_rotation(orientation)
        sense.set_pixels(image_pixels)
        current_time = time.time()
        won = False
        while time.time() - current_time < 1:
            acceleration = sense.get_accelerometer_raw()
            if orientation == 0:
                if acceleration['y'] > 0.9:
                    sense.set_pixels([(0,255,0) for i in range(64)])
                    won = True
                    time.sleep(1)
            elif orientation == 180:
                if acceleration['y'] < -0.9:
                    sense.set_pixels([(0,255,0) for i in range(64)])
                    won = True
                    time.sleep(1)
            elif orientation == 90:
                if acceleration['x'] < -0.9:
                    sense.set_pixels([(0,255,0) for i in range(64)])
                    won = True
                    time.sleep(1)
            elif orientation == 270:
                if acceleration['x'] > 0.9:
                    sense.set_pixels([(0,255,0) for i in range(64)])
                    won = True
                    time.sleep(1)
        if not won:
            sense.set_pixels([(255,0,0) for i in range(64)])
            time.sleep(1)
            sense.clear()
            sense.show_message("You won " + str(won_count) + " time(s)!", scroll_speed=0.04)
            time.sleep(2)
            sense.clear()
            break
        if won:
            won_count += 1
        time.sleep(1)
        sense.clear()
        time.sleep(1)
#accelerometer_game()
