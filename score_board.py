from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")  # Set the color
        self.penup()  # Lifts the pen up, no drawing when moving
        self.goto(0, 260)  # Go to a visible position on screen
        self.hideturtle()  # Hide the turtle
        self.score = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=("Courier", 24, "normal"))

# Create
