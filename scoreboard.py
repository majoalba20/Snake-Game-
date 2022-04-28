from turtle import Turtle

class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color('white')
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"El puntajes es: {self.score}",font=("Arial",24,"normal"),align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("¡¡Juego terminado!! :(",font=("Arial",24,"normal"),align="center")

