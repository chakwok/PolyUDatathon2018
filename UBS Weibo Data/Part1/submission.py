def main():
	with open('submission.txt', 'r') as f, open('submission9.txt', 'r') as g, open('finalSubmission.txt', 'w') as o : 
		lines = f.readlines()
		for line in lines:
			info = line.split(',')
			o.write("{:s}\t\t{:d}\n".format(info[1], int(float(info[2].strip()))))

		liness = g.readlines()
		for linee in liness:
			infoo = linee.split(',')
			o.write("{:s}\t\t{:d}\n".format(infoo[1], int(float(infoo[2].strip()))))



def checkSids():
	uniqueSids = []
	duplicateSids = []
	with open('finalSubmission.txt', 'r') as f: 
		lines = f.readlines() 
		for line in lines: 
			sid = line.split('\t')[0]
			if (sid not in uniqueSids):
				uniqueSids.append(sid)
			else: 
				duplicateSids.append(sid)
	print(len(uniqueSids))
	print(len(duplicateSids))
			

checkSids()