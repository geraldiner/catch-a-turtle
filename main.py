# Make a turtle on the screen jump to a random location if a person is able to click it in time.
# The click should trigger the player’s score to accumulate.
# If the timer runs out before the turtle is clicked, the turtle will disappear and the game will display a message.

#-----import statements-----
import turtle
import random

#-----game configuration----
# intial config variables
spot_color = "green"
spot_size = 2
spot_shape = "turtle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000
timer_up = False
sizes = [0.5, 1, 1.5, 2]
colors = ["red", "orange", "yellow", "blue", "purple"]

#-----initialize turtle-----

# Screen
wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("lightblue")
wn.colormode(255)

# Turtle
spot = turtle.Turtle(spot_shape)
spot.hideturtle()
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

# Score Writer
score_writer = turtle.Turtle("blank")
score_writer.penup()
score_writer.goto(-200, 200)
score_writer.pendown()

# Timer/Counter
counter = turtle.Turtle("blank")
counter.penup()
counter.goto(100, 200)
counter.pendown()

# Start Game Text
start_game_text = turtle.Turtle("blank")
start_game_text.penup()
start_game_text.goto(-100, 0)
start_game_text.pendown()
start_game_text.write("Click the arrow to start.",
                      font=("Arial", 14, "normal"))

# Start Game Button
start_game_button = turtle.Turtle("classic")
start_game_button.shapesize(5)
start_game_button.fillcolor("orange")
start_game_button.penup()
start_game_button.goto(40, -50)
start_game_button.pendown()

#-----game functions--------


def start_game_clicked(x, y):
	start_game_text.clear()
	start_game_text.hideturtle()
	start_game_button.hideturtle()
	score_writer.write("Score: " + str(score), font=font_setup)
	spot.showturtle()
	wn.ontimer(countdown, counter_interval)


def spot_clicked(x, y):
	if (timer_up == False):
		update_score()
		stamp_color()
		change_size()
		change_position()
	else:
		spot.hideturtle()


def stamp_color():
	new_R = random.randint(0,255)
	new_G = random.randint(0,255)
	new_B = random.randint(0,255)
	spot.fillcolor(new_R, new_G, new_B)
	spot.stamp()
	spot.fillcolor(spot_color)


def change_size():
	new_size = random.uniform(0.5, 2)
	spot.shapesize(new_size)


def change_position():
	new_xpos = random.randint(-200, 200)
	new_ypos = random.randint(-150, 150)

	# move turtle
	spot.hideturtle()
	spot.penup()
	spot.goto(new_xpos, new_ypos)
	spot.pendown()
	spot.showturtle()


def update_score():
	global score
	score += 1
	score_writer.clear()
	score_writer.write("Score: " + str(score), font=font_setup)


def countdown():
	global timer, timer_up
	counter.clear()
	if timer <= 0:
		counter.write("Time's Up", font=font_setup)
		timer_up = True
	else:
		counter.write("Timer: " + str(timer), font=font_setup)
		timer -= 1
		counter.getscreen().ontimer(countdown, counter_interval)


#-----events----------------
start_game_button.onclick(start_game_clicked)
spot.onclick(spot_clicked)
wn.mainloop()
