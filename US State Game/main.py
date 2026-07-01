import turtle
import pandas as pd


screen=turtle.Screen()
image=r"C:\Users\bhatt\Desktop\US State Game\blank_states_img.gif"
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv(r"C:\Users\bhatt\Desktop\US State Game\states_data.csv")
all_states=data.state.to_list()

guessed_states=[]

while len(guessed_states)<50:
    
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv(r"C:\Users\bhatt\Desktop\US State Game\missed_states.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)




