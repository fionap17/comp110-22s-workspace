"""Drawing a scenic view of mountains and sunset."""

__author__ = "730243735"


from random import randint


from turtle import Turtle, colormode, done
colormode(255)

"""Criteria to call for the same function twice fulfilled: fn 34-35."""
"""Criteria to fill color fulfilled: fn 69-76."""
"""Criteria to use loop fulfilled: fn 41-47."""
"""Criteria to change marker color fulfilled: fn 106."""

"""Criteria to try something fun fulfilled: fn 53-58."""


def main() -> None:
    """The entrypoint of my scene."""
    paint: Turtle = Turtle()
    background_sky(paint, -350, 0, 450)
    background_sky(paint, -750, 0, 450)
    background_sky(paint, 0, 0, 450)
    background_sky(paint, 350, 0, 450)

    background_meadow(paint, -350, -450, 450)
    background_meadow(paint, -750, -450, 450)
    background_meadow(paint, 0, -450, 450)
    background_meadow(paint, 350, -450, 450)

    """Mountains."""
    draw_triangle(paint, 0, 0, 350)
    draw_triangle(paint, -350, 0, 350)

    """Snow cap on mountain."""
    draw_cap(paint, -250, 175, 150)
    draw_cap(paint, 100, 175, 150)

    i: int = 0
    s: int = 0
    while i < 3:
        draw_snow(paint, -250 + s, 175, 50)
        draw_snow(paint, 100 + s, 175, 50)
        i += 1
        s += 50

    """Lake in foreground."""
    draw_lake(paint, 750, -850, 750, 180)

    """Drawing a random number of trees"""
    idx: int = 0
    sx: int = 0
    while idx < randint(10, 40):
        draw_forest(paint, -400 + sx, 0, 100)
        sx += 50
        idx += 1


def draw_triangle(mountain: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the mountains in the background."""
    mountain.hideturtle()
    mountain.speed(100)
    mountain.penup()
    mountain.goto(x, y)
    mountain.setheading(0.0)
    mountain.pendown()
    mountain.color("gray")
    mountain.begin_fill()
    i: int = 0
    while i < 3:
        mountain.forward(width)
        mountain.left(120)
        i += 1
    mountain.end_fill()


def draw_snow(snow: Turtle, x: float, y: float, fluff: float) -> None:
    """Draws more snow for the edges of the snowcap on the mountains."""
    snow.hideturtle()
    snow.speed(100)
    snow.penup()
    snow.goto(x, y)
    snow.setheading(0.0)
    snow.pendown()
    snow.pencolor("white")
    snow.fillcolor("white")
    snow.begin_fill()
    i: int = 0
    while i < 3:
        snow.forward(fluff)
        snow.right(120)
        i += 1
    snow.end_fill()


def draw_cap(cap: Turtle, x: float, y: float, ice: float) -> None:
    """Draws the snowcap at the top of each mountain."""
    cap.hideturtle()
    cap.speed(100)
    cap.penup()
    cap.goto(x, y)
    cap.setheading(0.0)
    cap.pendown()
    cap.pencolor("white")
    cap.fillcolor("white")
    cap.begin_fill()
    idx: int = 0
    while idx < 3:
        cap.forward(ice)
        cap.left(120)
        idx += 1
    cap.end_fill()


def background_sky(sky: Turtle, x: float, y: float, horizon: float) -> None:
    """Draws a blue sky in the background."""
    sky.hideturtle()
    sky.speed(100)
    sky.penup()
    sky.goto(x, y)
    sky.setheading(0.0)
    sky.pendown()
    sky.color("light blue")
    sky.begin_fill()
    i: int = 0
    while i < 4:
        sky.forward(horizon)
        sky.left(90)
        i += 1
    sky.end_fill()


def background_meadow(field: Turtle, x: float, y: float, width: float) -> None:
    """Draws a grassy meadow."""
    field.hideturtle()
    field.speed(100)
    field.penup()
    field.goto(x, y)
    field.setheading(0.0)
    field.pendown()
    field.color(60, 80, 20)
    field.begin_fill()
    i: int = 0
    while i < 4:
        field.forward(width)
        field.left(90)
        i += 1
    field.end_fill()


def draw_lake(radius: Turtle, x: float, y: float, rad1: float, rad2: float) -> None:
    """Draws a lake in the foreground of scene."""
    radius.hideturtle()
    radius.speed(100)
    radius.penup()
    radius.goto(x, y)
    radius.setheading(90.0)
    radius.pendown()
    radius.color("dark blue")
    radius.begin_fill()
    radius.circle(rad1, rad2)
    radius.end_fill()


def draw_forest(tree: Turtle, x: float, y: float, height: float) -> None:
    """Draws trees into the meadow."""
    tree.hideturtle()
    tree.speed(100)
    tree.penup()
    tree.goto(x, y)
    tree.setheading(0.0)
    tree.pendown()
    tree.pencolor("green")
    tree.fillcolor("dark green")
    tree.begin_fill()
    i: int = 0
    while i < 3:
        tree.forward(height)
        tree.left(120)
        i += 1
    tree.end_fill()


if __name__ == "__main__":
    main()
    done()