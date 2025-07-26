import numpy as np

# units m
L = 0.2

# units kg/m^3
rho = 998

# units Ns/m^2
mu = 0.001003

# units m
# epsilon = 0.0000015

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

# 0.035904566293528936


def calculate_vp(height, friction_factor):
    pipe_vel_squared = (2 * g * (height + L / 150)) / (2.5 - (a_tube**2 / a_tank**2) + ((L * friction_factor) / d_tube))
    print("pipe velocity squared is -----------> ", pipe_vel_squared)
    pipe_velocity = np.sqrt(pipe_vel_squared)
    return pipe_velocity


def calculate_reynolds(velocity):
    return (rho * velocity * d_tube) / mu  # return reynolds number


# assuming material is plastic
e_over_d = 0.0015 / 7.94


# not working... in progress
def calculate_f(re):
    colebrook_RHS = -2.0 * np.log10((e_over_d / 3.7) + (2.51 / (re / np.sqrt(f))))
    return 1 / colebrook_RHS**2  # returns f


drain_time = 0

# iterate while decreasing height
while height > 0:
    f = 0.01 # initial guess for f
    f_prev = -1 # stored f value

    print("HEIGHT --> ", height)

    # Iterate for friction factor
    while abs(f - f_prev) > 0.01:
        vp = calculate_vp(height, f)
        re = calculate_reynolds(vp)

        f_prev = f

        f = calculate_f(re)
        print("new f_prev (in loop) --> ", f)

        print("DIFFERENCE: ", f, f_prev, f - f_prev)

    print("this is f: ", f)
    print(" ")


    # drain_time +=
    height -= step