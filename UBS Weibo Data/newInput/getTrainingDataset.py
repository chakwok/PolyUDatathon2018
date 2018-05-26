import json
import re
import math
import pprint

pp = pprint.PrettyPrinter()

# An array of sid
trainingSids = []

# num of post in training set 1229
NumPosts = 0 

# catId: [sid, sid ...]
categoryToSIDs = {}

#initializing only
for i in range(0,13): 
	categoryToSIDs[i] = []

#An array of appended sid
appendedSids = []

# training data only [{data}, {data} ... ]
trainingData = []


with open('../weibo/train_label.txt', 'r') as f:
	count = 0 
	lines = f.readlines()
	for line in lines:
		sid = line.split('\t')[0]
		trainingSids.append(sid)
		category = line.split('\t')[2]
		count += 1
		categoryToSIDs[int(category)].append(sid)
	#to print the whole dict
	#print(categoryToSIDs)
	#print("Number of line: {:d}".format(count))
	#print((trainingSids))
	NumPosts = count

	# for i in range(0, 13): 
	# 	print("Category {:d}'s count: {:d}\n".format(i, len(categoryToSIDs[i])))

def getAllTrainingDataset(): 
	
	with open('combinedData.json', 'r') as g: 
		data = json.loads(g.readline())
		for entry in data: 
			if (entry['id'] in trainingSids):
				trainingData.append(entry)
				appendedSids.append(entry['id'])
		#print(len(trainingData))
		#print(len(appendedSids))

def removeNullFromTrainingSids():
	for ele in trainingSids:
		if (ele not in appendedSids):
			trainingSids.remove(ele)

	#print(len(trainingSids))

getAllTrainingDataset()
removeNullFromTrainingSids()


pp.pprint(trainingData)

def generateCatWords():
	categoryToJsons = {}
	categoryWords = {}
	for i in range(0,13): 
		categoryToJsons[i] = []
		categoryWords[i] = []


	#print(data)
	#category{:d}jsons are not used
	for i in range(0, 13): 
		filename = 'category{:d}jsons.txt'.format(i)
		filenamee = 'category{:d}words.txt'.format(i)
		with open(filename, 'w') as o, open(filenamee, 'w') as p:
			for sid in categoryToSIDs[i]: 
				for entry in trainingData: 
					if (sid == entry['id']):
						categoryToJsons[i].append(entry)
						p.write(json.dumps(entry["text"]))

			#o.write(json.dumps(categoryToJsons[i]))
	#print(categoryToJsons)
	#for i in range(0, 13): 
	 	#print("For the json file created, category {:d}'s count: {:d}\n".format(i, len(categoryToJsons[i])))

generateCatWords()


