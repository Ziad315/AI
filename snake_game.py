                  #============> Start <==============#
#files to include
import turtle
import time
import random
import sys
delay=0.1
score=0
high_score=0

 
#Set up the screen
wn=turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)     
wn.tracer(0)#turns off screen updates



# snake head
head=turtle.Turtle()
head.speed(0)  #animation speed
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction="stop"



#food
food=turtle.Turtle()
food.speed(0)  #animation speed
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#segment
segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 High Score: 0", align="center",font=("courier",24,"normal"))


#functions
def go_up():
    if head.direction != "down":
        head.direction="up"
    
def go_down():
    if head.direction!="up":
        head.direction="down"
    
def go_left():
    if head.direction!="right":
        head.direction="left"
    
def go_right():
    if head.direction!="left":
          head.direction="right"
    

def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)
        
    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20)    


# keyboard moves
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


#Main loop
while True:
    wn.update()
    #check collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segment in segments:
            segment.goto(2000,2000)
            
        delay-=0.001
        segments.clear()  
        #reset score
        score=0
        pen.clear()

        pen.write("score: {} High score: {}".format(score,high_score),align="center",font=("courier",24,"normal")) 
                        
    #collision
    if head.distance(food)<20:
        #move food to random location
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color=("grey")
        new_segment.penup()
        segments.append(new_segment)


        #add score
        score+=10


        if score>high_score:
            high_score=score

        pen.clear()

        pen.write("score: {} High score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))    
        
   # move The end segment first
    for index in range(len(segments)-1, 0, -1):
       x=segments[index-1].xcor()
       y=segments[index-1].ycor()
       segments[index].goto(x,y)


   # move of segment 0
    if len(segments)>0:
       x=head.xcor()
       y=head.ycor()
       segments[0].goto(x,y)
        
    move()

    #check for head collsion

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                segment.goto(1000,1000)
            

            segments.clear()  



      
    time.sleep(delay)


wn.mainloop()
               
                 #============> End <==============#
