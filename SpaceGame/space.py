"""
Project : Which Way?
Course:     CS 111
Prof:       Shanon Reckinger
Year:       2022-23
Members:    Aaryan Sharma, Ayush Bhardwaj

We have added a derivative of our final project from CS 111 to satisfy the space-theme criteria.
"""

import turtle
import random
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

dice_number = 0
position = 1

def addshape(filename):
    turtle.addshape(filename)


def game_exit(x,y):
  exit()


def ladder(object, target):                                                         # function moves the token upward to the desired position(target), effectively acting as a ladder.
    global position
    if position == object:
        position = target

def snake(object,target):                                                           # function moves the token downward to the desired position(target), effectively acting as a ladder.
    global position
    if position == object:
        position = target

def game_start():                                                                   # function used to define the very first screen of the game.
  game = open("game.txt")
  game_lines = game.readlines()
  game_start_line = game_lines[0]
  game.close()

  intro = turtle.Turtle()
  intro.turtlesize(0.1)
  intro.penup()
  intro.color("white")
  intro.fillcolor("white")
  intro.goto(0,50)

  title = turtle.Turtle()
  title.penup()
  title.turtlesize(0.1)
  title.goto(0,300)
  title.color("white")
  title.fillcolor("white")
  title.write("Which way?",False, align='center', font=('Arial', 40,"bold")) 

  start = turtle.Turtle()
  start.penup()
  start.goto(200,-100)

  exit = turtle.Turtle()
  exit.penup()
  exit.goto(-200,-100)

  exit.shape("exit.gif")
  start.shape("start.gif")
  intro.write(game_start_line,False, align='center', font=('Arial', 15))

  exit.onclick(game_exit)
  start.onclick(game_instruction)



def game_instruction(x,y):                                                          # function used to define the 2nd screen containing the instructions.
  global s
  s.clearscreen()
  s.bgpic("space.gif")
  instruct = open("instructions.txt")
  instruction_lines = instruct.readlines()
  instruct.close()

  title = turtle.Turtle()
  title.penup()
  title.turtlesize(0.1)
  title.goto(0,300)
  title.color("white")
  title.fillcolor("white")
  title.write("INSTRUCTIONS",False, align='center', font=('Arial', 40,"bold"))

  a = 200

  for i in range(len(instruction_lines)):
    a -= 100

    instruction = turtle.Turtle()
    instruction.penup()
    instruction.turtlesize(0.1)
    instruction.goto(-750,a)
    instruction.color("white")
    instruction.fillcolor("white")
    instruction.write(instruction_lines[i],False, align='left', font=('Arial', 20))

  
  next = turtle.Turtle()
  next.penup()
  next.goto(200,-200)

  exit = turtle.Turtle()
  exit.penup()
  exit.goto(-200,-200)

  exit.shape("exit.gif")
  next.shape("next.gif")

  exit.onclick(game_exit)
  next.onclick(game_main)


def game_win():                                                                  # function used to define the congratulatory screen, containing the overall theme of the project.
    global s
    s.clearscreen()
    s.bgpic("space.gif")
    win = turtle.Turtle()
    win.penup()
    win.turtlesize(0.1)
    win.color("white")
    win.fillcolor("white")
    win.goto(0,150)

    msg = turtle.Turtle()
    msg.penup()
    msg.turtlesize(0.1)
    msg.color("dark orange")
    msg.fillcolor("dark orange")
    msg.goto(0,-50)

    win.write("Congratulations, you have won the game!", False, align='center', font=('Arial', 40))
    msg.write("\"The only way out is through.\" - Robert Frost", False, align='center', font=('Arial', 20))



    retry = turtle.Turtle()
    retry.penup()
    retry.goto(200,-300)

    exit = turtle.Turtle()
    exit.penup()
    exit.goto(-200,-300)

    retry.shape("retry.gif")
    exit.shape("exit.gif")

    retry.onclick(game_retry)
    exit.onclick(game_exit)


def dice_click(x,y):                                                                # function used to define the behaviour/actions when the dice turtle is clicked.
    global num
    global dice_number
    global t
    global position

    num.clear()
    dice_number = random.randint(1,6)
    # dice_number = 99
    position += dice_number
    num.write(str(dice_number), False, align='center', font=('Arial', 30))

    if position < 100:
        ladder(2,23)
        ladder(8,12)
        ladder(17,93)
        ladder(29,54)
        ladder(32,51)
        ladder(70,89)
        ladder(75,96)

        snake(99,4)
        snake(41,20)
        snake(58,31)
        snake(67,49)
        snake(84,62)
        snake(92,76)  
        
        t.goto(goto_square(position))

    elif position == 100:
        game_win()

    elif position > 100:
      position = position - dice_number
        



def dictionary_squares():                                                           # function creates a dictionary of each square and the coordinate of the corresponding midpoint.
    dict = {}

    filename = "coordinates.txt"
    file = open(filename)
    lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i]
        line_content = line.split()
        key = line_content[0]
        value = [int(line_content[1])/2, int(line_content[2])/2]

        dict[key] = value

    file.close()

    return dict


def goto_square(position):                                                          # function is used to move the token to the desired position, using the coordinates of the midpoint of the desired square.
    dict = dictionary_squares()
    coordinate_list = dict[str(position)]
    x = coordinate_list[0]
    y = coordinate_list[1]

    return x,y


def game_main(x,y):                                                                 # function used to define the main functioning of the game.
  global s
  global num
  global t

  s.clearscreen()
  s.bgpic("space.gif")

  num = turtle.Turtle()
  num.color("white")
  num.fillcolor("white")
  num.penup()
  num.hideturtle()
  num.goto(313, 190)


  bg = turtle.Turtle()
  bg.shape("bg.gif")

  ladder = turtle.Turtle()
  ladder.penup()
  ladder.hideturtle()
  ladder.goto(-500, 150)
  ladder.showturtle()

  snake = turtle.Turtle()
  snake.penup()
  snake.hideturtle()
  snake.goto(-500, -150)
  snake.showturtle()

  exit = turtle.Turtle()
  exit.penup()
  exit.goto(500,-300)

  exit.shape("exit.gif")
  snake.shape("Snakes.gif")
  ladder.shape("Ladders.gif")

  exit.onclick(game_exit)

  t = turtle.Turtle()
  t.shape("goti.gif")
  t.penup()


  dice = turtle.Turtle()
  dice.shape("dice.gif")
  dice.hideturtle()
  dice.penup()
  dice.goto(275,213)
  dice.showturtle()
  dice.onclick(dice_click)

  t.goto(goto_square(position))


def game_retry(x,y):
  global position

  position = 1
  game_main(x,y)


"""
MAIN CODE:
"""

addshape("goti.gif")
addshape("bg.gif")
addshape("dice.gif")
addshape("next.gif")
addshape("exit.gif")
addshape("retry.gif")
addshape("start.gif")
addshape("Snakes.gif")
addshape("Ladders.gif")

s = turtle.getscreen()
s.bgpic("space.gif")
s.listen()

game_start()

turtle.mainloop()