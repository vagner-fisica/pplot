from pylab import *
import matplotlib.pyplot as plt
import os, trim

doc = \
		'-------------------------------------------\n'\
		'pplot class\n'\
		'Developed by Vagner Bessa.\n'\
		'Contact: vagner.fisica@gmail.com.\n\n'\
		'Check README file for main informations.\n\n'\
		'This module has the MIT License (MIT)\n'\
		'Copyright (c) 2014 Vagner Bessa.\n'\
		'-------------------------------------------\n'
def lzeros(nzeros, idx):
	s = ("%0" + str(nzeros) + "d")  % (idx)
	return s
class pplot:
	#----------------------
	"""pplot class: developed by Vagner Bessa. Contact: vagner.fisica@gmail.com. For more information, use 'showDoc()' method or saveDoc() and check documentation.txt file."""
	
	#----------------------
	dataFolder = "dataFolder"
	plotsFolder = "plotsFolder"
	cwd = os.getcwd()
	fig = plt.figure(figsize=(6,6), dpi=80)
	frameDim = [0.1,.1,.8,.8]
	ax = fig.add_axes(frameDim)
	yLabel = r'$cos(\theta)$'
	
	#----------------------		
	def __init__(self, dFolder = "dataFolder", pFolder = "plotsFolder"):
		if type(dFolder) is str:
			pth = os.path.join(self.cwd,dFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(dFolder)
			else:
				os.mkdir(dFolder)
			self.dataFolder = dFolder
		else:
			pth = os.path.join(self.cwd,self.dataFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(self.dataFolder)
			else:
				os.mkdir(self.dataFolder)
		if type(pFolder) is str:
			pth = os.path.join(self.cwd,pFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(pFolder)
			else:
				os.mkdir(pFolder)
			self.plotsFolder = pFolder
		else:
			pth = os.path.join(self.cwd,self.plotsFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(self.plotsFolder)
			else:
				os.mkdir(self.plotsFolder)

	#----------------------				
	def plotfname(self,f):
		f = os.path.join(self.plotsFolder,f)
		return f	
	def datafname(self,f):
		f = os.path.join(self.dataFolder,f)
		return f				
	#----------------------
	def plotXY(self,fName = None,SHOW = False):
		if fName is None:
		
			dataname = self.datafname('sampledataXY.dat')
			plotname = self.plotfname("sampleplotXY.png")
			
			print "Ploting with \'%s\'" %(dataname)
			
			x = linspace(-2*pi,2*pi,100,endpoint=True)
			y = cos(x)
			
			data = np.array(zip(x,y),dtype=dtype)
			np.savetxt(dataname,data,delimiter = '\t',newline='\n')
			
			self.ax.plot(x,y,label = self.yLabel, color='#025167', lw = 2.0)
			self.ax.legend(loc = 3)

			xlim(x.min(),x.max())

			xticks = linspace(-6,6,5,endpoint=True)
			self.ax.set_xticks(xticks)

			ylim(-1.0,1.0)

			self.ax.set_xlabel(r'$\theta$', fontsize = 18)
			self.ax.set_ylabel(r'$y$', fontsize = 18)
			self.ax.set_title('Title')
			
			
			self.fig.savefig(plotname,dpi=72)
			
			print "Plot saved at \'%s\'" %(plotname)
			
			if SHOW:
				show()		
				
	#----------------------				
	def showDoc(self):
		print trim.trim(doc)

	#----------------------			
	def saveDoc(self):
		out = open("documentation.txt","w")
		out.write(trim.trim(doc))			

#plot = pplot()
#plot.plotXY(SHOW = True)
#fName = 'documentation.dat'
#x.saveDoc(fName)
