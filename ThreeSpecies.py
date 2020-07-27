import numpy as np
from scipy import integrate
import matplotlib.pylab as plt
import matplotlib.animation as animation


def dX_dt(X, t, a,b,c,d,e,f):

    return np.array([X[0]*(1 - X[0] - X[1] - X[2]),
                     X[1]*(-a + b * X[0] - c*X[2]),
                     X[2]*(-d + e*X[0] + f*X[1])])

def ThreeSpecies(X0, params, t):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    e = params[4]
    f = params[5]

    if len(params) != 6:
        print("Params must be of length four!")

    sol = integrate.odeint(dX_dt, X0, t, args = (a,b,c,d,e,f), rtol=10**-8)

    plt.plot(t, sol[:, 0], 'b', label='Prey')
    plt.plot(t, sol[:, 1], 'g', label='Predator')
    plt.plot(t, sol[:, 2], 'r', label='Super-Predator')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2], 'b')
    ax.grid()
    ax.set_xlabel('Prey')
    ax.set_ylabel('Predator')
    ax.set_zlabel('Super-Predator')
    ax.set_title('Three Species Model')
    plt.show()

    # we now want to animate the trajectories
    plt.rcParams['animation.writer'] = 'avconv'

## aa = -5 bb = 25 cc = 0.0400 dd =2 ee = 0.65 ff=1.3

params = [5, 32, 0.04, 2, 0.5, 1.3]
t = np.linspace(0, 500, 100000)  # time
X0 = np.array([0.1, 0.1, 0.1])

ThreeSpecies(X0, params, t)