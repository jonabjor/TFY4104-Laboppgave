from numerikkberegning import get_time
from visplot import plotShow
from eksperiment import eksp_data
from eksperimentfart import eks_speed
import matplotlib.pyplot as plt
def main():
    # x-verdier for baneprofilene
    x = [0, 0.20, 0.40, 0.60, 0.80, 1, 1.20, 1.40]

    # y-verdier for de tre baneprofilene
    y_a = [0.81, 0.74, 0.67, 0.60, 0.53, 0.46, 0.39, 0.32]
    y_b = [0.81, 0.39, 0.185, 0.095, 0.075, 0.1, 0.185, 0.32]
    y_c = [0.81, 0.78, 0.75, 0.71, 0.655, 0.585, 0.49, 0.32]

    x_a, v_a, t_ans_a, t_plot_a, v_x_a, f_a, no_a = get_time(x, y_a)
    x_b, v_b, t_ans_b, t_plot_b, v_x_b, f_b, no_b = get_time(x, y_b)
    x_c, v_c, t_ans_c, t_plot_c, v_x_c, f_c, no_c = get_time(x, y_c)
    '''
    # parametere for plotshow fra plotAndShow
    t = [t_plot_a, t_plot_b, t_plot_c]
    x = [x_a, x_b, x_c]
    color = ["black", "red", "blue"]
    label = ["Bane A", "Bane B", "Bane C"]
    gtitle = "Numerisk resultat Bane A, B og C"
    xlabel = r'$t [s]$'
    ylabel = r'$x [m]$'
    xlim = [0,1.9]
    ylim = [0,1.440]
    legendloc = "lower right"
    save = True
    figname = "numX.pdf"
    # kaller plowShow for x(t)
    plotShow(t, x, color, label, gtitle, ylabel, xlabel, xlim, ylim, legendloc, save, figname)

    # setup parametere for vx(t)
    v_x = [v_x_a, v_x_b, v_x_c]
    ylabel = r'$v [m/s]$'
    xlim = [0,1.6]
    ylim = [0,4]
    figname = "numV.pdf"
    # kaller plotShow for vx(t)
    plotShow(t, v_x, color, label, gtitle, ylabel, xlabel, xlim, ylim, legendloc, save, figname)

    # filinput for eksperimentell data. Dataverdier er hentet fra Tracker.
    filename = "input.csv"
    # kaller ekspdata
    t_A, x_A, t_B, x_B, t_C, x_C = eksp_data(filename)
    # setup parametere for plotShow
    t = [t_A, t_B, t_C]
    x = [x_A, x_B, x_C]
    ylabel = r'$x [m]$'
    xlim = [0,1.9]
    ylim = [0,1.440]
    gtitle = "Eksperimentelt resultat for Bane A, B og C"
    figname = "eksX.pdf"
    # kaller plowShow for x(t) (data fra eksperimentet)
    plotShow(t, x, color, label, gtitle, ylabel, xlabel, xlim, ylim, legendloc, save, figname)

    # kaller eks_speed() for å hente verdier for farten eksperimentelt
    v_A, v_B, v_C, t_A, t_B, t_C = eks_speed()
    # setup parametere
    t = [t_A, t_B, t_C]
    v = [v_A, v_B, v_C]
    ylabel = r'$v [m/s]$'
    xlim = [0,1.6]
    ylim = [0,4]
    figname = "eksV.pdf"
    # kaller plowShow for vx(t) (data fra eksperimentet)
    plotShow(t, v, color, label, gtitle, ylabel, xlabel, xlim, ylim, legendloc, save, figname)
    '''
    # parametere for friksjonskraft og normalkraft Bane A
    plt.figure()
    plt.plot(t_plot_a, f_a, color="black", label="Friksjonskraft")
    plt.plot(t_plot_a, no_a, color="blue", label="Normalkraft")
    plt.title("Normalkraft og friksjonskraft for Bane A")
    plt.legend()
    plt.ylabel("Kraft [N]")
    plt.xlabel("tid [s]")
    plt.xlim(0,1.5)
    plt.ylim(-0.2,0.5)
    plt.grid()
    plt.show()

    # parametere for friksjonskraft og normalkraft Bane B
    plt.figure()
    plt.plot(t_plot_b, f_b, color="black", label="Friksjon")
    plt.plot(t_plot_b, no_b, color="blue", label="Normalkraft")
    plt.title("Normalkraft og friksjonskraft for Bane B")
    plt.legend()
    plt.ylabel("Kraft [N]")
    plt.xlabel("tid [s]")
    plt.xlim(0,1)
    plt.ylim(-0.5,1)
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(t_plot_c, f_c, color="black", label="Friksjon")
    plt.plot(t_plot_c, no_c, color="blue", label="Normalkraft")
    plt.title("Normalkraft og friksjonskraft for Bane C")
    plt.legend()
    plt.ylabel("Kraft [N]")
    plt.xlabel("tid [s]")
    plt.xlim(0,1.7)
    plt.ylim(-0.5,0.7)
    plt.grid()
    plt.show()
main()
    