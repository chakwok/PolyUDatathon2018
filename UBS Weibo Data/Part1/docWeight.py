import json
import re
import math
import pprint
import jieba

pp = pprint.PrettyPrinter()

# An array of sid
trainingSids = []

# num of post in training set 1229
NumPosts = 0 

# catId: [sid, sid ...]
categoryToSIDs = {}
sidsToCategory = {}

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
		sidsToCategory[sid] = int(category)
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
		#print(len(data))
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

tfIdfs = {}
def generateTfIds():
	for i in range(0, 13):
		tfIdfs[i] = {}

	with open('data_update.txt', 'r') as f: 
		data = json.loads(f.readline())
		#pp.pprint(data[0])
		count = 0
		for doc in data: 
			i = 0
			corpus = tfIdfs[sidsToCategory[doc[-1]]]
			while(i != len(doc) -1 ):
				#print(corpus)
				#print(i)
				#print(doc)
				#print(doc[i])
				#print(doc[i+1])
				if doc[i] not in corpus:
					corpus[(doc[i])] = (doc[i+1])
				else:
					corpus[doc[i]] += doc[i+1]
				i += 2
			count +=1
			#print("{:d} document has been processed".format(count))
	with open('tfIdf.txt', 'w') as o:
		o.write(json.dumps(tfIdfs))

generateTfIds()

def calculateDocWeight():
	# {sid: [train_label cat, cat1's score, cat2's score... cat13's score]}
	docDict = {}
	for entry in trainingData:
		docDict[(entry['id'])] = [(sidsToCategory[entry['id']])]
		for i in range(0, 13): 
			docDict[(entry['id'])].append(computeScore(entry['text'], i))
	#print(len(docDict))
	#pp.pprint(json.dumps(docDict))
	with open('output.txt', 'w') as o:
		o.write(json.dumps(docDict))

	with open('submissionTraining', 'w') as oo: 
		for key, value in docDict.items():
			oo.write("{:s}\t\t{:d}\n".format(key, value[0]))
		
	
	#with open('tfIdf.txt', 'r') as f:
#calculateDocWeight()

def isHashTag(text, word):
	if(text.find('#') == -1):
		return False
	if(text.find(word) < text.find('#',text.find('#'))):
		return True
	return False
		
def computeScore(text, category):
	score = 0 
	#print(text)
	#print((tfIdfs))
	tfIdfsList = tfIdfs[category]
	#print(type(tfIdfsList))
	for key, value in tfIdfsList.items():
		occ = text.count(key)
		if(occ != 0):
			score += value * occ
			print("score({}) += value({}) * count({})".format(score, value, occ))
			if(isHashTag(text, key)):
				score += value * occ
	return score

calculateDocWeight()







#print(computeScore(trainingData[0]['text'], 0))

testingData = []
appendedTestingData = [] 

def getAllTestingDataset(): 
	with open('combinedData.json', 'r') as g: 
		data = json.loads(g.readline())
		for entry in data: 
			if (entry['id'] not in trainingSids):
				testingData.append(entry)
				appendedTestingData.append(entry['id'])

getAllTestingDataset()
#print(len(testingData))
				

def processForPrediction():
	# {sid: [train_label cat, cat1's score, cat2's score... cat13's score]}
	docDict = {}
	for entry in testingData:
		docDict[(entry['id'])] = []
		for i in range(0, 13): 
			docDict[(entry['id'])].append(computeScore(entry['text'], i))
	#print(len(docDict))
	#pp.pprint(json.dumps(docDict))
	print(len(docDict))
	with open('testingSet.txt', 'w') as o:
		o.write(json.dumps(docDict))

processForPrediction()

