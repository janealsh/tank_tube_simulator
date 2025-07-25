import numpy as np


# in degrees
theta = np.arcsin(1/150);
theta_deg = theta * (180/np.pi)

# units below in meters
tank_a = 0.32 * 0.26

tube_d = 0.00794

print ("hello", theta_deg)
