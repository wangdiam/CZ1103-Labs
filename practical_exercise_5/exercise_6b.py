from sense_hat import SenseHat
##Exercise 6b##
from textcolor import get_color

r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")

msg_color = (r_int, g_int, b_int)
sense = SenseHat()
sense.show_message("I got it!", text_colour=msg_color)
