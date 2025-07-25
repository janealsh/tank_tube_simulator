import numpy as np


# in degrees
theta = np.arcsin(1/150);
theta_deg = theta * (180/np.pi)

# units m
a_tank = 0.32 * 0.26
d_tube = 0.00794

# units m^2
a_tube = np.square((d_tube/2)) * np.pi

# units m/s^2
g = 9.81

# assuming material is plastic

e_over_d = 0.0015/7.94 



print ("hello", theta_deg, "a_tube", a_tube)
