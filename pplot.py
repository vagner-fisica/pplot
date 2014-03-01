from pylab import *
import matplotlib.pyplot as plt
import os, trim

doc = open('documentation.txt','r').read()

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
	
	xDimPLot = 6
	yDimPlot = 6
	fig = plt.figure(figsize = (xDimPLot,yDimPlot), dpi = 80)
	frameDim = [0.1,.1,.8,.8]
	pXY = fig.add_axes(frameDim)
	yLabel = r'$y(x)$'
	xLabel = r'$x$'
	
	dataname = 'dataname.dat'
	plotname = 'sampleplotXY.png'
	
	X = []
	Y = []
	Z = []
	
	XY = []
	XYZ = []
	
	matrix = []
	
	colorDict = {'pblue':'#025167'}
	
	#----------------------		
	def __init__(self, dFolder = "dataFolder", pFolder = "plotsFolder"):
		"""Create the folder to work in.
		"""
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
		"""Return path to file 'f' in folder pplot.plotsFolder
		"""
		f = os.path.join(self.plotsFolder,f)
		return f

	#----------------------	
	def datafname(self,f):
		"""Return path to file 'f' in folder pplot.dataFolder
		"""
		f = os.path.join(self.dataFolder,f)
		return f
	
	#----------------------	
	def saveData(self,dataname,data):
		"""Store data in file in pplot standar format:
			x11 y12 z13 ...
			x21 y22 z23 ... 
			x31 y32 z33 ... 
				.
				. 
				. 			
		"""
		np.savetxt(dataname,data,delimiter = '\t',newline='\n')	

	#----------------------		
	def sampleplotXY(self):
		"""Plot with a sample data: y(x) = cos(x) in range [-2Pi,2Pi].
		"""
		self.dataname = self.datafname('sampledataXY.dat')
		self.plotname = self.plotfname('sampleplotXY.png')
		
		print "Ploting with \'%s\'" %(dataname)
		
		self.X = linspace(-2*pi,2*pi,100,endpoint=True)
		self.Y = cos(x)
		
		self.XY = np.array(zip(x,y),dtype=dtype)
		
		self.saveData(dataname,self.XY)
		
		self.pXY.plot(self.X, self.X, label = self.yLabel, color = self.colorDict['pblue'], lw = 2.0)
		
		self.pXY.legend(loc = 3)

		xlim(x.min(),x.max())
		ylim(y.min(),y.max())
		
		from math import floor, ceil
		xini = int(ceil(x.min()))
		xend = int(floor(x.max()))
		yini = int(ceil(y.min()))
		yend = int(floor(y.max()))				
		xticks = linspace(xini,xend,5,endpoint=True)
		yticks = linspace(yini,yend,5,endpoint=True)
		self.pXY.set_xticks(xticks)
		self.pXY.set_yticks(yticks)

		self.pXY.set_xlabel(self.xLabel, fontsize = 18)
		self.pXY.set_ylabel(self.yLabel, fontsize = 18)
		self.pXY.set_title('Sample data')
		
		
		self.fig.savefig(plotname, dpi = 100)
		
		print "Plot saved at \'%s\'" %(plotname)	
						
	#----------------------
	def plotXY(self,fName = None,SHOW = False):
		"""If no data is supplied, the sampleplotXY() method is executed.
		"""
		if fName is None:
			self.sampleplotXY()
			if SHOW:
				show()
				
	#----------------------				
	def showDoc(self):
		"""Print pplot's doc string
		"""
		print trim.trim(doc)
	def showDoc(self, f):
		"""Usefull to print <methodname>.__doc__.
		Example:
		'myplot.showDoc(myplot.showDoc.__doc__)'
		shows this very docs string without \\t, \\n or identation.
		"""
		print trim.trim(f)
	#----------------------			
	def saveDoc(self):
		out = open("documentation.txt","w")
		out.write(trim.trim(doc))			

a = pplot()
#a.plotXY(SHOW = True)
a.doc(a.showDoc().__doc__)



