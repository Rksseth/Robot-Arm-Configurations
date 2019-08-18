'''
Ravi Seth
July 27
Tron Days Operation Arm Calculations

POSSIBLE CONSTRAINTS FOR FIXED LENGTHS

    - x can never be negative, so the arm must stay in the 1st quadrant
    - RULE : a + b > c MUST!
'''
import math

from turtle import*

colours = ['red','blue','green','yellow','purple','orange']
idx = 0

def jumpto(x, y):
    penup(); goto(x,y)

def plotPoints(points):
    global idx
    jumpto(0, 0)
    for point in points:
        plot(point,colours[idx])
    return 1
    
def plot(point,color):
    pencolor(color)
    pendown()
    goto(point[0],point[1])
    dot(10)
    return 1

fixed1 = 21
fixed2 = 21 #FROM THE TOP DOWN
r1 = 45#21#HAS A HIGH AND LOW RANGE
r2 = 21#HAS A HIGH AND LOW RANGE

speed(1)
factor = 5

xRange = range(20,21)  #INPUT A RANGE FOR THE ARM TO BE
yRange = range(20,21) #INPUT A RANGE FOR Y AS WELL

print('What variable values put arm in x-%s and y-%s : \n'%(xRange,yRange))

for r1 in range(21,46,3):
    for r2 in range(21,46,3):
        for a1 in range(3,r1,3):
            for a2 in range(3,r2,3):
                for pneumatic1 in range(21,32,10):
                    for pneumatic2 in range(21,32,10):
                        try:
                            b1 = fixed1 #B FOR BOTTOM
                            c1 = pneumatic1#25 #Actuator RIGHT #RANGES FROM FULLY RETRACTED TO FULLY EXTENDED
                            #a1 = r1/2 #LEFT arm # ANOTHER RANGED VARIABLE

                            C1 =math.acos(((a1*a1+b1*b1-c1*c1)/(2*a1*b1)))#*180/math.pi #CONVERTS TO DEGREES
                            
                            arm1 = (math.cos(C1)*r1, math.sin(C1)*r1)

                            c2 = pneumatic2#25 #Actuator RIGHT - RANGES FROM FULLY RETRACTED TO FULLY EXTENDED
                            b2 = fixed2 #LEFT arm
                            #a2 = r2/4*3 #RIGHT arm , ANOTHER RANGED VARIABLE


                            
                            
                            C12 = math.acos(((b2*b2+a2*a2-c2*c2)/(2*a2*b2)))
                            C12 = C12
                            

                            #vA2 = [math.cos(C12)*arm1[0] + -1*math.sin(C12)+arm1[1],math.sin(C12)*arm1[0]+math.cos(C12)*arm1[1]]

                            #ANGLE
                            #C2 = math.atan(vA2[1]/vA2[0])


                                                                                   
                            C2 = (math.pi - C1 - C12)
                            #C2 = math.pi/2 - C2
                            C2 = -1*C2
                            
                            

                            
                            
                            #NOW DETERMINE THE POINT POSITIONS OF THE ACTUATOR
                            start1 = [fixed1,0]
                            start1 = [item*factor for item in start1]
                            end1 = [math.cos(C1)*a1,math.sin(C1)*a1]
                            end1 = [item*factor for item in end1]
                            
                            arm2 = (math.cos(C2)*r2, math.sin(C2)*r2)

                            #NOW DETERMINE THE POINT POSITIONS OF THE ACTUATOR
                            start2 = [arm1[0] - math.cos(C1)*b2,arm1[1] - math.sin(C1)*b2]
                            start2 = [item*factor for item in start2]
                            end2 = [math.cos(C2)*a2+arm1[0],math.sin(C2)*a2+arm1[1]]
                            end2 = [item*factor for item in end2]

            
                            #print(start,end)

                            
                            armTotal = [(arm1[i] + arm2[i]) for i in range(0,len(arm1))]
                            points = [arm1,armTotal]



                            if round(armTotal[0]) in xRange and round(armTotal[1]) in yRange:
                                #print(math.sqrt(math.pow(armTotal[0] - arm1[0],2) + math.pow(armTotal[1] - arm1[1],2)))
                                #print((math.sqrt(math.pow(start1[0]-end1[0],2) + math.pow(start1[1] - end1[1],2))/factor),end = ' ')
                                #print((math.sqrt(math.pow(start2[0]-end2[0],2) + math.pow(start2[1] - end2[1],2))/factor))
                                
                                penup();goto(start1[0],start1[1]);plot(start1,'black');plot(end1,'black')
                                dot(2)
                                penup();goto(start2[0],start2[1]);plot(start2,'black');plot(end2,'black')
                                dot(2)

                                

                                for point in points:
                                    points[points.index(point)] = [item*factor for item in point]
                                plotPoints(points)

                                print('R1 = %d P1 = %d R2 = %d P2 = %d Pneumatic1 = %d Pneumatic2 = %d (x,y) = (%0.1f,%0.1f)'%(r1,a1,r2,a2,pneumatic1,pneumatic2,armTotal[0],armTotal[1]))
                                idx += 1
                                idx = idx%len(colours)

                                 
                            #print(armTotal)
                        except:
                            pass

                
            


hideturtle()
