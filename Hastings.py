import numpy as np
from scipy import integrate
import matplotlib.pylab as plt
import matplotlib.animation as animation

def dX_dt(X, t, a, b, c , d, e ,f):


    return np.array([ X[0]*(1 - X[0]) - a*(X[0]*X[1])/(1 + b*X[0]),
                    (-e*X[1] + (a*X[0]*X[1])/(1 + b*X[0]) - c*(X[2]*X[1])/(1 + d*X[1])),
                    - f*X[2] + c*(X[1]*X[2])/(1 + d*X[1])])


# animation function.  This will be called sequentially with the frame number


def Hastings(X0, params, t):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    e = params[4]
    f = params[5]

    if len(params) != 6:
        print("Params must be of length six!")

    sol = integrate.odeint(dX_dt, X0, t, args=(a, b, c, d, e, f), rtol=10**-8)
    plt.figure()
    plt.plot(t[50:-6000], sol[50:-6000, 0], 'b', label='Prey')
    plt.plot(t[50:-6000], sol[50:-6000, 1], 'g', label='Predator')
    plt.plot(t[50:-6000], sol[50:-6000, 2], 'g', label='Super-Predator')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol[50:-6000, 0], sol[50:-6000, 1], sol[50:-6000, 2],'b')
    ax.legend(loc='best')
    ax.grid()
    ax.set_xlabel('Prey')
    ax.set_ylabel('Predator')
    ax.set_zlabel('Super-Predator')
    ax.set_title('Hastings Lotka-Volterra Model')
    plt.show()

    ###
    # we now want to animate the trajectories


    x = sol[:,0]
    y = sol[:,1]
    z = sol[:,2]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    ax.set_xlabel('Prey')
    ax.set_ylabel('Predator')
    ax.set_zlabel('Super-Predator')
    ax.set_title('Hastings Lotka-Volterra Model')
    ax.set_xlim(-0.1, 1)
    ax.set_ylim(-0.1, 1)
    ax.set_zlim(0, 13)

    lines = []
    for i in range(len(t)):
        head = i - 1
        head_slice = (t > t[i] - 1.0) & (t < t[i])
        line1, = ax.plot(x[:i], y[:i], z[:i],
                          color='black', alpha =0.5)
        line1a, = ax.plot(x[head_slice], y[head_slice], z[head_slice],
                           color='red', linewidth=2)
        line1e, = ax.plot([x[head]], [y[head]], [z[head]],
                           color='red', marker='o', markeredgecolor='r')
        lines.append([line1, line1a, line1e,])

    plt.tight_layout()
    ani = animation.ArtistAnimation(fig, lines, interval= 5, blit=True)
    plt.show()
    # sample params: params = [5, 2, 0.1, 2, 0.4, 0.01]

params = [5, 3, 0.1, 2, 0.4, 0.01]
t = np.linspace(0, 2500, 10000)  # time
X0 = np.array([1, 0.19, 10])

Hastings(X0, params, t)
