# Script to generate the categories drop-down list for the main LgLg page

first = True
lastLine = None
curLine = None
nextLine = None
title = ""
category = ""
models_cat = open('models_cat.txt', 'r') # categories for models
problems_cat = open('problems_cat.txt', 'r') # categories for problems
files = [models_cat, problems_cat]

for i in range(2):
	if i == 0: # models category
		cat_type = 'MODEL'
	else:
		cat_type = 'PROBLEMS'
	for line in files[i]:
		curLine = line[:-1]
		# delay curLine by one step, so that curLine is actually the last line we saw
		if lastLine is None:
			lastLine = curLine
			continue
		else:
			nextLine = curLine
			curLine = lastLine
			lastLine = line[:-1]
		if curLine[0] != '-': # curLine is main category
			if first is False:
				print "}}\n:"	
			category = curLine
			if cat_type == 'MODEL':
				category = ':Category:' + category + '|' + category
			if nextLine[0] != '-': # no subcategories --> no dropdown
				first = True
				print "'''[[" + category + "]]'''\n:"
			else: # has subcategories --> build collapsible list
				first = False
				print "{{collapsible list"
				print " | liststyle=padding-left:10px;"
				print " | title = '''[[" + category + "]]''' &nbsp;"
		else: # curLine is subcategory
			title = curLine[1:] # strip dash
			subcategory = "_".join(title.split())
			if cat_type == 'MODEL':
				c = category.split('|')[0]
			else:
				c = category
			print " | [["+c+"#"+subcategory+"|"+title+"]]"
	# special handling for last line of file
	if nextLine[0] == '-': 
		print " | [["+category+"#"+"_".join(nextLine[1:].split())+"|"+nextLine[1:]+"]]" # print last line
		print "}}"
	else:
		if cat_type == 'MODEL':
			print "'''[[:Category:" + nextLine + "|"+ nextLine + "]]'''"
		else:
			print "'''[[" + nextLine + "]]'''"
	first = True
	lastLine = None
	print "\n\n=====================================\n\n"
