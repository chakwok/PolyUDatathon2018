import codecs
with codecs.open('summary_table_comments.csv', "r",encoding='utf-8', errors='ignore') as f:
	provinceList = {}
	cityList = {}
	provinceCityList = {}
	for i in range(0, 13): 
		provinceList[i] = []
		cityList[i] = [] 
		provinceCityList[i] = [] 

	
	#str = unicode(f.readlines(), errors='replace')
	lines = f.readlines()
	for line in lines:
		print(len(line.split()))
		proId = line.split()[12] + line.split()[14]
		print(proId)
	#print(lines)