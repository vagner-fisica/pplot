from pylab import *
import matplotlib.pyplot as plt
import os, trim

doc = \
		'-------------------------------------------\n'\
		'pplot class\n'\
		'Developed by Vagner Bessa.\n'\
		'Contact: vagner.fisica@gmail.com.\n\n'\
		'Check README file for main informations.\n\n'\
		'This module has the MIT License (MIT)\nCopyright (c) 2014 Vagner Bessa.\n'\
		'-------------------------------------------\n'

class pplot:
	"""pplot class: developed by Vagner Bessa. Contact: vagner.fisica@gmail.com. For more information, use 'showDoc()' method."""
	def showDoc(self):
			print trim.trim(doc)
	def saveDoc(self,fName):
		if type(fName) is str:
			out = open(fName,"w")
			out.write(trim.trim(doc))
		else:
			out = open("documentation.txt","w")
			out.write(trim.trim(doc))			


x = pplot()
fName = 'documentation.dat'

x.saveDoc(fName)

