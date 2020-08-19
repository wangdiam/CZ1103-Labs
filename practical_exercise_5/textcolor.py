from sense_hat import SenseHat
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

