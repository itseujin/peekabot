# Peekabot
My first end-to-end robotics project. Starting from scratch with derivations of equations of motion, simulations, and building real prototypes.

## Step 0: Deriving the Equations of Motion
Using my knowledge from the Mechanics component of Further Mathematics, I tried to derive the underlying equations of motion for this inverted pendulum connected to a smooth cart under it. However, halfway through I realised this is a bigger problem that I am not equiped to tackle. I researched for the concepts of tangential acceleration, and followed YouTube videos to further aid in my visualisation of this problem. I found the positive and negative signs challenging to grasp. In the end, I managed to reach the final 2 equations that describe the motion of the weight at the top of the pendulum, given a force acting on the cart. The picture of my derivation can be found in /docs

## Step 1: Simulating with a=0
Imported numpy and pyplot to calculate and test the equations of motion in code. I assumed radius of the pendulum was 1m, and acceleration to be 0.0 for now. One part that confused me for a while was the difference between angle and theta in my code. We always assume vertically upwards is 0 degrees, and any displacement left or right is the theta.

In my initial test simulations, I measured the period when it was hanging below the horizontal. 'angle' in my code simply means the displacement left or right against the vertically *downwards* direction.

I made the hard time limit of 20 seconds for the pendulum simulation to run. In the while loop, I implemented my derived equations, and saved all the values in an array for me to plot afterwards. This confirmed my equations were working correctly.

## Step 2: Simulating the Proportional & Derivative gain Controller
I started fresh, knowing my equations worked. I did research and knew I needed a controller formula to adjust my acceleration to move the cart. I came across Proportional gain and Derivative gain tuning knobs that will give me my expression for acceleration. Great! I implemented it, and also modified the code to store x and v for the cart.

In order to help visualise my simulation, I went to the internet to figure out how to animate all the data that I have simulated. I used parts of matplotlib to make the window and draw text & lines, draw shapes, and call drawing functions to animate the motion.

My simulation in the while loop already finished the calculations for all the positions of both the cart and the thetas. ***The animation just replays the saved numbers in the lists.***
### Cart moving to infinity at constant speed
What I noticed in the simulation was that the cart kept moving after the pendulum was steady. I'm assuming this is because I never considered where I want the cart to be, just whether theta is 0 or not. Once theta is 0, the cart can continue on to infinity at constant speed and it will still satisfy my equations.

This led me into a topic called ***full-state feedback***, where I feed the cart's position x and speed v to the controller as well. This gave me the idea of manipulating where the cart "parks" by changing the input of x in the controller to x minus position, where position is anywhere on the 1d number line you want the cart to rest at.

### Tuning the controller & other Experiments
In /docs I have a picture of my further equations I derived for the fine-tuning of Kd and Kp terms in my controller. I noticed my current simulations of the cart kept moving left and right about the position for a very long time. I learnt about the concept of critical damping from A-Level physics, and was overjoyed when I realised it can be applied here.

Through trial and error, so far I found that the input Kp of 25 in my equations produced a very smooth feel.

Furthermore, given a maximum acceleration limit (from the motors I will use) I needed to find the largest lean the system can still recover from. This problem is also in /docs

The real interesting part was adding a sudden impulse to the theta_d, meaning the angular velocity of the pendulum. This would equate to me physically pushing the pendulum in real life. I wanted a simulation to predict how my system would react.


# Learning materials I found useful
Detailed explanations of PD Controllers, their block diagrams, and the pros and cons of PD Controllers:
- https://youtu.be/Yc0VDIrsNnA?si=sh2tcsMZHpy7kVMJ

Mechanical Vibrations, Damping equations and graphs:
- https://youtu.be/CTd1uVq5-l8?si=96R_yTQJHkJNG4Ri