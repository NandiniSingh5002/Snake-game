from turtle import Screen,Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-20, 0)]
MOVE_DISTANCE=20; #constant
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]#it store segment first heading
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)  # it appends box we made
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):  # 2,1,0
            new_x = self.segment[seg_num - 1].xcor()  # IT FIND  i th index xcor
            new_y = self.segment[seg_num - 1].ycor()  # it find i th index ycor
            self.segment[seg_num].goto(new_x, new_y)  # it  will put i-1th box ar i th box x & y corrdinate
        self.head.forward(MOVE_DISTANCE)  # first box keep moving
    def up(self):
        if self.head.heading !=DOWN: #agra abhi ki heading down nhi hai tabhi up move kar skta hai
           self.head.setheading(UP)
    def down(self):
        if self.head.heading != UP:
           self.head.setheading(DOWN)
    def left(self):
        if self.head.heading != RIGHT:
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading != LEFT:
           self.head.setheading(RIGHT)