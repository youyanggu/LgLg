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
problems_cat = open('problems_cat.txt', 'r') # categories for problems

def print_infobox():
	print "{{Infobox\n|title = General Links\n| headerstyle = background-color:#eee;\n| labelstyle  = background-color:#eee;\n \
		|header1 = [[Main Page]]\n|data2 = [http://en.wikipedia.org/wiki/To_be_announced Wikipedia Page]\n \
		|header3 = Models Used\n|data4 = [[TBA]]}}"

def print_page(hasSub):
	# Generates the main section of the page
	if hasSub: # has subcategory --> No need for own result section
		print "== More Results ==\n"
	else: # has no subcategory --> Need its own results section
		print "== Results ==\n"
		print "=== Definitions ===\n"
		print "=== Bounds ===\n"
		print "{| class=\"wikitable\"\n!\n! Bound\n! Notes\n! Source\n! Year\n! Last Updated\n"
		print "|-\n|Description of bound\n|<math>O(?)</math>\n|? \n| <ref>F. LName. [http://link_to_source Title of source]. Rest of citation.</ref>\n|? \n|?"
		print "|}\n"
		print "=== Additional Results ===\n"
	print "== Resources ==\n{{reflist}}\n"
	print "[[Category:Model_name]]\n"

for line in problems_cat:
	title = line[:-1]
	if not (cat == [] or title in cat or category in cat): # only generate specific pages, as specified by 'cat' array
		if category in cat and line[0] != '-':
			category = ""
		continue
	if line[0] != '-': # Main category
		if first is False:
			print_page(hasSub)	
		hasSub = False
		first = False
		category = title
		if cat != [] and category not in cat:
			continue
		
		print "--------------------------------------------------------------------------------------------------------------------------------------------------------"
		print "TITLE: " + title + "\n\n"
		print_infobox()
		print "Here we present some useful learning resources related to " + category + ".\n"
		print "=== General Resources ==="
		print "* [http://courses.csail.mit.edu/6.851/spring14/lectures/ MIT 6.851 Video & Notes]\n"
	else: # Subcategory
		hasSub = True
		title = title[1:]
		print "== " + title + " ==\n"
		print "=== Resources ===\n"
		print "=== Definitions ===\n"
		print "=== Bounds ===\n"
		print "{| class=\"wikitable\"\n!\n! Bound\n! Notes\n! Source\n! Year\n! Last Updated\n"
		print "|-\n|Description of bound\n|<math>O(?)</math>\n|? \n| <ref>F. LName. [http://link_to_source Title of source]. Rest of citation.</ref>\n|? \n|?"
		print "|}\n"
		print "=== Additional Results ===\n"
print_page(hasSub) # special handling for last category

