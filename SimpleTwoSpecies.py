import numpy as np
from scipy import integrate
import matplotlib.pylab as plt
import matplotlib.animation as animation
from IPython.display import HTML

def dX_dt(X, t, a,b,c,d):
    '''

    :param X:
    :param t:
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    '''
    return np.array([a * X[0] - b * X[0] * X[1],
                  -c * X[1] + d * X[0] * X[1]])

def LotkaVolterra(X0, params, t):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    if len(params) != 4:
        print("Params must be of length four!")

    sol = integrate.odeint(dX_dt, X0, t, args = (a,b,c,d))
    plt.plot(t, sol[:, 0], 'b', label='Prey')
    plt.plot(t, sol[:, 1], 'g', label='Predator')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    ###
    # we now want to animate the trajectories
    plt.rcParams['animation.writer'] = 'avconv'

    def random_ic(scalefac=2.0):  # generate initial condition
        return scalefac * (0.5 * abs(np.random.randn(2)) + 1)

    nlines = 10
    linedata = []
    for ic in [random_ic() for i in range(nlines)]:
        linedata.append(integrate.odeint(dX_dt, ic, t, args = (a,b,c,d)))

    fig = plt.figure()
    ax = plt.axes(xlim=(0, 30), ylim=(0, 30))
    line, = ax.plot([], [], 'ko', markersize=5, zorder= 10)
    traj, = ax.plot([],[],'ro', markersize=1, zorder= 2)
    npts = len(linedata[0][:, 0])

    def init():
        line.set_data([], [])
        traj.set_data([],[])
        return line, traj

    def animate(i):
        traj.set_data([l[0:i-1:3, 0] for l in linedata], [l[0:i-1:3, 1] for l in linedata])
        line.set_data([l[i, 0] for l in linedata], [l[i, 1] for l in linedata])
        return line, traj

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=npts, interval=15, blit=True)

    plt.title('Lotka-Volterra Trajectories')
    plt.xlabel('Prey')
    plt.ylabel('Predator')
    plt.show()

    return anim

params = [0.8, 0.1, 1.3, 0.2]
t = np.linspace(0, 15, 1000)  # time
X0 = np.array([10, 5])  # initials conditions: 10 rabbits and 5 foxes

LotkaVolterra(X0, params, t)
