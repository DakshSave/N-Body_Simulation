#Import Necessary Libraries.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



#Define Class For Body.
class Body:
    def __init__ (self, posx, posy, posz, mass, radius):
        self.position = np.array([posx, posy, posz])
        self.velocity = np.array([0.0, 0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0, 0.0])
        self.mass = mass
        self.radius = radius
        self.area = 4 * 3.14 * (radius*radius)



#Create Linear Space For Random Positioning.
space = np.linspace(start = _, stop = _, num = 10000) #Replace underscores with desired values of start and stop of linear space (will determine positioning of bodies).



#Create Empty List To Store Bodies.
bodies = []



#Create Variable(s) For Body(ies).
N = range(_) #Replace underscore with desired number of bodies.
for n in N:
   body = Body(posx = np.random.choice(space), posy = np.random.choice(space), posz = np.random.choice(space), mass = _, radius = _) #Replace underscores with desired values of mass and radius.
   bodies.append(body)



#Create Variable For Gravitational Constant (G).
G = 1 #Gravitational Constant = 6.674e-11, replaced here by 1 to speed up simulation process.



#Create A Variable For The Length Of Time Step.
dt = _ #Replace underscore with desired length of time step (preferably use 0.1, 0.01 or 0.001).



#Create Variable For Number Of Time Steps (dt).
steps = range(_) #Replace underscore with desired number of steps.



#Create Empty Arrays To Store Path History.
path = []
for body in bodies:
  path.append([])



#Main Simulation Loop.
for step in steps:
  #Reset Acceleration To 0 Every Iteration.
  for body in bodies:
    body.acceleration = np.array([0.0, 0.0, 0.0])
  #Form Pairs Of Bodies And Calculate Factors.  
  for i in range(len(bodies)):
    for j in range(i+1, len(bodies)):
      b1, b2 = bodies[i], bodies[j]
      epsilon = 0.5 #Softening Term
      d = np.sqrt(((b1.position[0]-b2.position[0])**2) + ((b1.position[1]-b2.position[1])**2) + ((b1.position[2]-b2.position[2])**2) + epsilon**2) #Distance From b1 To b2.
      r_vector = b2.position - b1.position #Vector From b1 To b2.
      r_hat = r_vector/d #Unit Direction Vector.
      F_magnitude = G * ((b1.mass*b2.mass) / (d*d)) #Magnitude Of Gravtational Force.
      F_vector = F_magnitude * r_hat #Vector Of Force.
      b1.acceleration += F_vector / b1.mass #Calculate And Update Acceleration Of b1.
      b2.acceleration -= F_vector / b2.mass #Calculate And Update Acceleration Of b2.
  #Calculate And Update Velocity And Position.  
  for body in bodies:
      body.velocity += body.acceleration * dt
      body.position += body.velocity * dt
  #Append Position Of Bodies On Every Step To Path.
  for i, body in enumerate(bodies):
      path[i].append(body.position.copy())



#Assign Animation Values And Variables.
trail_length = _ #Replace underscore with desired trail length.
colors = ["_", "_", "_"] #Replace underscores with desired colours (number of colours must be same as number of bodies).
lower_lim = _ #Replace underscore with desired lower limit (used to define figure size and axes limits).
upper_lim = _ #Replace underscore with desired upper limit (used to define figure size and axes limits).
fig = plt.figure(figsize=(-(lower_lim), upper_lim))
ax = fig.add_subplot(projection="3d")
scatters = [ax.scatter([], [], [], color=colors[i], s=bodies[i].area) for i in range(len(bodies))]
trails = [ax.plot([], [], [], color=colors[i], alpha=0.4, linewidth=0.8)[0] for i in range(len(bodies))]
ax.set_xlim(lower_lim, upper_lim)
ax.set_ylim(lower_lim, upper_lim)
ax.set_zlim(lower_lim, upper_lim)



#Main Animation Loop.
def update(frame):
    for i in range(len(bodies)):
        pos = path[i][frame]
        scatters[i]._offsets3d = ([pos[0]], [pos[1]], [pos[2]])
        start = max(0, frame - trail_length)
        t = np.array(path[i][start:frame+1])
        if len(t) > 1:
            trails[i].set_data(t[:, 0], t[:, 1])
            trails[i].set_3d_properties(t[:, 2])
    return scatters + trails
ani = animation.FuncAnimation(fig, update, frames=len(path[0]), interval=20, blit = False)
plt.tight_layout()
plt.show()
