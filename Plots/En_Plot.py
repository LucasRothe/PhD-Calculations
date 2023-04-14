# python packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# convert cm to inch
def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)


# plot style
fig, ax = plt.subplots(figsize=(cm2inch(19.5,7.5))) #Werte für die exakte Breite des Word-Textfeldes!
#ax.grid()
ax.set(ylabel='G rel [kcal/mol]',
       xlabel='Reaction Coordinate',
       xlim = (-0.3, 4.3))

# Datenpunkte
# --<Start>-- #
plt.plot([-0.1,0.1],[0,0], c='black', lw="1")
# --<Strukturen>-- #
# -> Pyr-OMe mit BF4
plt.plot([0.9,1.1],[10.444262,10.444262], c='b', lw="1") # Edukt -> MA
plt.plot([1.9,2.1],[-1.791218,-1.791218], c='b', lw="1") # MA -> Diketon
plt.plot([2.9,3.1],[0.896635,0.896635], c='b', lw="1") # Diketon -> 4H-Pyran
plt.plot([3.9,4.1],[-30.675929,-30.675929], c='b', lw="1") # 4H-Pyran -> Pyryliumsalz + tChalkon
plt.plot([3.9,4.1],[-42.915172,-42.915172], c='b', lw="1") # 4H-Pyran -> Pyryliumsalz + Ph3COh




# -> TPP mit BF4
plt.plot([0.9,1.1],[-3.326678127,-3.326678127], c='r', lw="1") # Edukt -> MA
plt.plot([1.9,2.1],[0.241395742,0.241395742], c='r', lw="1") # MA -> Diketon
plt.plot([2.9,3.1],[1.796698896,1.796698896], c='r', lw="1") # Diketon -> 4H-Pyran
plt.plot([3.9,4.1],[-39.23501565,-39.23501565], c='r', lw="1") # 4H-Pyran -> Pyryliumsalz + tChalkon
plt.plot([3.9,4.1],[-51.47425821,-51.47425821], c='r', lw="1") # 4H-Pyran -> Pyryliumsalz + Ph3COh

# --<TS>-- #


# --<Dashed-Lines>-- #
# Edukt -> MA
plt.plot([0.1,0.9],[0,10.444262], c='black', ls="--", lw="0.5")
plt.plot([0.1,0.9],[0,-3.326678127], c='black', ls="--", lw="0.5")
# MA -> Diketon
plt.plot([1.1,1.9],[10.444262,-1.791218], c='black', ls="--", lw="0.5")
plt.plot([1.1,1.9],[-3.326678127,0.241395742], c='black', ls="--", lw="0.5")
# Diketon -> 4H-Pyran
plt.plot([2.1,2.9],[-1.791218,0.896635], c='black', ls="--", lw="0.5")
plt.plot([2.1,2.9],[0.241395742,1.796698896], c='black', ls="--", lw="0.5")
# 4H-Pyran -> Pyryliumsalz
# >tChalkon<
plt.plot([3.1,3.9],[0.896635,-30.675929], c='green', ls="--", lw="0.5")
plt.plot([3.1,3.9],[1.796698896,-39.23501565], c='green', ls="--", lw="0.5")
# >Ph3COH<
plt.plot([3.1,3.9],[0.896635,-42.915172], c='orange', ls="--", lw="0.5")
plt.plot([3.1,3.9],[1.796698896,-51.47425821], c='orange', ls="--", lw="0.5")

# output
#plt.plot(data0[:,0],data0[:,1],linewidth=1,marker="1",color="red",label="Pyr_vac")


#xcoords = range(data0["x"].min().astype(int),data0["x"].max().astype(int),100)
#for xc in xcoords:
#    plt.axvline(x=xc, linestyle=":", linewidth=0.25, color="gray")

# legende in plot
#plt.legend(fontsize="small")

# legende over plot
#plt.legend(fontsize="x-small",bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=5, mode="expand", borderaxespad=0.)

# save plot
plt.savefig(r"C:\Users\Lukas\sciebo\Promotion_Lucas\PyPlots\Plots\En_Dia\plotname"
            r".png",
            dpi=400,
            bbox_inches="tight",
            pad_inches=0)
