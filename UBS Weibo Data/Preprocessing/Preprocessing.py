import json

Ids = [ ]

def getAllIds():
	with open('Oneline_Data1.json', 'r') as f: 
		data = f.readlines()
		data = json.loads(data)
		print(data)
		#for line in data: 
		#	 print(line)

getAllIds()
print(Ids)