import tkinter as tk #Lets us create user interface
import math #Had to import this, as otherwise the calculations wouldn't work

#Create the application window
window = tk.Tk()

#Create the heading label for "Projectile Estimator"
lblHeading = tk.Label(
    text = "Projectile Estimator", #text for the Heading
    height = 2, #how much vertical distance it takes up
    font = ("Impact", 20, "bold")) #font type, size, and make it bolded 

#Place the heading on the top of the window (row = 1) 
lblHeading.grid(column = 1, row = 1) 

#Create the label for "Velocity"
#Place it a bit below the heading (row = 3)
lblVelocity = tk.Label(text = "Velocity (m/s): ")
lblVelocity.grid(column = 1, row = 3, stick = tk.W)

#Create the textbox for Velocity with an INPUT field (tk.Entry)
#Place it right next to lblVelocity (tk.E) 
txtVelocity = tk.Entry()
txtVelocity.grid(column = 1, row = 3, stick = tk.E)

#Create the label for "Angle"
#Place it just below Velocity (row = 4)
lblAngle = tk.Label(text = "Angle (degrees): ")
lblAngle.grid(column = 1, row = 4, stick = tk.W)

#Create the textbox for Angle with an INPUT field (tk.Entry)
#Place it right next to lblAngle (tk.E)
txtAngle = tk.Entry()
txtAngle.grid(column = 1, row = 4, stick = tk.E)

#Create a METHOD for Distance Traveled 
def distanceTraveled():
    #Get the number from the Velocity textbox (accept decimals)
    velocity = float(txtVelocity.get()) 
    #Get the degrees from the Angle textbox (accept decimals)
    originalAngle = float(txtAngle.get()) 
    #Convert the orignal angle to radians by multiplying with math.pi and dividing by 180
    newAngle = (originalAngle * math.pi) / 180 
    #See how much the projectile is moving up, vy = v * sin(angle)
    vY = velocity * math.sin(newAngle)
    #See how much the projectile is moving sideways, vx * cos(angle)
    vX = velocity * math.cos(newAngle) 
    #cCalculate the distance traveled, distance = vx * 2 * vy/9.8
    distance = (vX * 2 * vY) / 9.8
    #Change the text in lblDistance to show the results
    lblDistance["text"] = "Distance Traveled: " + str(distance)

#Create the BUTTON that performs the distanceTraveled method 
btnCalculate = tk.Button(text = "Calculate Distance", command = distanceTraveled)
btnCalculate.grid(column = 1, row = 6, pady = 20)

#Create the LABEL that will change when the distance is found
lblDistance = tk.Label(text = "")
lblDistance.grid(column = 1, row = 8)

