import numpy as np
import matplotlib.pyplot as plt
import random
import secrets
import copy




class Tree:

	def __init__(self, MaxAge, alpha, minBranches, Vmax, X0, Xdim, Ydim, lw):
		self.ax = plt.subplot(111, frameon=False)
		self.MaxAge = MaxAge
		self.alpha = alpha
		self.minBranches = minBranches
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
		self.Xdir.append((secrets.randbelow(101)-50)/400)
		self.Ydir.append((secrets.randbelow(81)+20)/100)
		self.Age.append(1)
		self.colors.append(np.random.randint(101, size=3)/100)
		line, = self.ax.plot(self.X[0], self.Y[0], 'o-', color=self.colors[0], lw=self.lw)
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
				line, = self.ax.plot(self.X[-1], self.Y[-1], 'o-', color=self.colors[-1], lw=self.lw)
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
			elif abs(self.X[j][-1])>self.Xdim/2 or abs(self.Y[j][-1])>self.Ydim/2:
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