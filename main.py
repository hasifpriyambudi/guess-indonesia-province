import turtle
import pandas
IMAGE = "indonesia-province.gif"
EXPORT = "province-to-learn.csv"

def get_mouse_click_coor(x, y):
    print(x, y)


screen = turtle.Screen()
screen.setup(1200, 634)
screen.title("Guess Indonesia Province")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("34-province.csv")
provinceList = data['province'].to_list()
correct = 0
correctAnswer = []

while len(correctAnswer) < len(provinceList):
    answer = screen.textinput(f"{correct}/{len(provinceList)} Province Correct", "What's another Province's name?").title()
    turtle.onscreenclick(get_mouse_click_coor)
    if answer == "Exit":
        missingProvince = []
        for province in provinceList:
            if province not in correctAnswer:
                missingProvince.append(province)
        newData = pandas.DataFrame(missingProvince)
        newData.to_csv(EXPORT)
        break
    if answer in provinceList:
        if answer not in correctAnswer:
            coordinates = data[data['province'] == answer]
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(int(coordinates['x']), int(coordinates['y']))
            t.write(answer, font=("Arial", 12, "normal"))
            correct += 1
            # coordinates['state'].item()
            correctAnswer.append(answer)
