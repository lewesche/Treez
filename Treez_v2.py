import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tree

#Enviromental Variables
bgColor = 'black'
time = 18 			#For mp4 saving purposes
numTrees = 8

print("Running")
# Create new Figure with black background
fig = plt.figure(figsize=(16, 8), facecolor=bgColor)

# Add a subplot with no frame
ax = plt.subplot(111, frameon=False)
Xdim = 800
Ydim = 400

T=[]
for i in range(0, numTrees):
	X0 = -Xdim/2 + Xdim/(2*numTrees) + i*Xdim/numTrees
	T.append(tree.Tree(120, 50, 12, 1.2, X0, Xdim, Ydim, 2))

def init():
    ax.set_xlim(-Xdim/2-10, Xdim/2+10)
    ax.set_ylim(-Ydim/2-10, Ydim/2+10)
    ax.set_xticks([])
    ax.set_yticks([])
    # Title
    ax.text(0.44, 1.0, "Treez", transform=ax.transAxes,
        ha="center", va="bottom", color=np.random.randint(101, size=3)/100,
        family="sans-serif", fontweight="bold", fontsize=22)
    ax.text(0.49, 1.0, "by", transform=ax.transAxes,
        ha="center", va="bottom", color=np.random.randint(101, size=3)/100,
        family="sans-serif", fontweight="light", fontsize=18)
    ax.text(0.52, 1.0, "Leif", transform=ax.transAxes,
        ha="center", va="bottom", color=np.random.randint(101, size=3)/100,
        family="sans-serif", fontweight="light", fontsize=18)
    ax.text(0.57, 1.0, "Wesche", transform=ax.transAxes,
        ha="center", va="bottom", color=np.random.randint(101, size=3)/100,
        family="sans-serif", fontweight="light", fontsize=18)
    return []

#Animation Function
def update(*args):
	artists = []
	for i in range(0, numTrees):
		T[i].newBranch()
		T[i].growBranch()
		T[i].killBranch()
		artists += T[i].lines
	return artists


fig.subplots_adjust(left=0, right=1, top=0.95, bottom=0)

anim = animation.FuncAnimation(fig, update, interval=30, frames=time*30, init_func=init, blit=True)

#Uncomment this next line to save an animation
anim.save('Treez_med.mp4', fps=30, extra_args=['-vcodec', 'libx264'],  savefig_kwargs={'facecolor':bgColor})

plt.show()
