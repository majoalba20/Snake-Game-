from turtle import Screen
from food import Food
from snake import Snake
from food import Food
import time
from scoreboard import Scorebord

#crear el escenario
screen = Screen() #instanciar obj
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate Snake")

screen.tracer(0) #Quitamos animación de movimiento

snake = Snake() #crear - instanciar obj
food = Food()

#tablero de puntos
score = Scorebord()

#movimiento de la serpiente
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")

game_is_on = True

while game_is_on:

    screen.update() #elimina el efecto oruga de la serpiente
    time.sleep(0.2) #velocidad de los cuadros ms

    snake.move()

    #detectar colision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extends()

    #detectar las paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score.game_over()

    #detectar la colision de la cola
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()