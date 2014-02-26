from pylab import *
import matplotlib.pyplot as plt
import os

class pplot:
	"""pplot class: developed by Vagner Bessa. Contact: vagner.fisica@gmail.com. For more information, use 'showDoc()' method."""
	def showDoc(self):
		doc = 
		'pplot class'\
		'developed by Vagner Bessa.'\
		'			  Contact: vagner.fisica@gmail.com.' \
		'
		'
		return trim(doc)

def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)


#x = pplot()
#print x.showDoc()

