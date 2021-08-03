import matplotlib.pyplot as plt
import numpy as np


def plot(start: int, hide_boxes: bool):
    if start <= 0:
        raise ValueError("Error! Positive, non-zero integers only")

    count = 0
    yPos = [start]

    while start != 1:
        if start % 2 != 0:
            start = start * 3 + 1
        else:
            start = start / 2
        yPos.append(start)
        count += 1

    fig, ax = plt.subplots(figsize=(20, 6))
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
    ax.plot(yPos, '-')
    plt.style.use('seaborn-whitegrid')
    plt.show()


plot(27, True)
plot(9, False)
