#HW3 Week 3
#Air Speed
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from matplotlib import cm
import matplotlib.colors as colors
if __name__=='__main__':
    filenm = 'PIXHAWKPOSITION.csv'
    df = pd.read_csv('/opt/miniconda3/envs/PY101/Week3/to_ev/'+filenm)
    df['msec'] = df['nsec'] / 5000_0000
    df['msec'] = df['msec'].astype('int')
    filenm = 'PIXHAWKAIRSPEED.csv'
    dfa = pd.read_csv('/opt/miniconda3/envs/PY101/Week3/to_ev/'+filenm)
    dfa['msec'] = dfa['nsec'] / 5000_0000
    dfa['msec'] = dfa['msec'].astype('int')
    print(dfa.columns)
    dfa = dfa.rename(columns={'Unnamed: 11':'speed'})
    dfa['speed'] = dfa['speed'].rolling(window=100).mean()
    dfa = dfa[['sec','speed','msec']]
    df_new = df.merge(dfa,on=['msec','sec'])
    len(df_new) #5911 Too much overlap at n = 1000_000_00
    fig = plt.figure("3D UAS")
    ax = fig.add_subplot(111, projection='3d')
    norm = colors.Normalize(df_new.speed.min(),df_new.speed.max())
    Colors = cm.plasma(norm(df_new.speed.to_numpy()))
    ax.scatter3D(xs=df_new.latitude, ys=df_new.longitude, zs=df_new.altitude , c=Colors)
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_zlabel('Altidue')
    plt.show()
