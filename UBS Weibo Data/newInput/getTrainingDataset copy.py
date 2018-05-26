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

with open('categoryToSIDs.txt', 'w') as o: 
	o.write(json.dumps(categoryToSIDs))

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
						p.write((entry["text"]))

			#o.write(json.dumps(categoryToJsons[i]))
	#print(categoryToJsons)
	#for i in range(0, 13): 
	 	#print("For the json file created, category {:d}'s count: {:d}\n".format(i, len(categoryToJsons[i])))

generateCatWords()

with open('temp.txt', 'w') as oo:
	for ele in trainingData:
		oo.write("{},\n".format(ele))

def getAllUniqueWords():
	uniqueWords = []
	for entry in trainingData: 
		words = (entry["text"])
		words = list(jieba.cut(words, cut_all=False))
		for word in words: 
			if (word not in uniqueWords):
				uniqueWords.append(word)
	#print(len(uniqueWords))
	#uniqueWords.remove(r'\ud83e')
	#uniqueWords.remove(r'\udd23')
	#uniqueWords.remove(r'\ud83d')
	return uniqueWords


getAllUniqueWords()

with open('temp2.txt', 'w') as ooo:
	for ele in getAllUniqueWords():
		ooo.write("{},\n".format(ele))



def computeIdfs():
	Idfs = {} 
	count = 0
	for word in getAllUniqueWords():
		print("computing the tfidf for {:d}th word: {}".format(count, word))
		idf = computeIdf(word)
		Idfs[word] = idf
		count += 1 
	return Idfs
	
def computeIdf(word): 
	print(word)
	count = 0 
	
	for entry in trainingData: 
		#print(word)
		#print(entry['text'])
		if (word in list(jieba.cut(entry['text'], cut_all=True))):
			count += 1 

	print(count)
	if (count == 0 ):
		count = 1229
	
	idf = math.log2(NumPosts / count)
	
	return idf

def computeTfIdf(): 
	Idfs = computeIdfs()
	with open('tfIdfs.json', 'w') as o:
		o.write('[')
		for i in range(0, 13): 
			filename = 'category{:d}words.txt'.format(i)
			#filenameWrite = 'tfidf{:d}.txt'.format(i)

			with open(filename, 'r') as f:
				tfIdfs = {}
				words = f.readline()
				words = list(jieba.cut(words, cut_all=False))
				for word in words: 
					if word not in tfIdfs:
						tfIdfs[word] = 1 
					else:
						tfIdfs[word] += 1 

				for word in words:
					try:
						tfIdfs[word] = tfIdfs[word] * Idfs[word]
					except: 
						continue

				tfIdfs['catId'] = str(i)
				o.write('{},'.format(json.dumps(tfIdfs)))
		o.write(']')


computeTfIdf()
