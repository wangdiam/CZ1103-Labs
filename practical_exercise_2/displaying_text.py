from sense_hat import SenseHat

input_string = ""
red_input = "-1"
green_input = "-1"
blue_input = "-1"
red_background_input = "-1"
green_background_input = "-1"
blue_background_input = "-1"
rotation_input = "-1"
scroll_speed_input = "-1"
background_done = False

def validate_color_input(inpt):
    return inpt != '' and not inpt.isalpha() and 0 <= int(inpt) <= 255
def validate_rotation_input(inpt):
    return inpt != '' and not inpt.isalpha() and (int(inpt) in [0, 90, 180, 270])
def validate_scroll_speed_input(inpt):
    return inpt != '' and not inpt.isalpha() and float(inpt) > 0
def user_input_limit_check(string):
    for i in range(3):
        inpt = input(string)
        if validate_color_input(inpt):
            return inpt
    print("You have reached the maximum number of attempts. The program will now end.")
    return None
print("Welcome to SenseHat!")
while True:
    quit = input("To quit, enter 'q'. Enter anything else to continue: ")
    if quit == 'q':
        break
    input_string = input("Enter your message: ")
    red_input = user_input_limit_check("Enter red value of text (range from 0-255): ")
    if red_input == None:
        break
    green_input = user_input_limit_check("Enter green value of text (range from 0-255): ")
    if green_input == None:
        break
    blue_input = user_input_limit_check("Enter blue value of text (range from 0-255): ")
    if blue_input == None:
        break
    while not background_done:
        red_backgroud_input = user_input_limit_check("Enter red value of background (range from 0-255): ")
        if red_input == None:
            break
        green_background_input = user_input_limit_check("Enter green value of background (range from 0-255): ")
        if green_input == None:
            break
        blue_background_input = user_input_limit_check("Enter blue value of background (range from 0-255): ")
        if green_input == None:
            break
        if (red_input, green_input, blue_input) != (red_background_input, green_background_input, blue_background_input):
            if (red_background_input and green_background_input and blue_background_input):
                background_done = True
            else:
                break
        else:
            print("You can't have the same background color as your text!")
            red_background_input = "-1"
            green_background_input = "-1"
            blue_background_input = "-1"
    if not background_done:
        break
    while not validate_rotation_input(rotation_input):
        rotation_input = input("Enter the amount of rotation in degrees (0, 90, 180, 270): ")
    while not validate_scroll_speed_input(scroll_speed_input):
        scroll_speed_input = input("Enter the scroll speed (speed has to be greater than 0): ")

    sense = SenseHat()
    sense.set_rotation(int(rotation_input))
    sense.show_message(input_string, 
            text_colour = (int(red_input),int(green_input),int(blue_input)), 
            back_colour = (int(red_background_input), int(green_background_input), int(blue_background_input)),
            scroll_speed = float(scroll_speed_input)
            )
    sense.clear()
