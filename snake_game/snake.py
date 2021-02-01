from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  # this is bcuz we want to organise each turtle b4 they wer just placed
        # on screen

    def reset(self): # this is cuz if game over score goes to high scre and new game should start
        for seg in self.segments:
            seg.goto(1000, 1000) # this is uz thogh we clear all segents but it still stay and create another snake thats why we are moving all them from out of our screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # this is for changing direction of snake we will move 3rd to 2nd,
            # 2nd to 1 & 1 to its next position
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # using this we will take position of its previous seg
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)

