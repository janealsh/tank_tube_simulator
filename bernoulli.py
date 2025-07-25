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

def calculate_vp(height, friction_factor):
  return np.sqrt((2 * g * (height + L/150)) / (1 - (np.square(a_tube) / np.square(a_tank) + 1.5 + ((L * friction_factor) / d_tube))))

def calculate_reynolds(velocity):
  return (rho*velocity*d_tube)/mu # return reynolds number

# assuming material is plastic
e_over_d = 0.0015/7.94 

#not working... in progress
def calculate_f(re):
  colebrook_RHS = -2.0*np.log10((e_over_d/3.7) + (2.51/(re/np.sqrt(f))))
  return  1/colebrook_RHS**2 # returns f

drain_time = 0

# iterate while decreasing height
while height > 0:
  f_prev = 0.02 
  f = 0
#   vp = calculate_vp(height, f_prev)
#   stored_v = vp
#   re = calculate_reynolds(stored_v)
  while abs(f - f_prev) > 0.01:
    f = f_prev
    vp = calculate_vp(height, f)
    re = calculate_reynolds(f)
    f = calculate_f(re)
    # if (abs(f - f_prev) < 0.01): 
    #     break
    # f_prev = f

  print("this is f: ", f)

  #drain_time += 
  height -= step

print ("hello", theta_deg, "a_tube", a_tube)
