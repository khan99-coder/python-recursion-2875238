"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import turtle

MAX_LENGTH = 250
INCREMENT = 10


def draw_spiral(a_turtle, line_length):
    # TODO: Add a base case to stop the recursion when the line_length exceeds MAX_LENGTH
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    # TODO: Add a recursive call to draw_spiral with the line_length incremented by INCREMENT
    draw_spiral(a_turtle, line_length + INCREMENT)


charlie = turtle.Turtle(shape="turtle")
charlie.pensize(5)
charlie.color("red")
draw_spiral(charlie, 10)
turtle.done()
