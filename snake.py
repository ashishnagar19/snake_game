from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.timmy = []
        self.create_snake()
        self.head = self.timmy[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.timmy.append(segment)

    def reset(self):
        for segment in self.timmy:
            segment.goto(1000, 1000)
        self.timmy.clear()
        self.create_snake()
        self.head = self.timmy[0]

    def extend(self):
        self.add_segment(self.timmy[-1].position())




    def move(self):
        for seg_num in range(len(self.timmy)-1, 0, -1):
            new_x = self.timmy[seg_num-1].xcor()
            new_y = self.timmy[seg_num-1].ycor()
            self.timmy[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() !=DOWN:
             self.head.setheading(90)

    def down(self):
        if self.head.heading !=UP:
             self.head.setheading(270)

    def right(self):
        if self.head.heading != LEFT:
             self.head.setheading(0)

    def left(self):
        if self.head.heading != RIGHT:
                self.head.setheading(180)




