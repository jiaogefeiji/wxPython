import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

from matplotlib.ticker import MultipleLocator, FuncFormatter

if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlim(0.1, 10)
    ax1.set_ylim(0.1, 100)
    ax1.set_aspect(1)
    ax1.set_title("adjustable = box")
    # 设置轴的主刻度
    # x轴
    ax1.xaxis.set_major_locator(MultipleLocator(0.1))  # 设置20倍数
    #ax1.xaxis.set_major_formatter(FormatStrFormatter('%5.1f'))  # 设置文本格式

    # y轴
    ax1.yaxis.set_major_locator(MultipleLocator(10))  # 设置100倍数
    #ax1.yaxis.set_major_formatter(FormatStrFormatter('%1.2f'))  # 设置文本格式

    # 设置轴的副刻度
    # x轴
    ax1.xaxis.set_minor_locator(MultipleLocator(0.1))  # 设置10倍数
    # ax.xaxis.set_minor_formatter(FormatStrFormatter('%2.1f'))  # 设置文本格式

    # y轴
    ax1.yaxis.set_minor_locator(MultipleLocator(1))  # 设置50倍数
    # ax.yaxis.set_minor_formatter(FormatStrFormatter('%1.0f'))  # 设置文本格式

    # 设置网格
    ax1.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax1.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_adjustable("datalim")
    ax2.plot([1, 3, 10], [1, 9, 100], "o-")
    ax2.set_xlim(1e-1, 1e2)
    ax2.set_ylim(1e-1, 1e3)
    ax2.set_aspect(1)
    ax2.set_title("adjustable = datalim")

    plt.show()