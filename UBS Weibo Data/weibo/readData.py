import json

List = []

for i in range(1 ,9):
	filename = 'Status_Data{:d}.json'.format(i)
	with open(filename, 'r') as f:
		data = json.loads(f.readline())
		count = 0 
		#print(data)
		for entry in data: 
			List.append(json.dumps(entry))
			count+=1 
		print("Number of Entries: {:d}".format(count))

with open('Oneline_Data1.json', 'w') as o:
	o.write('[')
	for entry in List:
		o.write("{}, ".format(entry))
	o.write(']')