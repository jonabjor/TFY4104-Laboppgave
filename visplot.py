import matplotlib.pyplot as plt

def plotShow(x, y, color, label, gtitle, ylabel, xlabel, xlim, ylim, legendloc, save, figname):
    plt.figure()
    for i in range(len(y)):
        plt.plot(x[i],y[i], color=color[i], label=label[i])
    plt.legend(loc=legendloc)
    plt.title(gtitle)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xlim(xlim[0],xlim[1])
    plt.ylim(ylim[0],ylim[1])
    plt.grid()
    if save:
        plt.savefig(figname)
    else:
        plt.show()