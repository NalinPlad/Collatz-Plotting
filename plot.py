import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline


def collatz(start: int):
    if start <= 0:
        raise ValueError("Error! Positive, non-zero integers only")
    numOdd = 0
    numEven = 0
    count = 0
    yPos = [start]

    while start != 1:
        if start % 2 != 0:
            start = start * 3 + 1
            numOdd += 1
        else:
            start = start / 2
            numEven += 1
        yPos.append(start)
        count += 1
    return [yPos, count, numOdd, numEven]


def plot_coll(funcIn: list, hide_boxes=False, hide_text=False, advanced_stats=False, smooth=False):
    yPos = funcIn[0]
    count = funcIn[1]
    numOdd = funcIn[2]
    numEven = funcIn[3]

    fig, ax = plt.subplots(figsize=(6, 4))

    if not hide_boxes:
        for i, v in enumerate(yPos):
            ax.text(i, v, "%d" % v, ha="center", c="black", clip_on=True,
                    bbox=dict(boxstyle="round",
                              ec=(1., 0.5, 0.5),
                              fc=(1., 0.8, 0.8),
                              ))
        ax.axes.yaxis.set_ticks([])
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Calculated Value')

    ax.set_title('Collatz Conjecture Plot')

    if count < 100:
        plt.xticks(np.arange(0, count + 1, 1.0))
    plt.style.use('dark_background')

    props = dict(boxstyle='round', facecolor='red', alpha=0.5)
    if advanced_stats:
        textString = f"Starting Value: {yPos[0]}\n" \
                     f"Steps: {count}\n" \
                     f"Highest Value: {int(max(yPos))}\n" \
                     f"Num of Odd: {numOdd}\n" \
                     f"Num of Even: {numEven}"
    else:
        textString = f"Starting Value: {yPos[0]}\n" \
                     f"Steps: {count}\n" \
                     f"Highest Value: {int(max(yPos))}"
    if not hide_text:
        ax.text(0.05, 0.95, textString, transform=ax.transAxes, fontsize=14,
                verticalalignment='top', bbox=props)
    if smooth:
        print(type(yPos))
        # 300 represents number of points to make between T.min and T.max
        xnew = np.linspace(0, count, 300)
        spl = make_interp_spline(range(0,count+1),yPos, k=5)  # type: BSpline
        power_smooth = spl(xnew)

        ax.plot_coll(xnew, power_smooth)
        plt.show()
    else:
        ax.plot_coll(yPos, '-')
        plt.show()



