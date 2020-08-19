from sense_hat import SenseHat

## Exercise 6a##
def get_color(color):
    keep_looping = True
    no_of_try = 0
    while keep_looping:
        color_str = input("Enter the value of the " + color + " color for message (0 to 255):")
        if color_str != '' and not color_str.isalpha() and 0 <= int(color_str) <= 255:
            return int(color_str)
        no_of_try += 1
        if no_of_try == 3:
            return 0

r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")

msg_color = (r_int, g_int, b_int)
sense = SenseHat()
sense.show_message("I got it!", text_colour=msg_color)

##Exercise 6b##
from textcolor import get_color

r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")

msg_color = (r_int, g_int, b_int)
sense = SenseHat()
sense.show_message("I got it!", text_colour=msg_color)
