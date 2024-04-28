#Marvin Barksdale
#4/28/2024
#P4 LAB1
#Use turtle and loops to draw a triangle


#import the library
import turtle


# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()


#set turtle options
pen.pensize (5)
pen.pencolor("blue")
pen.shape("turtle")
pen.shape("arrow")

#Code to draw shapes
#pen.forward(200)
#pen.left(90)
#pen.forward(200)
#pen.left(90)
#pen.forward(200)
#pen.left(90)
#pen.forward(200)

for side in range(4):
    pen.forward(200)
    pen.left(90)



#while loop that executes 3 times
#change color of pen for triangle

pen.pencolor("red")

sides =3

while sides > 0:
    pen.forward (200)
    pen.left (120)
    sides = sides -1

    
#wait for user to close window
win.mainloop()
