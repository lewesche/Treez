import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import secrets
import copy

class Tree:

	def __init__(self, MaxAge, alpha, minBranches, maxWidth, Vmax, X0, Xdim, Ydim, lw):
		self.MaxAge = MaxAge
		self.alpha = alpha
		self.minBranches = minBranches
		self.maxWidth=maxWidth
		self.Vmax = Vmax
		self.X0 = X0
		self.Xdim = Xdim
		self.Ydim = Ydim
		self.lw = lw

		self.X = []
		self.Y = []
		self.Xdir = []
		self.Ydir = []
		self.Age = []
		self.colors = []
		self.lines=[]

		self.X.append([self.X0, self.X0])
		self.Y.append([-self.Ydim/2, -self.Ydim/2])
		self.Xdir.append((secrets.randbelow(101)-50)/200)
		self.Ydir.append((secrets.randbelow(81)+20)/100)
		self.Age.append(1)
		self.colors.append(np.random.randint(101, size=3)/100)
		line, = ax.plot(self.X[0], self.Y[0], 'o-', color=self.colors[0], lw=self.lw)
		self.lines.append(line)

	def newBranch(self):
		for j in range(0,len(self.X)):
			if self.X[j] is None:
				continue
			if secrets.randbelow(101) % self.alpha == 0:
				self.Age.append(1)
				self.X.append([self.X[j][-1], self.X[j][-1]])
				self.Y.append([self.Y[j][-1], self.Y[j][-1]])
				temp = copy.copy(self.colors[j])
				ind = secrets.randbelow(3)
				delta = (secrets.randbelow(121)-60)/200
				temp[ind] = temp[ind] + delta
				if temp[ind] > 1 or temp[ind] < 0:
					temp[ind] = temp[ind] - 2*delta
				self.colors.append(temp)
				self.Xdir.append(self.Xdir[j] + (secrets.randbelow(201)-100)/200)
				self.Ydir.append(self.Ydir[j] + (secrets.randbelow(151)-50)/200)
				if self.Ydir[-1] > self.Vmax:
					self.Ydir[-1] = self.Vmax
				if self.Xdir[-1] > self.Vmax:
					self.Xdir[-1] = self.Vmax
				elif self.Xdir[-1] < -self.Vmax:
					self.Xdir[-1] = -self.Vmax 
				line, = ax.plot(self.X[-1], self.Y[-1], 'o-', color=self.colors[-1], lw=self.lw)
				self.lines.append(line)

	def growBranch(self):
		for j in range(0,len(self.X)):
			if self.X[j] is None:
				continue
			self.X[j][-1] = self.X[j][-1] + self.Xdir[j]
			self.Y[j][-1] = self.Y[j][-1] + self.Ydir[j]
			self.lines[j].set_xdata(self.X[j])
			self.lines[j].set_ydata(self.Y[j])
			self.Age[j] += 1

	def killBranch(self):
		KillAge = self.MaxAge/(np.power(len(self.X), 1/4))
		for j in range(0,len(self.X)):
			if self.X[j] is None:
				continue
			elif abs(self.X[j][-1])>self.Xdim/2 or abs(self.Y[j][-1])>self.Ydim/2 or (self.X[j][-1])>(self.X0+self.maxWidth) or (self.X[j][-1])<(self.X0-self.maxWidth):
				self.Age[j] = None
				self.X[j] = None
				self.Y[j] = None
				self.Xdir[j] = None
				self.Ydir[j] = None
		for i in range(0, len(self.X)-self.minBranches):
			if self.X[i] is None:
				continue 
			elif self.Age[i]>KillAge:
				self.Age[i] = None
				self.X[i] = None
				self.Y[i] = None
				self.Xdir[i] = None
				self.Ydir[i] = None  















#Enviromental Variables
bgColor = 'black'
time = 18 			#For mp4 saving purposes

print("Running")
# Create new Figure with black background
fig = plt.figure(figsize=(16, 8), facecolor=bgColor)

# Add a subplot with no frame
ax = plt.subplot(111, frameon=False)
Xdim = 800
Ydim = 400

T1 = Tree(120, 50, 12, 1500, 1.2, -300, Xdim, Ydim, 2)
T2 = Tree(120, 50, 12, 1500, 1.2, -100, Xdim, Ydim, 2)
T3 = Tree(120, 50, 12, 1500, 1.2, 100, Xdim, Ydim, 2)
T4 = Tree(120, 50, 12, 1500, 1.2, 300, Xdim, Ydim, 2)

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
	T1.newBranch()
	T2.newBranch()
	T3.newBranch()
	T4.newBranch()

	T1.growBranch()
	T2.growBranch()
	T3.growBranch()
	T4.growBranch()

	T1.killBranch()
	T2.killBranch()
	T3.killBranch()
	T4.killBranch()

	return T1.lines + T2.lines + T3.lines +T4.lines


fig.subplots_adjust(left=0, right=1, top=0.95, bottom=0)

anim = animation.FuncAnimation(fig, update, interval=30, frames=time*30, init_func=init, blit=True)

#Uncomment this next line to save an animation
#anim.save('Treez.mp4', fps=30, extra_args=['-vcodec', 'libx264'],  savefig_kwargs={'facecolor':bgColor})

plt.show()
