from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)] #tres cuadros

class Snake:

    def __init__(self):
        self.segments = [] #atributo
        self.create_snake() #metodo

    #creación de cuerpo de la serpiente
    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("red")
            snake_segment.penup() #quita la linea
            snake_segment.goto(position) #coordenadas de pos inicial x,y
            self.segments.append(snake_segment)

    #movimiento de la serpiente
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)

        self.segments[0].forward(20)
        # segments[0].left(90)

