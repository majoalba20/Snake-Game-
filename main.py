from turtle import Screen
from snake import Snake
import time

#crear el escenario
screen = Screen() #instanciar obj
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate Snake")

screen.tracer(0) #Quitamos animación de movimiento

snake = Snake() #crear - instanciar obj

game_is_on = True

while game_is_on:

    screen.update() #elimina el efecto oruga de la serpiente
    time.sleep(0.2) #velocidad de los cuadros ms

    snake.move()

screen.exitonclick()