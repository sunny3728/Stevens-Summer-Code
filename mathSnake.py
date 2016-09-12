#Main project code. Uses graphics.py, snake.gif, and raspLogo.gif
#written at summer workshop Mini-Hackathon july 2015
from graphics import *
import time
import string
import random
global win
win=GraphWin("Feed the Python!",500,500)
global snake
snake=Image(Point(250,500),"Snake.gif")
global message
message = Text(Point(225,15),"")
global rasp1
rasp1 = Image(Point(50,450),"rasplogo.gif")
global rasp2
rasp2 = Image(Point(150,450),"rasplogo.gif")
global rasp3
rasp3 = Image(Point(250,450),"rasplogo.gif")
global rasp4
rasp4 = Image(Point(350,450),"rasplogo.gif")
global rasp5
rasp5 = Image(Point(450,450),"rasplogo.gif")
global ans1
ans1 = Text(Point(50,500),"")
global ans2
ans2 = Text(Point(150,500),"")
global ans3
ans3 = Text(Point(250,500),"")
global ans4
ans4 = Text(Point(350,500),"")
global ans5
ans5 = Text(Point(450,500),"")
global answer
answer = 20
global whichRasp
whichRasp = 0

def mathGame():
        global win
        global snake
        global rasp1
        global rasp2
        global rasp3
        global rasp4
        global rasp5
        global ans1
        global ans2
        global ans3
        global ans4
        global ans5
        global message
        global answer
         
        snake.draw(win)
        message.draw(win)
        count = 0
        
        while count<10:
                rasp1.draw(win)
                ans1.draw(win)
                rasp2.draw(win)
                ans2.draw(win)
                rasp3.draw(win)
                ans3.draw(win)
                rasp4.draw(win)
                ans4.draw(win)
                rasp5.draw(win)
                ans5.draw(win)
                equation()
                genAns()
                snakeMove()
                check()
                count+=1
        message.setText("Thanks for Playing!")
        win.getMouse()
        win.close()
        
def check():
        global win
        global snake
        global rasp1
        global rasp2
        global rasp3
        global rasp4
        global rasp5
        global whichRasp
        response = Text(Point(250,200),"")
        response.draw(win)
        if snake.getAnchor().getX() == rasp1.getAnchor().getX():#if the snake is under this raspberry
                if whichRasp==1:
                        response.setText("Correct!")
                        time.sleep(3)
                        response.setText("")
                else:
                        response .setText("Incorrect")
                        time.sleep(3)
                        response.setText("")
        if snake.getAnchor().getX() == rasp2.getAnchor().getX():
                if whichRasp==2:
                        response.setText("Correct!")
                        time.sleep(3)
                        response.setText("")
                else:
                        response .setText("Incorrect")
                        time.sleep(3)
                        response.setText("")
        if snake.getAnchor().getX() == rasp3.getAnchor().getX():
                if whichRasp==3:
                        response.setText("Correct!")
                        time.sleep(3)
                        response.setText("")
                else:
                        response .setText("Incorrect")
                        time.sleep(3)
                        response.setText("")
        if snake.getAnchor().getX() == rasp4.getAnchor().getX():
                if whichRasp==4:
                        response.setText("Correct!")
                        time.sleep(3)
                        response.setText("")
                else:
                        response .setText("Incorrect")
                        time.sleep(3)
                        response.setText("")
        if snake.getAnchor().getX() == rasp5.getAnchor().getX():
                if whichRasp==5:
                        response.setText("Correct!")
                        time.sleep(3)
                        response.setText("")
                else:
                        response .setText("Incorrect")
                        time.sleep(3)
                        response.setText("")
def snakeMove():
        global win
        global snake
        global message
        global answer
        rasp1.move(0,-390)
        ans1.move(0,-390)
        rasp2.move(0,-390)
        ans2.move(0,-390)
        rasp3.move(0,-390)
        ans3.move(0,-390)
        rasp4.move(0,-390)
        ans4.move(0,-390)
        rasp5.move(0,-390)
        ans5.move(0,-390)
        x=0
        while x<13:
                raspfall()
                direction = win.getKey()
                x+=1
                if direction == "Left" and snake.getAnchor().getX()>50:
                        snake.move(-100,0)
                elif direction == "Right" and snake.getAnchor().getX()<450:
                        snake.move(100,0)
        rasp1.undraw()
        rasp2.undraw()
        rasp3.undraw()
        rasp4.undraw()
        rasp5.undraw()
        ans1.undraw()
        ans2.undraw()
        ans3.undraw()
        ans4.undraw()
        ans5.undraw()
                        
def raspfall():
        global win
        global rasp1
        global rasp2
        global rasp3
        global rasp4
        global rasp5
        global ans1
        global ans2
        global ans3
        global ans4
        global ans5
        if rasp1.getAnchor().getY()<500:
                rasp1.move(0,30)
                ans1.move(0,30)
                rasp2.move(0,30)
                ans2.move(0,30)
                rasp3.move(0,30)
                ans3.move(0,30)
                rasp4.move(0,30)
                ans4.move(0,30)
                rasp5.move(0,30)
                ans5.move(0,30)

def equation():
        global win
        global message
        global answer
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        sign = random.randint(0,1)
        if sign == 0:
                question = str(num1)+"+"+str(num2)+"= ?"
                answer = num1+num2
        elif sign == 1:
                question = str(num1)+"-"+str(num2)+"= ?"
                answer = num1-num2
        message.setText(question)
def genAns():
        global win
        global whichRasp
        global rasp1
        global rasp2
        global rasp3
        global rasp4
        global rasp5
        global ans1
        global ans2
        global ans3
        global ans4
        global ans5
        global message
        global answer
        rand1 = random.randint(-9,18)
        while rand1 == answer:
                rand1 = random.randint(-9,18)
        rand2 = random.randint(-9,18)
        while rand2==answer or rand2==rand1:
                rand2 = random.randint(-9,18)
        rand3 = random.randint(-9,18)
        while rand3==answer or rand3==rand1 or rand3==rand2:
                rand3 = random.randint(-9,18)
        rand4 = random.randint(-9,18)
        while rand4==answer or rand4==rand1 or rand4==rand3 or rand4==rand2:
                rand4 = random.randint(-9,18)
        whichRasp = random.randint(1,5)
        if whichRasp == 1:
                ans1.setText(answer)
                ans2.setText(rand1)
                ans3.setText(rand2)
                ans4.setText(rand3)
                ans5.setText(rand4)
        elif whichRasp == 2:
                ans1.setText(rand1)
                ans2.setText(answer)
                ans3.setText(rand2)
                ans4.setText(rand3)
                ans5.setText(rand4)
        elif whichRasp == 3:
                ans1.setText(rand1)
                ans2.setText(rand2)
                ans3.setText(answer)
                ans4.setText(rand3)
                ans5.setText(rand4)
        elif whichRasp == 4:
                ans1.setText(rand1)
                ans2.setText(rand2)
                ans3.setText(rand3)
                ans4.setText(answer)
                ans5.setText(rand4)
        elif whichRasp == 5:
                ans1.setText(rand1)
                ans2.setText(rand2)
                ans3.setText(rand3)
                ans4.setText(rand4)
                ans5.setText(answer)

def main():
        mathGame()
        
