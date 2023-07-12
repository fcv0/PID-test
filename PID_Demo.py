# Jack Bradley - jackwbradley13@gmail.com
# Importance of tuning a PID controller demonstartion.
import turtle
import random
import matplotlib.pyplot as plt

screen = turtle.Screen()
screen.setup(1000, 1000)
boundary = turtle.Turtle(visible=False)
my_turtle = turtle.Turtle()
pos1, pos2 = 0, 350

XP, YP, XT, YT = [], [], [], []

def sim_L():
    rand1 = random.randint(pos1, pos2)
    rand2 = random.randint(pos1, pos2)
    print(f'x target = {rand1}, y target = {rand2}')

    def xPID(xpos, p, i, d):
        if p is None and i is None and d is None:
            p, i, d = 0.6, 0.05, 0.1
        global xtarget
        xtarget = rand1
        dt = 1
        integral = 0
        L_E = 0
        error = xtarget - xpos
        Kp = p*error
        integral += error * dt
        Ki = i*integral
        der = (error - L_E) / dt
        Kd = d*der
        out = Kp + Ki + Kd
        L_E = error
        return out

    def yPID(ypos, p, i, d):
        if p is None and i is None and d is None:
            p, i, d = 0.6, 0.05, 0.1
        global ytarget
        ytarget = rand2
        dt = 1
        integral = 0
        L_E = 0
        error = ypos - ytarget
        Kp = p*error
        integral += error * dt
        Ki = i*integral
        der = (error - L_E) / dt
        Kd = d*der
        out = Kp + Ki + Kd
        L_E = error
        return out

    def xpath():
        C=0
        while True:
            x = my_turtle.xcor()
            print(x, 'xpos')
            correctionx = xPID(x, p=P, i=I, d=D)
            my_turtle.forward(correctionx)
            XP.append(x), XT.append(C)
            C += 1
            if my_turtle.xcor() == xtarget:
                break

    def ypath():
        C=0
        while True:
            y = my_turtle.ycor()
            print(y, 'ypos')
            correctiony = yPID(y, p=P, i=I, d=D)
            my_turtle.backward(correctiony)
            YP.append(y), YT.append(C)
            C +=1
            if my_turtle.ycor() == ytarget:
                break
    def plot():
        plt.figure(1), plt.plot(XT, XP, 'r'), plt.xlabel('Time step'), plt.ylabel('X Position'), plt.title('PID controller X Pos vs Time steps')
        plt.figure(2), plt.plot(YT, YP, 'y'), plt.xlabel('Time step'), plt.ylabel('Y Position'), plt.title('PID controller Y Pos vs Time steps'), plt.show()
    
    my_turtle.speed(5)
    xpath()
    my_turtle.left(90)
    ypath()
    plot()

if __name__ == '__main__':
    # You can visually see the effect of PID on the positional movement of the moving object.
    # Mess around with these values and compare the difference.
    # These values are not tuned, if you want to see the tuned values of P I D the comment line 75 and uncomment line 76
    P, I, D = 0.5, 0.5, 0.5
    #P, I, D = None, None, None
    for i in range(1):
        sim_L()
        my_turtle.right(90)