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
	
	#----------------------		
	def __init__(self, dFolder, pFolder):
		if type(dFolder) is str:
			pth = os.path.join(pplot.cwd,dFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(dFolder)
			else:
				os.mkdir(dFolder)
			dataFolder = dFolder
		else:
			pth = os.path.join(pplot.cwd,pplot.dataFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(pplot.dataFolder)
			else:
				os.mkdir(pplot.dataFolder)
		if type(pFolder) is str:
			pth = os.path.join(pplot.cwd,pFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(pFolder)
			else:
				os.mkdir(pFolder)
			plotsFolder = pFolder
		else:
			pth = os.path.join(pplot.cwd,pplot.plotsFolder)
			if os.path.exists(pth):
				print 'WARNING: Folder \'%s\' already exists.' %(pplot.plotsFolder)
			else:
				os.mkdir(pplot.plotsFolder)
				
	#----------------------
	def plotXY(self,fName = None,SHOW = False):
		if fName is None:
			print 'Ploting with \'sampledata.dat\''
			x = linspace(-2*pi,2*pi,100,endpoint=True)
			y = cos(x)
			
			data = np.array(zip(x,y),dtype=dtype)
			np.savetxt('sampledata.dat',data,delimiter = '\t',newline='\n')
			

			pplot.ax.plot(x,y,label = r'$cos(\theta)$', color='#025167', lw = 2.0)
			pplot.ax.legend(loc = 3)

			xlim(x.min(),x.max())

			xticks = linspace(-6,6,5,endpoint=True)
			pplot.ax.set_xticks(xticks)

			ylim(-1.0,1.0)

			pplot.ax.set_xlabel(r'$\theta$', fontsize = 18)
			pplot.ax.set_ylabel(r'$y$', fontsize = 18)
			pplot.ax.set_title('Title')

			pplot.fig.savefig("sampleplotXY.png",dpi=72)

			if SHOW:
				show()		
			
	#----------------------				
	def showDoc(self):
		print trim.trim(doc)

	#----------------------			
	def saveDoc(self):
		out = open("documentation.txt","w")
		out.write(trim.trim(doc))			

plot = pplot(12,"pFolder")
plot.plotXY()
#fName = 'documentation.dat'
#x.saveDoc(fName)
