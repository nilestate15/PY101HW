#HW1 Week 3
#Niles Tate
#HR: Ms.Evelyn


import pandas as pd  # For getting the data
import matplotlib.pyplot as plt # for plotting
from matplotlib import rc # for custom styling


def plot_ll(sec,altitude, title=None):
    font = {'family': 'serif', 'weight': 'normal', 'size': 12}
    rc('font', **font)
    (fig,ax) = plt.subplots(figsize=(16, 9))
    ax.grid(True)
    s = ax.scatter(sec, altitude)
    plt.xlabel('Time (sec)')
    plt.ylabel('Altitude (ft)')
    if title!=None:
        plt.title(title)
    #plt.show()
    return (fig, ax, s)

if __name__=='__main__':
  #step 1: Get data
  filenm = '/opt/miniconda3/envs/PY101/Week3/to_ev/PIXHAWKALTITUDE.csv'
  df = pd.read_csv(filenm, delimiter=",") #"," is the default
  # step 2-4 Create plot:
  fig, ax, s = plot_ll(df['sec'], df['altitude'], 'Test')
  ax.set_title("PIXHAWK ALT VS TIME")
  # step 5 save plot
  # step 6 show plot
  plt.show()
