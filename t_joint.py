import matplotlib.pyplot as plt
import numpy as np

# units m
lengths = [0.2, 0.3, 0.4, 0.6]
experiment_drain_times = [180 + 19, 180 + 34, 240 + 26, 240 + 48]

# units kg/m^3 (water density)
rho = 998

# units Ns/m^2 (water viscosity)
mu = 0.001003

# units degrees
theta = np.arcsin(1 / 150)
theta_deg = theta * (180 / np.pi)

# units m
a_tank = 0.32 * 0.26
d_tube = 0.00794

# units m^2
a_tube = ((d_tube / 2) ** 2) * np.pi

# units m/s^2
g = 9.81
height = 0.08  # units m
step = 0.001

drain_times = []

def calculate_vp(height, friction_factor, L):
    pipe_vel_squared = (2 * g * (height + (L / 150))) / (1.5 - (a_tube**2 / a_tank**2) + ((L * friction_factor) / d_tube))
    # print("pipe velocity squared is -----------> ", pipe_vel_squared)
    pipe_velocity = np.sqrt(pipe_vel_squared)
    return pipe_velocity

def calculate_reynolds(velocity):
    return (rho * velocity * d_tube) / mu  # return reynolds number

# assuming material is plastic
e_over_d = 0.0015 / 7.94

# colebrook equation iteration
def calculate_f(re, f):
    colebrook_RHS = -2.0 * np.log10((e_over_d / 3.7) + (2.51 / (re * np.sqrt(f))))
    return 1 / colebrook_RHS**2  # returns f

drain_time = 0

# iterate while decreasing height
for L in lengths:
  while height > 0:
      f = 0.02 # initial guess for f
      f_prev = -1 # stored f value

      # print("HEIGHT --> ", height)
      vp_guess = np.sqrt((2 * g * (height + (L / 150))) / (1.5 - (a_tube**2 / a_tank**2)))
      re = calculate_reynolds(vp_guess)

      if re < 2300:
        f = 64 / re
      else:
        vp = calculate_vp(height, f, L)
        re = calculate_reynolds(vp)
        # Iterate for friction factor
        while abs(f - f_prev) > 0.0001:
            f_prev = f
            f = calculate_f(re, f_prev)
            #print("new f_prev (in loop) --> ", f)
            #print("DIFFERENCE: ", f, f_prev, f - f_prev)
            vp = calculate_vp(height, f, L)
            re = calculate_reynolds(vp)

      # print(" ")

      final_vp = calculate_vp(height, f, L)

      t_step = (step * a_tank) / (a_tube * final_vp)
      drain_time += t_step # dh divided by v2
      #print("drain_time -->", drain_time)

      height = round(height - step, 3) # Avoid floating point error

  print(f"{L} {int(drain_time // 60)}:{int(drain_time % 60)}")
  drain_times.append(drain_time)

  height = 0.08
  drain_time = 0

np_lengths = np.array(lengths) * 100
np_times = np.array(drain_times) / 60
np_experiment_times = np.array(experiment_drain_times) / 60

line1 = plt.plot(np_lengths, np_times, marker='o', label="Calculated Values")
plt.plot(np_lengths, np_experiment_times, marker='o', label="Experimental Average")
plt.fill_between(np_lengths, np_times, np_experiment_times, color='lightgray', alpha=0.4, label='Difference')

plt.xlabel("Tube Length (cm)")
plt.ylabel("Drain Time (min)")
plt.legend()
plt.grid(True)
plt.show()