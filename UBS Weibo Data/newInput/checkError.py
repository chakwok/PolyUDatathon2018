import json

List = []
idList =[]

for i in range(1 ,9):
	filename = '../weibo/Status_Data{:d}.json'.format(i)
	with open(filename, 'r') as f:
		data = json.loads(f.readline())
		count = 0 
		#print(data)
		for entry in data: 
			
			if (entry['id'] not in idList):
				List.append(json.dumps(entry))
				idList.append(entry['id'])
			else: 
				print("There is duplicate item with id: {}".format(entry['id']))
			count+=1 
		print("Number of Entries: {:d}".format(count))

with open('Oneline_Data2.json', 'w') as o:
	o.write('[')
	for entry in List:
		o.write("{}, ".format(entry))
	o.write(']')
	print(len(List))