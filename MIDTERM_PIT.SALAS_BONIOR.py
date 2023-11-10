# Using time to make the text appear to the console as if being type by a typewriter
# This is applicable to text1,text3,text4,text5 and to the delays
import time
from turtle import Turtle, Screen

while True:
    screen = Screen()
    text1 = "Hello and Welcome, Wanna combine colors?"
    for char in text1:
        print(char, end='', flush=True)
        time.sleep(0.050)

    text2 = int(input("\nIf yes press 1"
                      "\nIf you're not interested press 2"
                      "\nEnter here:"))

    if text2 == 1:
        print("Valid input")
    elif text2 == 2:
        print("Program stop.")
        screen.bye()  # Close the turtle graphics window
        break  # Exit the loop
    else:
        print("Invalid input. Refer to the choices.")

    print("\n========================="
          "\n====LET'S GET STARTED===="
          "\n=========================")

    # Adding delay
    delay_second = 1
    time.sleep(delay_second)

    text3 = "\n****Select your primary color****"
    for char in text3:
        print(char, end='', flush=True)
        time.sleep(0.050)

    # Using selections to variables color1, color2 to get the desired output based on the input of the user
    color1 = int(input('\nPress 1 for RED'
                       '\nPress 2 for YELLOW'
                       '\nPress 3 for BLUE '
                       '\nEnter here:'))
    if color1 == 1:
        print("You have selected RED")
    elif color1 == 2:
        print("You have selected YELLOW")
    elif color1 == 3:
        print("You have selected BLUE")
    else:
        print("The input is invalid, refer to the choices.")

    print("\n============================================================"
          "\n------------------------------------------------------------"
          "\n-----NOW LET'S PROCEED ON SELECTING THE SECONDARY COLORS-----"
          "\n------------------------------------------------------------"
          "\n============================================================")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    text4 = "\n*****Select your secondary color*****"
    for char in text4:
        print(char, end='', flush=True)
        time.sleep(0.050)

    color2 = int(input("\nPress 5 for GREEN"
                       "\nPress 6 for ORANGE "
                       "\nPress 7 for PURPLE"
                       "\nEnter here:"))
    if color2 == 5:
        print("You have selected GREEN ")
    elif color2 == 6:
        print("You have selected ORANGE ")
    elif color2 == 7:
        print("You have selected PURPLE ")
    else:
        print("The input is invalid, refer to the choices.")

    print("\n=================================================="
          "\n-----THE RESULT OF THE COLORS YOU HAVE CHOSEN-----"
          "\n==================================================")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    text5 = "\nThe tertiary result is:"
    for char in text5:
        print(char, end='', flush=True)
        time.sleep(0.050)

    # Combining two variables by multiplying the number inputs of the user
    inputs = color1 * color2

    tertiary_result = ""
    if inputs == 5:
        tertiary_result = "YELLOW\nColor Code: #FFFF00"
    elif inputs == 6:
        tertiary_result = "VERMILION\nColor code: #E34234"
    elif inputs == 7:
        tertiary_result = "MAGENTA/RED-VIOLET\nColor code: #C71585"
    elif inputs == 10:
        print("YELLOW-GREEN"
              "\nColor code: #9ACD32")
    elif inputs == 12:
        print("AMBER"
              "\nColor code: #FFBF00")
    elif inputs == 14:
        print("BROWN"
              "\nColor code: #964B00")
    elif inputs == 15:
        print("TEAL"
              "\nColor code: #008080")
    elif inputs == 18:
        print("REDDISH-BROWN OF BURNT SIENNA"
              "\nColor code: #E97451")
    elif inputs == 21:
        print("BLUE-VIOLET"
              "\nColor code: #8a2be2")

    # Add more conditions for other cases

    print(f"\n{tertiary_result}")

    # Adding delay after end_fill before continuing
    delay_seconds = 1
    time.sleep(delay_seconds)

    # Asking the user for input
    shape_selector = int(input("\nIn what shape do you want this color to be filled?"
                               "\n[1] Circle"
                               "\n[2] Diamond/Square(4 sides)"
                               "\n[3] Triangle(3 sides)"
                               "\n[4] Pentagon(5 sides)"
                               "\n[5] Hexagon(6 sides)"
                               "\nEnter here:"))

    # Importing turtle inside the Multi-way if-elif-else Statements
    pen = Turtle()
    pen.hideturtle()

    if shape_selector == 1:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(-10, -190)
        pen.down()
        pen.circle(radius=200)
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=200)
        pen.end_fill()
        time.sleep(2)  # Adding a delay for visibility (you can adjust the duration)

    elif shape_selector == 2:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(-10, -190)
        pen.down()
        pen.circle(radius=200, steps=4)
        pen.color("white")
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=200, steps=4)
        pen.end_fill()
        time.sleep(2)  # Adding a delay for visibility (you can adjust the duration)

    elif shape_selector == 3:


    else:
        print("Can't read input.")

    screen.update()  # Update the turtle screen

