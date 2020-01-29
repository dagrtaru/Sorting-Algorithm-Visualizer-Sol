import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys


fig, graph = plt.subplots()

def plot(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, align='edge', width=1, data=arr)
    plt.pause(0.001)


def on_close(event):
    if not sys.argv[0] == 'test.py':
        sys.exit(0)

def call(arr):
    plt.bar(range(len(arr)), arr, align='edge', width=1, data=arr)

def show():
    #My approach to speed up the plotting process would be to use matplotlib's animation. Following is a partially wrong implementation. Uncomment it to run...
    #myAnimation = animation.FuncAnimation(fig, call, interval=5, blit=True, repeat=True)
    plt.show()



fig.canvas.mpl_connect('close_event', on_close)
graph.yaxis.set_visible(False)
graph.xaxis.set_visible(False)
