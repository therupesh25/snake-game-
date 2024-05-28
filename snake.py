from turtle import Turtle
HEADING=[(0,0) , (-20,0) , (-40,0)]
FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self) :
         self.segments=[]
         self.create_snake()
         self.head = self.segments[0]
    def create_snake(self):
        for position in HEADING:
            self.add_new_segment(position)
    def add_new_segment(self,position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)
    def extend_seg(self):
        self.add_new_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0 , -1):
            xpos=self.segments[seg - 1].xcor()
            ypos=self.segments[seg - 1].ycor()
            self.segments[seg].goto(xpos, ypos)
        self.head.forward(FORWARD)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT :
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)