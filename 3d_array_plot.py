import numpy as np
import matplotlib.pyplot as plt

def drawArr3d(tdarr):
    x22 = np.arange(-10, 10, 0.1)
    y22 = x22 ** 2
    plt.plot(x22, y22, c='w')
    for row in range(min(len(tdarr), 2)): # rows 0 and 1
        for col in range(min(len(tdarr[row]), 4)): # columns 0,1,2
            for z in range(min(len(tdarr[row][col]), 3)):  # z-index 0 and 1
                plt.text(-7 + col*3 + z*1.5, 60 - 55 * row + z*14, str(tdarr[row][col][z])[12:13], fontsize=50 - z*5, bbox = dict(facecolor = 'red', alpha = 0.5 - z*0.2))
    plt.show()
