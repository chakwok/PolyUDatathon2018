import json 
import pprint
import re 
import math 

pp = pprint.PrettyPrinter()

categoryToSIDs = {}
trainingSids =[]
for i in range(0,13): 
	categoryToSIDs[i] = []

NumPosts = 0 

with open('../weibo/train_label.txt', 'r') as f: 
	count = 0 
	lines = f.readlines()
	for line in lines:
		sid = line.split('\t')[0]
		trainingSids.append(sid)
		category = line.split('\t')[2]
		count +=1
		categoryToSIDs[int(category)].append(sid)
	#to print the whole dict
	#print(categoryToSIDs)
	print("Number of line: {:d}".format(count))
	NumPosts = count


#to print the count of each cat
for i in range(0, 13): 
	print("Category {:d}'s count: {:d}\n".format(i, len(categoryToSIDs[i])))

#print(categoryToSIDs[2])



def generateJson():
	categoryToJsons = {}
	for i in range(0,13): 
		categoryToJsons[i] = []

	with open('TrainDataOnly.json', 'r') as f:
		data = json.loads(f.readline())
		#print(data)
		for i in range(0, 13): 
			filename = 'category{:d}data.txt'.format(i)
			with open(filename, 'w') as o:
				for sid in categoryToSIDs[i]: 
					for entry in data: 
						if (sid == entry['id']):
							categoryToJsons[i].append(entry)
							break

				o.write(json.dumps(categoryToJsons[i]))

	#pp.pprint(categoryToJsons)

	#for checking only
	for i in range(0, 13): 
	 	print("For the json file created, category {:d}'s count: {:d}\n".format(i, len(categoryToJsons[i])))
	#print(categoryToJsons[2])

generateJson()


def generateTrainJson():
	with open('Oneline_Data1.json', 'r') as f, open('TrainDataOnly.json', 'w') as o:
		o.write('[')
		data = json.loads(f.readline())
		#print(data)
		for sid in trainingSids: 
			for entry in data: 
				if sid == entry['id']:
					o.write('{},'.format(json.dumps(entry)))
					
		o.write(']')

#generateTrainJson()


#generateJson()

def generateTotal(): 
	with open('TrainDataOnly.json', 'r') as f, open('allWords.txt', 'w') as o: 
		data = json.loads(f.readline())
		for entry in data:
			o.write(json.dumps(entry["text"]))
generateTotal()

def generateCategoryWords():
	for i in range(0, 13):
		filename = 'category{:d}data.txt'.format(i)
		filenameWrite = 'data{:d}words.txt'.format(i)
		with open(filename, 'r') as f, open(filenameWrite, 'w') as o: 
			data = json.loads(f.readline())
			for entry in data:
				o.write(json.dumps(entry["text"]))

generateCategoryWords()




def getAllUniqueWords(): 
	uniqueWords = []
	with open('allWords.txt', 'r') as f: 
		words = f.readline()
		#print(type(words))
		words = re.findall(r'\\u\w{4}', words)
		#pp.pprint(words)
		print("There are total {:d} words in total".format(len(words)))
		for word in words: 
			if word not in uniqueWords:
				uniqueWords.append(word)

		print("Total words: {:d}, Unique Words:{:d}".format(len(words), len(uniqueWords)))
	return uniqueWords


#generateDf()
#print(df)
#print("len(df) = {:d}".format(len(df)))

# num = 0
# max = 0
# for key,value in df.items():
# 	num += value
# 	if (value > max):
# 		max = value
# print("total count ={:d}, max = {:d}".format(num, max))


def computeIdfs():
	Idfs = {} 
	count = 0
	for word in getAllUniqueWords():
		#print("computing the tfidf for {:d}th word: {}".format(count, word))
		idf = computeIdf(word)
		
		Idfs[word] = idf
		count += 1 
		
	return Idfs
	
def computeIdf(word): 
	count = 0 
	with open('TrainDataOnly.json', 'r') as f:
		data = json.loads(f.readline())
		for entry in data: 
			#print(word)
			#print(entry['text'])
			if (re.search(word, entry['text']) != None):
				count += 1 

	
	
	idf = math.log2(NumPosts / count)
	
	return idf



def computeTfIdf(): 
	Idfs = computeIdfs()
	with open('tfIdfs.json', 'w') as o:
		o.write('[')
		for i in range(0, 13): 
			filename = 'data{:d}words.txt'.format(i)
			#filenameWrite = 'tfidf{:d}.txt'.format(i)

			with open(filename, 'r') as f:
				tfIdfs = {}
				words = f.readline()
				words = re.findall(r'\\u\w{4}', words)
				for word in words: 
					if word not in tfIdfs:
						tfIdfs[word] = 1 
					else:
						tfIdfs[word] += 1 

				for word in words:
						tfIdfs[word] = tfIdfs[word] * Idfs[word]

				tfIdfs['catId'] = str(i)
				o.write('{},'.format(json.dumps(tfIdfs)))
		o.write(']')


computeTfIdf()








