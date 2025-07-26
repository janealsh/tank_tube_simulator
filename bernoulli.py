import numpy as np

# units m
L = 0.2


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

def calculate_vp(height, friction_factor):
    pipe_vel_squared = (2 * g * (height + L / 150)) / (2.5 + ((L * friction_factor) / d_tube))
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
while height > 0:
    f = 0.01 # initial guess for f
    f_prev = -1 # stored f value

    # print("HEIGHT --> ", height)

    # Iterate for friction factor
    while abs(f - f_prev) > 0.0001:
        vp = calculate_vp(height, f)
        re = calculate_reynolds(vp)

        f_prev = f

        f = calculate_f(re, f_prev)
        #print("new f_prev (in loop) --> ", f)

        #print("DIFFERENCE: ", f, f_prev, f - f_prev)

    # print("this is f: ", f)
    # print(" ")

    final_vp = calculate_vp(height, f)

    drain_time += (step * a_tank) / (a_tube * final_vp) # dh divided by v2
    #print("drain_time -->", drain_time)

    height = round(height - step, 3) # Avoid floating point error

print(f"{int(drain_time // 60)}:{int(drain_time % 60)}")