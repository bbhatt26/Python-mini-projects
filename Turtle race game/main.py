from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
race=False
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
print(user)
colors=["red", "yellow", "pink", "blue", "purple"]
y_position=[-70,-40,-10,20,50,80]

all_turtles=[]

for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user:
    race=True
    
while race:
    for turtle in all_turtles:
        
        if turtle.xcor()>230:
            race=False
            winning_color=turtle.pencolor()
            if winning_color==user:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lose! The {winning_color} turtle is the winner.")
            
        distance=random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()
