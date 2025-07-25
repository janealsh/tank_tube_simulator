import numpy as np

L = 20

# in kg/m^3
rho = 998

# in Ns/m^2
mu = 0.001003

# in m
epsilon = 0.0000015

# in degrees
theta = np.arcsin(1/150)
theta_deg = theta * (180/np.pi)

# units m
a_tank = 0.32 * 0.26
d_tube = 0.00794

# units m^2
a_tube = np.square((d_tube/2)) * np.pi

# units m/s^2
g = 9.81

height = 0.08 # units m

stored_v = 0

step = 0.001

def caclulate_pipe_velocity(height, friction_factor):
  return np.sqrt((2 * g * (height + L/150)) / (1 - (np.square(a_tube) / np.square(a_tank) + 1.5 + ((L * friction_factor) / d_tube))))

def calculate_reynolds(velocity):
  re = (rho*velocity*d_tube)/mu

# assuming material is plastic
e_over_d = 0.0015/7.94 

#not working... in progress
def calculate_f(re):
  colebrook_RHS = -2.0*np.log10((e_over_d/3.7) + (2.51/(re/np.sqrt(f))))
  f = 1/colebrook_RHS**2

def iterate_f():
  

# iterate while decreasing height
while height > 0:
  f = 0.02 
  vp = caclulate_pipe_velocity(height, f)
  stored_v = vp
  re = calculate_reynolds(stored_v)

  height -= step

print ("hello", theta_deg, "a_tube", a_tube)
