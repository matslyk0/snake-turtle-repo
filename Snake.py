import turtle
import time
import random

delay = 0.1
segments = []

# Score
score = 0
highScoreTextFile = open("snakeHighScore.txt", "r")
highScore = highScoreTextFile.read()

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgpic("snakeBackground.gif")
screen.tracer(0)  # Turns off screen updates

# Default shape registering
headUp = "snakeHeadUpWhite.gif"
headDown = "snakeHeadDownWhite.gif"
headLeft = "snakeHeadLeftWhite.gif"
headRight = "snakeHeadRightWhite.gif"
segmentShape = "snakeBodySegmentWhite.gif"
turtle.register_shape("apple.gif")

def registration():
    turtle.register_shape(headUp)
    turtle.register_shape(headDown)
    turtle.register_shape(headLeft)
    turtle.register_shape(headRight)
    turtle.register_shape(segmentShape)
    
def colorReset():
    for index in segments:
        index.shape(segmentShape)
        
def whiteSnake():
    global headUp, headDown, headLeft, headRight, segmentShape
    headUp = "snakeHeadUpWhite.gif"
    headDown = "snakeHeadDownWhite.gif"
    headLeft = "snakeHeadLeftWhite.gif"
    headRight = "snakeHeadRightWhite.gif"
    segmentShape = "snakeBodySegmentWhite.gif"
    registration()
    colorReset()
    
def redSnake():
    global headUp, headDown, headLeft, headRight, segmentShape
    headUp = "snakeHeadUpRed.gif"
    headDown = "snakeHeadDownRed.gif"
    headLeft = "snakeHeadLeftRed.gif"
    headRight = "snakeHeadRightRed.gif"
    segmentShape = "snakeBodySegmentRed.gif"
    registration()
    colorReset()

def blueSnake():
    global headUp, headDown, headLeft, headRight, segmentShape
    headUp = "snakeHeadUpBlue.gif"
    headDown = "snakeHeadDownBlue.gif"
    headLeft = "snakeHeadLeftBlue.gif"
    headRight = "snakeHeadRightBlue.gif"
    segmentShape = "snakeBodySegmentBlue.gif"
    registration()
    colorReset()

def yellowSnake():
    global headUp, headDown, headLeft, headRight, segmentShape
    headUp = "snakeHeadUpYellow.gif"
    headDown = "snakeHeadDownYellow.gif"
    headLeft = "snakeHeadLeftYellow.gif"
    headRight = "snakeHeadRightYellow.gif"
    segmentShape = "snakeBodySegmentYellow.gif"
    registration()
    colorReset()

def greenSnake():
    global headUp, headDown, headLeft, headRight, segmentShape
    headUp = "snakeHeadUpGreen.gif"
    headDown = "snakeHeadDownGreen.gif"
    headLeft = "snakeHeadLeftGreen.gif"
    headRight = "snakeHeadRightGreen.gif"
    segmentShape = "snakeBodySegmentGreen.gif"
    registration()
    colorReset()

registration()
    
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("snakeHeadUpWhite.gif")
head.penup()
head.goto(0, 0)
head.direction = "stop"

def addSegment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape(segmentShape)
    new_segment.penup()
    segments.append(new_segment)

addSegment()
addSegment()
# Create food
food = turtle.Turtle()
food.speed(0)
food.shape("apple.gif")
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: {} High Score: {} Segments: {}".format(score, highScore, len(segments)), align="center",
          font=("Arial", 12, "normal"))

# Functions
def snake_restart():
    global delay, score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(9999, 9999)

    # Reset the segments to 2
    segments.clear()
    addSegment()
    addSegment()

    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1

    pen.clear()
    pen.write("Score: {} High Score: {} Segments: {}".format(score, highScore, len(segments)), align="center",
              font=("Arial", 12, "normal"))

def move():
    if head.direction == "up":
        moveUp()
    if head.direction == "down":
        moveDown()
    if head.direction == "left":
        moveLeft()
    if head.direction == "right":
        moveRight()

def moveUp():
    head.shape(headUp)
    y = head.ycor() + 20
    if y > 300:
        snake_restart()
    else:
        head.sety(y)

def moveRight():
    head.shape(headRight)
    x = head.xcor() + 20
    if x > 300:
        snake_restart()
    else:
        head.setx(x)

def moveLeft():
    head.shape(headLeft)
    x = head.xcor() - 20
    if x < -300:
        snake_restart()
    else:
        head.setx(x)

def moveDown():
    head.shape(headDown)
    y = head.ycor() - 20
    if y < -300:
        snake_restart()
    else:
        head.sety(y)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def snakeGrow():
    global delay, score, highScore, highScoreTextFile

    # Move the food to a random spot
    food.goto(random.randrange(-300, 300, 20), random.randrange(-300, 300, 20))

    # Reset the segments
    segments[len(segments) - 1].shape(segmentShape)

    # Add a segment
    addSegment()

    # Shorten the delay
    delay *= 0.95

    # Increase the score
    score += 10

    if score > int(highScore):
        highScoreTextFile = open("snakeHighScore.txt", "w")
        highScoreTextFile.write(str(score))
        highScoreTextFile = open("snakeHighScore.txt", "r")
        highScore = highScoreTextFile.read()
    pen.clear()
    pen.write("Score: {} High Score: {} Segments: {}".format(score, highScore, len(segments)), align="center",font=("Arial", 12, "normal"))

def selfCollisionReset():
    global segment, score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(9999, 9999)

    # Reset the segments to 2
    segments.clear()
    addSegment()
    addSegment()

    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1
    pen.clear()

    # Update the text
    pen.write("Score: {} High Score: {} Segments: {}".format(score, highScore, len(segments)), align="center",
              font=("Arial", 12, "normal"))

# Key bindings
screen.listen()
screen.onkeypress(whiteSnake, "1")
screen.onkeypress(redSnake, "2")
screen.onkeypress(blueSnake, "3")
screen.onkeypress(yellowSnake, "4")
screen.onkeypress(greenSnake, "5")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")

# Main game loop
while True:
    screen.update()

    # Check for a collision with the food
    if head.distance(food) < 20:
        snakeGrow()

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for a collision between the head and the segments
    if len(segments) > 2:
        for segment in segments:
            if segment.distance(head) < 20:
                selfCollisionReset()
    time.sleep(delay)
    
screen.mainloop()
