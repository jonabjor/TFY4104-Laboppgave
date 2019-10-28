from eksternlab import height, slope, curvature
import numpy as np
import matplotlib.pyplot as plt

def get_time(x, y):

    he = height(x,y) 
    x_interp = np.linspace(0.0, 1.4, 10000)
    alpha = slope(he, x_interp)
    kappa = curvature(he, x_interp)
    N = 10000  # antall steg
    h = 0.002  # stegstørrelse

    # initialverdier
    t_0 = 0
    v_0 = 0
    x_0 = 0
    v_x_0 = 0
    no_0 = 0
    f_0 = 0

    # konstant g/(1+(I_0/mr^2)) for kula
    K = 7.007143
    m = 0.03
    g = 9.81
    c = 2/5

    #kappa = curvature(he_acc, x_interp)
    # alpha funksjonen a(x)
    a = height(x_interp, alpha)
    k = height(x_interp, kappa)

    t = np.zeros(N+1)
    v = np.zeros(N+1)
    x = np.zeros(N+1)
    v_x = np.zeros(N+1)
    no = np.zeros(N+1)
    f = np.zeros(N+1)

    t[0] = t_0
    v[0] = v_0
    x[0] = x_0
    v_x[0] = v_x_0
    no[0] = no_0
    f[0] = f_0

    t_old = t_0
    v_old = v_0
    x_old = x_0
    no_old = no_0
    f_old = f_0

    for n in range(N):
        v_new = v_old + h*(K*(np.sin(a(x_old))))  # Euler's method
        v_x_new = v_new*np.cos(a(x_old))
        x_new = x_old + h*(v_new*np.cos(a(x_old)))

        aks = K*(np.sin(a(x_old)))

        f_new = m*g*np.sin(a(x_old)) - m*aks
        no_new = m*g*np.cos(a(x_old)) + m*v_new**2*k(x_old)

        t[n+1] = t_old+h
        v[n+1] = v_new
        x[n+1] = x_new
        v_x[n+1] = v_x_new
        f[n+1] = f_new
        no[n+1] = no_new

        t_old = t_old+h
        v_old = v_new
        x_old = x_new
        if x_old >= 1.4:
            t_ans = t_old-h
            N = n
            break

    t = t[: N]
    x = x[: N]
    v_x = v_x[: N]
    f = f[: N]
    no = no[: N]
    
    return x, v, t_ans, t, v_x, f, no

'''
x_a, v_a, t_ans_a, t_plot_a, v_x_a = get_time(y_a)
x_b, v_b, t_ans_b, t_plot_b, v_x_b = get_time(y_b)
x_c, v_c, t_ans_c, t_plot_c, v_x_c = get_time(y_c)


x_b = x_b[:600]
t_plot_b = t_plot_b[:600]

plt.figure()
plt.plot(t_plot_a,x_a, color="black", label="Bane A, "r'$t=1.13s$')
plt.plot(t_plot_b,x_b, color="red", label="Bane B, "r'$t=0.84s$')
plt.plot(t_plot_c,x_c, color="blue", label="Bane C, "r'$t=1.586s$')
plt.legend(loc="lower right")
plt.title("Numerisk resultat (x-forflytning)")
plt.ylabel(r'$x [m]$')
plt.xlabel(r'$t [s]$')
plt.xlim(0,1.9)
plt.ylim(0,1.440)
plt.grid()
plt.show()
'''