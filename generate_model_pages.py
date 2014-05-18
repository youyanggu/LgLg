# This is the script to generate the template for each of the Wiki pages, based 
# on the list of categories. To use, simply run the script and then copy the 
# output to the appropriate Wiki page (don't copy the 'TITLE' line). Some minor changes might then be needed.
#
# To generate a specific page(s), put the exact page name in the 'cat' array
#
# @Author: Youyang Gu

cat = [] # make this nonempty to generate specific pages, rather than all of them
hasSub = False
first = True
title = ""
category = ""
models_cat = open('models_cat.txt', 'r') # categories for problems

def print_infobox():
	print "{{Infobox\n|title = General Links\n| headerstyle = background-color:#eee;\n| labelstyle  = background-color:#eee;\n \
		|header1 = [[Main Page]]\n|data2 = [http://en.wikipedia.org/wiki/To_be_announced Wikipedia Page]\n \
		|header3 = Related Topics\n|data4 = [[TBA]]}}"

for line in models_cat:
	title = line[:-1]
	#print line
	if not (cat == [] or title in cat or category in cat): # only generate specific pages, as specified by 'cat' array
		if category in cat and line[0] != '-':
			category = ""
		continue
	if line[0] != '-': # Main category
		if first is False:
			if hasSub:
				pass
			else:
				pass
		hasSub = False
		first = False
		category = title
		if cat != [] and category not in cat:
			continue
		print "--------------------------------------------------------------------------------------------------------------------------------------------------------"
		print "TITLE: " + title + "\n\n"
		print_infobox()
		print "Here we present some useful resources related to " + category + ".\n"
		print "=== Resources ==="
		print "* [http://courses.csail.mit.edu/6.851/spring14/lectures/ MIT 6.851 Video & Notes]\n"
	else: # Subcategory
		hasSub = True
		title = title[1:]
		print "== " + title + " ==\n"
		print "''Currently empty''\n"


