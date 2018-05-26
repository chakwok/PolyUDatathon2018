import json 
import pprint

pp = pprint.PrettyPrinter()

categoryToSIDs = {}
for i in range(0,13): 
	categoryToSIDs[i] = []

with open('../weibo/train_label.txt', 'r') as f: 
	count = 0 
	lines = f.readlines()
	for line in lines:
		sid = line.split('\t')[0]
		category = line.split('\t')[2]
		count +=1
		categoryToSIDs[int(category)].append(sid)
	#to print the whole dict
	#print(categoryToSIDs)
	print("Number of line: {:d}".format(count))

#to print the count of each cat
for i in range(0, 13): 
	print("Category {:d}'s count: {:d}\n".format(i, len(categoryToSIDs[i])))

print(categoryToSIDs[2])



def generateJson():
	categoryToJsons = {}
	for i in range(0,13): 
		categoryToJsons[i] = []

	with open('Oneline_Data1.json', 'r') as f:
		data = json.loads(f.readline())
		#print(data)
		for i in range(0, 13): 
			filename = 'category{:d}data.txt'.format(i)
			with open(filename, 'w') as o:
				for sid in categoryToSIDs[i]: 
					for entry in data: 
						if sid == entry['id']:
							categoryToJsons[i].append(entry)
							break


				o.write(json.dumps(categoryToJsons[i]))
	#pp.pprint(categoryToJsons)

	#for checking only
	for i in range(0, 13): 
		print("For the json file created, category {:d}'s count: {:d}\n".format(i, len(categoryToJsons[i])))
	print(categoryToJsons[2])


generateJson()