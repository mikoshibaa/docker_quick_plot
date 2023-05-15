import numpy as np
import matplotlib.pyplot as plt
import scipy

if __name__ == "__main__":
    fig, ax = plt.subplots()
    
    x = np.arange(0,10,0.01)
    y = np.sin(x)

    ax.plot(x,y)
    plt.savefig("sin.png")